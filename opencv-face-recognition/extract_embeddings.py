# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import pickle
import cv2
import os

# construct the paths and declaration of constants
MIN_CONFIDENCE = 0.5
dataset_path = "dataset"
embeddings_path = "output/embeddings.pickle"
detector = "face_detection_model"
embedding_model = "openface_nn4.small2.v1.t7"
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

# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(dataset_path))

# initialize our lists of extracted facial embeddings and
# corresponding people names
knownEmbeddings = []
knownNames = []

# initialize the total number of faces processed
total = 0

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	# load the image, resize it to have a width of 600 pixels
    	# and took the dimensions
	image = cv2.imread(imagePath)
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

	# ensure at least one face was found
	if len(detections) > 0:
		# we're making the assumption that each image has only ONE
		# face, so find the bounding box with the largest probability
		i = np.argmax(detections[0, 0, :, 2])
		confidence = detections[0, 0, i, 2]

		# ensure that the detection with the largest probability also
		# means our minimum probability test (thus helping filter out
		# weak detections)
		if confidence > MIN_CONFIDENCE:
			# compute the (x, y)-coordinates of the bounding box for
			# the face
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# extract the face ROI and grab the ROI dimensions
			face = image[startY:endY, startX:endX]
			(fH, fW) = face.shape[:2]

			# ensure the face width and height are sufficiently large
			if fW < 20 or fH < 20:
				continue

			# construct a blob for the face ROI, then pass the blob
			# through our face embedding model to obtain the 128-d
			# quantification of the face
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
				(96, 96), (0, 0, 0), swapRB=True, crop=False)
			embedder.setInput(faceBlob)
			vec = embedder.forward()

			# add the name of the person + corresponding face
			# embedding to their respective lists
			knownNames.append(name)
			knownEmbeddings.append(vec.flatten())
			total += 1

# dump the facial embeddings + names to disk
print("[INFO] serializing {} encodings...".format(total))
data = {"embeddings": knownEmbeddings, "names": knownNames}
f = open(embeddings_path, "wb")
f.write(pickle.dumps(data))
f.close()
