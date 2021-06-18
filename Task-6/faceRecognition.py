#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np


# In[ ]:


# Load HAAR Cascade face classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Setting file path for storing and retrieving data
path = './faces/user/'


# ## Face Extractor

# In[ ]:


# Function detects faces and returns cropped image | Returns None if no face detected
def face_extractor(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray, 1.3, 5)
    
    if len(face) == 0:
        return None
    
    # Crop detected faces
    (x, y, w, h) = face[0]
    cropped_face = frame[y:y+h, x:x+w]
    return cropped_face


# ## Sample Collection

# In[ ]:


cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    face = face_extractor(frame)
    if face is not None:
        count += 1
        face = cv2.resize(face, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
        # Save file in the specified directory with a unique name
        file_path = path + str(count) + '.jpg'
        cv2.imwrite(file_path, face)
        
        cv2.putText(face, str(count), (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,0,0], 1)
        cv2.imshow('samples', face)
        
    else:
        print("Face not found")
        pass
    
    if cv2.waitKey(10) == 13 or count == 500:
        break
        
cv2.destroyAllWindows()
print("Sample Collection Complete")
cap.release()


# ## Training the Model

# In[ ]:


from os import listdir
from os.path import isfile, join


# In[ ]:


# Fetching the paths of sample data for training
data_path = path
file_paths = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Lists for training data and labels
training_data, labels = [], []

# Open images from the file paths and create numpy array for training data
for i, f_path in enumerate(file_paths):
    image_path = data_path + f_path
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    training_data.append(np.asarray(images, dtype=np.uint8))
    labels.append(i)
    
# Create numpy array for both training data and labels
labels = np.asarray(labels, dtype=np.int32)
training_data = np.asarray(training_data)


# In[ ]:


# Initialize the face recognizer model
my_model = cv2.face_LBPHFaceRecognizer.create()

# Training the model
my_model.train(training_data, labels)
print("Model Trained")


# ## Run Facial Recognition

# In[ ]:


def detect_face(frame, size=0.5):
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray, 1.3, 5)
    
    if len(face) == 0:
        return None
    
    (x, y, w, h) = face[0]
    cv2.rectangle(frame, (x, y), (x+w, y+h), [178, 255, 25], 2)
    roi = frame[y:y+h, x:x+w]
    roi = cv2.resize(roi, (200, 200))
    return roi


# In[ ]:


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    face = detect_face(frame)
    
    try:
        grayface = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
        # Passing face to the model for prediction
        result = my_model.predict(grayface)
        
        if result[1] < 500:
            confidence = int(100 * (1 - result[1]/400))
            display_str = 'Confidence score : ' + str(confidence) + '%'
            
        cv2.putText(frame, display_str, (230, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,120,150], 1)
        
        if confidence > 90:
            cv2.putText(frame, "Hey Gaius", (276, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [178, 255, 25], 1)
        else:
            cv2.putText(frame, "Face not recognized", (240, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [80,19,247], 1)
        
    except:
        cv2.putText(frame, "Face not found", (260, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,255,255], 1)
        cv2.putText(frame, "Looking for a face", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,255,255], 1)
    cv2.imshow('Face Recognition', frame)
        
    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
cap.release()

