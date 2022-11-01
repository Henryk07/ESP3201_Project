from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from tensorflow import keras
import pathlib
import tensorflow as tf
import PIL
import os
import numpy as np
import matplotlib.pyplot as plt
import modtester as tester

# Initialization : importing useful libraries
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
import pathlib

from tensorflow import keras

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from keras.preprocessing import image

# Model test function
# This function takes in argument a saved model and a batch of images to be predicted from a directory


def modeltest(model, datatest):

    predata = datatest.unbatch()
    labels = list(predata.map(lambda x, y: y))
    labels_brut = []

    for i in range(len(labels)):  # gets the list of the predicted label for each image
        labels_brut.append(tf.get_static_value(labels[i]))

    dict = {0: "F", 1: "M", 2: "N", 3: "Q", 4: "S", 5: "V"}
    prediction = model.predict(datatest)
    prediction_prob = classifier.predict_proba(datatest)
    print(prediction_prob)

    classes = np.argmax(prediction, axis=1)
    classes_prob = np.argmax(prediction_prob, axis=1)

    for i, clas in enumerate(classes):
        print(f"Image {i} || Predicted Disease : " +
              dict[clas] + " || True Disease : "+dict[labels_brut[i]])
        print(classes_prob)


#"|| True Disease : "+dict[clas_p]


def confusionmatrix(model, datatest):
    predata = datatest.unbatch()
    labels = list(predata.map(lambda x, y: y))
    labels_brut = []

    for i in range(len(labels)):  # gets the list of the predicted label for each image
        labels_brut.append(tf.get_static_value(labels[i]))

    prediction = model.predict(datatest)
    classes = np.argmax(prediction, axis=1)

    ConfusionMatrixDisplay.from_predictions(labels_brut, classes)

# generates tests from model path


def testmodel(modelpath, color):
    model = tf.keras.models.load_model(modelpath)

    if color == True:
        hugedata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_training_datas_labels", shuffle=False)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_prediction_datas_labels", shuffle=False)

        modeltest(model, predictdata)
        confusionmatrix(model, hugedata)

    else:
        simpledata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_datas_labels_cb_bw", shuffle=False, batch_size=5)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_prediction_datas_labels_bw", shuffle=False, batch_size=5)

        modeltest(model, predictdata)
        confusionmatrix(model, simpledata)

# generates test from model


def directmodeltest(model, color):

    if color == True:
        hugedata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_training_datas_labels", shuffle=False)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_prediction_datas_labels", shuffle=False)

        modeltest(model, predictdata)
        confusionmatrix(model, hugedata)

    else:
        simpledata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_datas_labels_cb_bw", shuffle=False, batch_size=5)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "Small_dataset/S_prediction_datas_labels_bw", shuffle=False, batch_size=5)

        modeltest(model, predictdata)
        confusionmatrix(model, simpledata)


tester.testmodel('src/model/model_20E_fulldata.h5', True)
