import os
import cv2
import time
import numpy as np
from keras.models import model_from_json




# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the JSON file
json_file_path = os.path.join(os.getcwd(),'models', 'emotiondetector.json')
weighted_model_file_path = os.path.join(os.getcwd(),'models', 'emotiondetector.h5')


def extract_features(image):
    """
    extract the features from the image like converting to array

    Args:
        image as an input
    Returns:
        return a array repr. of the image after normalization.
    """
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return feature/255.0



def detect_emotion():
    """
    capture the live video using opencv and feed into the model
    Returns:
        return the list of emotions
    """
    # load the pretrained model 
    json_file = open(json_file_path, 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)

    # load the model with weights
    model.load_weights(weighted_model_file_path)


    # load the har cascade classifier for face detection 
    haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(haar_file)

    # set custom timer
    start_time = time.time()
    duration = 10

    emotions = []

    # open the camera
    cap = cv2.VideoCapture(0)

    labels = {0:"angry",1:"disgust",2:"fear",3:"happy",4:"neutral",5:"sad",6:"surprise"}

    while labels:

        if time.time() - start_time > duration:
            return emotions

        # read a frame from webcam 
        i, im = cap.read()

        # convert to grayscale
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(im, 1.3, 5)
        
        try:
            # For each detected face, perform facial emotion recognition
            for (p, q, r, s) in faces:
                # Extract the region of interest (ROI) which contains the face
                image = gray[q:q + s, p:p + r]

                # Draw a rectangle around the detected face
                cv2.rectangle(im, (p, q), (p + r, q + s), (255, 0, 0), 2)

                # Resize the face image to the required input size (48x48)
                image = cv2.resize(image, (48, 48))

                # Extract features from the resized face image
                img = extract_features(image)

                # Make a prediction using the trained model
                pred = model.predict(img)

                emotions.append(labels[pred.argmax()])

            # Break the loop if ESC is pressed 
            if cv2.waitKey(1) ==27:
                break

        except cv2.error:
            pass

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()