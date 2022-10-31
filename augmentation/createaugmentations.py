import os
from PIL import Image
import glob
import augment_and_mix as am
from PIL import Image
import numpy as np
import os
import random

def augmentationdata(n, directorypath, sourcedirectory):  # enter source directory

    # ENTER HERE THE SOURCE DIRECTORY PATH

    # ENTER HERE THE GOAL DIRECTORY PATH (has to be created, with its sub-folders F,M,N...)

    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n))
    # ENTER THE PATH OF THE FOLDER WHERE YOU WANT TO CREATE THE NEW DATASET
    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n)+"/M")
    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n)+"/N")
    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n)+"/V")
    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n)+"/F")
    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n)+"/S")
    os.mkdir(directorypath+"/S_datas_labels_augmented"+str(n)+"/Q")

    for pathdir in glob.glob(sourcedirectory+"/*"):
        dirname = os.path.normpath(pathdir)
        dirlab = os.path.basename(os.path.normpath(dirname))
        img_path_list = glob.glob(dirname+"/*.png")
        nb_images = len(img_path_list)
        img_path_list_dest = []
        print(dirlab)

        for i in range(len(img_path_list)): #copy all existing images to new directory
            img = Image.open(img_path_list[i])
            imgname = os.path.normpath(img_path_list[i])
            rootpath = os.path.basename(os.path.normpath(imgname))
            img.save(directorypath+"/S_datas_labels_augmented"+str(n)+"/"+dirlab+"//"+rootpath)
            img_path_list_dest = glob.glob(directorypath+"/S_datas_labels_augmented"+str(n)+"/"+dirlab+"/*.png")
        j=0
        while len(img_path_list_dest) != n: #complete new directory with augmented images 
            j+=1 #reference of the augmentation
            ran = random.randrange(nb_images)
            im = Image.open(img_path_list[ran])

            #pre-processing the image for the AugMix augmentations
            rgb_image = im.convert('RGB')
            rgbarray = np.asarray(rgb_image)
            rgbfloat=rgbarray.astype(np.float32)

            #Applying the Augmix augmentations
            augmentedimg=am.augment_and_mix(rgbfloat)
            
            #Converting back the image to an array to be saved
            augarray=Image.fromarray(augmentedimg.astype('uint8'), 'RGB')

            #Name of the image processing
            imgname = os.path.normpath(img_path_list[ran])
            rootpath = os.path.basename(os.path.normpath(imgname))

            #Saving the image
            augarray.save(directorypath+"/S_datas_labels_augmented"+str(n)+"/"+dirlab+"//"+rootpath+"aug"+str(j)+".png")
            img_path_list_dest = glob.glob(directorypath+"/S_datas_labels_augmented"+str(n)+"/"+dirlab+"/*.png")


# ENTER
# first argument : number of images in each category (should be 803)
# second argument : location of the new directory
# third argument : location of the source directory (including the parent directory)
augmentationdata(50, "Small_dataset", "Small_dataset/S_training_datas_labels")