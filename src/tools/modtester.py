# Initialization : importing useful libraries
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import tensorflow as tf
import pathlib

from tensorflow import keras
import sklearn.metrics as sk
from skimage import transform

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import sys
sys.path.append("..")

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

    classes = np.argmax(prediction, axis=1)

    for i, clas in enumerate(classes):
        print(f"Image {i} || Predicted Disease : " +
              dict[clas] + " || True Disease : "+dict[labels_brut[i]])


def confusionmatrix(model, datatest):
    predata = datatest.unbatch()
    labels = list(predata.map(lambda x, y: y))
    labels_brut = []

    for i in range(len(labels)):  # gets the list of the predicted label for each image
        labels_brut.append(tf.get_static_value(labels[i]))

    prediction = model.predict(datatest)
    print("test")
    classes = np.argmax(prediction, axis=1)
    ConfusionMatrixDisplay.from_predictions(labels_brut, classes)

# generates tests from model path


def testmodel(modelpath, color):
    model = tf.keras.models.load_model(modelpath)

    if color == True:
        hugedata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_training_datas_labels", shuffle=False)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_prediction_datas_labels", shuffle=False)

        modeltest(model, predictdata)
        confusionmatrix(model, hugedata)

    else:
        simpledata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_datas_labels_cb_bw", shuffle=False, batch_size=5)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_prediction_datas_labels_bw", shuffle=False, batch_size=5)

        modeltest(model, predictdata)
        confusionmatrix(model, simpledata)


def testmodeldemo(modelpath, directorypath):
    model = tf.keras.models.load_model(modelpath)

    predictdata = tf.keras.utils.image_dataset_from_directory(
        directorypath, shuffle=False, batch_size=5)

    modeltest(model, predictdata)
# generates test from model


def directmodeltest(model, color):

    if color == True:
        hugedata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_training_datas_labels", shuffle=False)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_prediction_datas_labels", shuffle=False)

        modeltest(model, predictdata)
        confusionmatrix(model, hugedata)

    else:
        simpledata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_datas_labels_cb_bw", shuffle=False, batch_size=5)
        predictdata = tf.keras.utils.image_dataset_from_directory(
            "data/Small_dataset/S_prediction_datas_labels_bw", shuffle=False, batch_size=5)

        modeltest(model, predictdata)
        confusionmatrix(model, simpledata)

# creates a single batch from one image


def read_one_image(path):

    np_image = Image.open(path)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (256, 256, 3))
    np_image = np.expand_dims(np_image, axis=0)

    label = os.path.dirname(path)[-1]
    lab = 0

    if label == "F":
        lab = 0
    elif label == "M":
        lab = 1
    elif label == "N":
        lab = 2
    elif label == "Q":
        lab = 3
    elif label == "S":
        lab = 4
    else:
        lab = 5
    return (np_image, lab)


def create_list_of_predictions(modelpath, datas):
    model = tf.keras.models.load_model(modelpath)
    # save the name of the model for the confusion matrix save
    modelname = os.path.basename(modelpath)
    modelname = modelname[:-3]

    # list of images from the validation data
    file_paths = datas.file_paths
    listofimages = []

    # list of useful labels
    listoftruelabels = []
    listofpredictions = []
    for path in file_paths:
        process = read_one_image(path)
        listofimages.append(process[0])
        listoftruelabels.append(process[1])
        pred = model.predict(process[0], verbose=0)
        classe = np.argmax(pred, axis=1)
        listofpredictions.append(classe[0])

    matrix = ConfusionMatrixDisplay.from_predictions(
        listofpredictions, listoftruelabels, display_labels=["F", "M", "N", "Q", "S", "V"])
    matrix.figure_.savefig("pictures/conf_matrix_"+modelname+".png")
    report = sk.classification_report(listofpredictions, listoftruelabels)
    print(report)
