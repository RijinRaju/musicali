import os
import pathlib
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from keras_preprocessing.image import load_img
from sklearn.preprocessing import LabelEncoder


TEST_DIR =  os.path.join(os.getcwd(),'data', 'images', 'test')
TRAIN_DIR = os.path.join(os.getcwd(),'data', 'images', 'train')



def create_data_frame(dir):
    """
    
    """
    image_paths =[]
    labels = []

    for label in os.listdir(dir):
        for img_name in os.listdir(os.path.join(dir, label)):
            image_paths.append(os.path.join(dir,label,img_name))
            labels.append(label)

    return image_paths, labels


def extract_features(images):
    """
    
    """
    features = []
    for image in tqdm(images):
        img =  load_img(image, color_mode='grayscale')
        img = np.array(img)
        features.append(img)
    features = np.array(features)
    features = features.reshape(len(features), 48,48,1)
    return features


def label_encoder(train_label, test_label):
    """
    
    """
    le = LabelEncoder()
    le.fit(y= train_label)
    y_train = le.transform(train_label)
    y_test = le.transform(test_label)
    y_train = to_categorical(y_train, num_classes=7)
    y_test = to_categorical(y_test, num_classes=7)
    
    return y_test, y_train

def build_model(input_shape):

    model = Sequential()

    model.add(Conv2D(128, kernel_size=(3,3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(512, kernel_size=(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(512, kernel_size=(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.4))

    # flattern the layer
    model.add(Flatten())

    # fully connected layer
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.3))

    # ouput layer
    model.add(Dense(7, activation='softmax'))

    # model compilation
    model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    return model


if __name__ == "__main__":

    # create datframe with image path and labels for train
    train = pd.DataFrame()
    train['image'], train['label'] = create_data_frame(TRAIN_DIR)

    # create datframe with image path and labels for test
    test = pd.DataFrame()
    test['image'], test['label'] = create_data_frame(TEST_DIR)

    # extract  the features from  datasets
    train_features = extract_features(train['image'])
    test_features = extract_features(test['image'])

    # normalization 
    x_train = train_features / 255.0
    x_test = test_features / 255.0

    # encode the labels converting non-numerical values to numerical values
    y_test, y_train = label_encoder(train['label'], test['label'])
    
    # create the cnn model 
    input_shape = (48,48,1)
    model = build_model(input_shape)

    # training the model
    model.fit(x_train,y_train, batch_size=128, epochs=15, validation_data=(x_test,y_test))

    # save the model architecture to json
    model_json = model.to_json()
    with open("emotiondetector.json", 'w') as json_file:
        json_file.write(model_json)
    model.save("emotiondetector.h5")
