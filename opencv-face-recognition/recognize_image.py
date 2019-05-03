# import the necessary packages
import numpy as np
import imutils
import pickle
import cv2
import os

# construct the paths and declaration of constants
image_path = "images/emily.jpg" # path to input image
detector = "face_detection_model" # path to OpenCV's deep learning face detector
embedding_model = "openface_nn4.small2.v1.t7" # path to OpenCV's deep learning face embedding model
recognizer_path = "output/recognizer.pickle" # path to model trained to recognize faces
le_path = "output/le.pickle" # path to label encoder
MIN_CONFIDENCE = 0.5 # minimum probability to filter weak detections
DNN = "TF"

# load our serialized face detector from disk
print("[INFO] loading model...")

if DNN == "CAFFE":
    modelFile = "face_detection_model/res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile= "face_detection_model/deploy.prototxt"
    
    # Here we need to read our pre-trained neural net created using Caffe
    detector = cv2.dnn.readNetFromCaffe(configFile, modelFile)
else:
    modelFile = "face_detection_model/opencv_face_detector_uint8.pb"
    configFile= "face_detection_model/opencv_face_detector.pbtxt"
    
    # Here we need to read our pre-trained neural net created using Tensorflow
    detector = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

print("[INFO] model loaded.")


# load our serialized face embedding model from disk
print("[INFO] loading face recognizer...")
embedder = cv2.dnn.readNetFromTorch(embedding_model)

# load the actual face recognition model along with the label encoder
recognizer = pickle.loads(open(recognizer_path, "rb").read())
le = pickle.loads(open(le_path, "rb").read())

# load the image, resize it to have a width of 600 pixels (while
# maintaining the aspect ratio), and then grab the image dimensions
image = cv2.imread(image_path)
image = imutils.resize(image, width=600)
(h, w) = image.shape[:2]

# construct a blob from the image
imageBlob = cv2.dnn.blobFromImage(
	cv2.resize(image, (300, 300)), 1.0, (300, 300),
	(104.0, 177.0, 123.0), swapRB=False, crop=False)

# apply OpenCV's deep learning-based face detector to localize
# faces in the input image
detector.setInput(imageBlob)
detections = detector.forward()

# loop over the detections
for i in range(0, detections.shape[2]):
	# extract the confidence (i.e., probability) associated with the
	# prediction
	confidence = detections[0, 0, i, 2]

	# filter out weak detections
	if confidence > MIN_CONFIDENCE:
		# compute the (x, y)-coordinates of the bounding box for the
		# face
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		# extract the face ROI
		face = image[startY:endY, startX:endX]
		(fH, fW) = face.shape[:2]

		# ensure the face width and height are sufficiently large
		if fW < 20 or fH < 20:
			continue

		# construct a blob for the face ROI, then pass the blob
		# through our face embedding model to obtain the 128-d
		# quantification of the face
		faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
			(0, 0, 0), swapRB=True, crop=False)
		embedder.setInput(faceBlob)
		vec = embedder.forward()

		# perform classification to recognize the face
		preds = recognizer.predict_proba(vec)[0]
		j = np.argmax(preds)
		proba = preds[j]
		name = le.classes_[j]

		# draw the bounding box of the face along with the associated
		# probability
		text = "{}: {:.2f}%".format(name, proba * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(image, (startX, startY), (endX, endY),
			(0, 0, 255), 2)
		cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
