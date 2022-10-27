import os
import random
from PIL import Image
import glob

# THIS CODE TO CREATE A NEW SAMPLES DIRECTORY WITH BALANCED NUMBER OF DATAS FROM EACH CATEGORY


def balancedatas(n, directorypath, sourcedirectory):  # enter source directory

    directorypath = "M_dataset"  # ENTER HERE THE SOURCE DIRECTORY PATH

    # ENTER HERE THE GOAL DIRECTORY PATH (has to be created, with its sub-folders F,M,N...)
    sourcedirectory = "Full_dataset/ECG_Image_data_cb_bw"

    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n))
    # ENTER THE PATH OF THE FOLDER WHERE YOU WANT TO CREATE THE NEW DATASET
    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n)+"/M")
    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n)+"/N")
    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n)+"/V")
    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n)+"/F")
    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n)+"/S")
    os.mkdir(directorypath+"/S_datas_labels_bw_bal"+str(n)+"/Q")

    for pathdir in glob.glob(sourcedirectory+"/*"):
        dirname = os.path.normpath(pathdir)
        dirlab = os.path.basename(os.path.normpath(dirname))
        img_path_list = glob.glob(dirname+"/*.png")
        nb_images = len(img_path_list)
        img_path_list_dest = []

        while len(img_path_list_dest) != n:
            ran = random.randrange(nb_images)
            if (img_path_list[ran]) not in img_path_list_dest:
                img = Image.open(img_path_list[ran])
                imgname = os.path.normpath(img_path_list[ran])
                rootpath = os.path.basename(os.path.normpath(imgname))
                img.save(directorypath+"/S_datas_labels_bw_bal" +
                         str(n)+"/"+dirlab+"//"+rootpath)
                img_path_list_dest = glob.glob(
                    directorypath+"/S_datas_labels_bw_bal"+str(n)+"/"+dirlab+"/*.png")


# ENTER
# first argument : number of images in each category (should be 803)
# second argument : location of the new directory
# third argument : location of the source directory (including the parent directory)
balancedatas(2000, "M_dataset", "Full_dataset/ECG_Image_data_cb_bw")
