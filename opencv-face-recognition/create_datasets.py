
import cv2 # Import OpenCV2 for image processing
import os   # Import os for file path

# Checks if the directory exists else create a new directory
def check_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


# Start capturing video
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('face_detection_model/haarcascade/haarcascade_frontalface_default.xml')

# For each person, one face id
face_id = 1

# Initialize sample face image
count_frame = 0

name = input('Enter your name : ')

check_path_exists("dataset/"+name+"/")

# Start looping
while(True):

    # Capture video frame
    ret, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles and tries to set them to scale
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (0,0,0), 2)

        # Increment sample face image
        count_frame += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("train_img/"+name+"/img_"+ str(count_frame) + ".jpg", gray)
        #cv2.imwrite("dataset/Action_" + str(count_frame) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 15, stop taking video
    elif count_frame > 30:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
