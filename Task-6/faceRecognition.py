#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import smtplib, ssl
import pywhatkit


# ## Functions to send mail and WhatsApp message if Face is recognized

# In[ ]:


def sendMail(sender_email, password, receiver_email, message):
    port = 465  # For SSL
    
    # Setting smtp server
    smtp_server = "smtp.gmail.com"
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# In[ ]:


def sendWhatsMessage(phoneno, message):
    message = "Hey ... i sent this using python lol , just testing some stuff out , please ignore"
    pywhatkit.sendwhatmsg_instantly(phoneno, message)


# ## Face Extractor

# In[ ]:


# Load HAAR Cascade face classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Setting file path for storing and retrieving data
path = './faces/user/'


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
count = 500    # size of sample (number of images needed)

while True:
    ret, frame = cap.read()
    face = face_extractor(frame)
    if face is not None:
        count -= 1
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
    
    if cv2.waitKey(10) == 13 or count <= 0:
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
correction = 50 # Number of times the user's face must bre read correctly before sending the mail
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
            c += 1
            if c >= correction:
                # Fetching from_email, password, to_email, phone_number
                creds = open("password.txt", "r")
                sender_email = creds.readline()
                password = creds.readline()
                receiver_email = creds.readline()
                phoneno = creds.readline()
                creds.close()
                
                message = """Subject: Face ID Verified

                Greetings Gaius Reji
                """
                
                # Calling function to send Email
                sendMail(sender_email, password, receiver_email, message)
                print("Email sent")
                
                # Calling function to send WhatsApp Message
                sendWhatsMessage(phoneno, message)
                print("WhatsApp message sent")
                break
        else:
            cv2.putText(frame, "Face not recognized", (240, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [80,19,247], 1)
            c = 0
        
    except:
        cv2.putText(frame, "Face not found", (260, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,255,255], 1)
        cv2.putText(frame, "Looking for a face", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255,255,255], 1)
        c = 0
    cv2.imshow('Face Recognition', frame)
        
    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
cap.release()

