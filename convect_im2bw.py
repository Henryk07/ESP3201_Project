import os
from PIL import Image
import glob 


directory="S_datas_labels" # ENTER HERE THE SOURCE DIRECTORY PATH
goaldirec="S_datas_labels_bw" #ENTER HERE THE GOAL DIRECTORY PATH (has to be created, with its sub-folders F,M,N...)

for pathdir in glob.glob(directory+"/*"):
    dirname=os.path.normpath(pathdir)
    dirlab=os.path.basename(os.path.normpath(dirname))

    for imgpath in glob.glob(dirname+"/*.png"):

        imgname=os.path.normpath(imgpath)

        with Image.open(imgname) as im:
            gray = im.convert("L")
            bw = gray.point(lambda x: 0 if x < 200 else 255, 'L')
            rootpath=os.path.basename(os.path.normpath(imgname))
            bw.save(goaldirec+"//"+dirlab+"//bw_"+rootpath)
