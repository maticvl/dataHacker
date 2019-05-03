# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import numpy as np
import argparse
import pickle

# construct the paths
embeddings_path = "output/embeddings.pickle"
recognizer_path = "output/recognizer.pickle"
le_path = "output/le.pickle"


# load the face embeddings
print("[INFO] loading face embeddings...")
data = pickle.loads(open(embeddings_path, "rb").read())

# encode the labels
print("[INFO] encoding labels...")
le = LabelEncoder()
labels = le.fit_transform(data["names"])

# train the model based on the 128-d feature vector embeddings of the face
# then produce the actual face recognition
print("[INFO] training model...")

recognizer = SVC(C=1.0, kernel="linear", probability=True)

recognizer.fit(data["embeddings"], labels)

# write the actual face recognition model to disk
f = open(recognizer_path, "wb")
f.write(pickle.dumps(recognizer))
f.close()

# write the label encoder to disk
f = open(le_path, "wb")
f.write(pickle.dumps(le))
f.close()
