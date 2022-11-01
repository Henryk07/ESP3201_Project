This folder contains the AugMix functions used to augmented our datas. 

augmentations.py contains all the possible different augmentation possible for AugMix. 
augment_and_mix.py contains the function to augment one single image. 
createaugmentations.py contains the function to call to create a new directory with augmented datas. 


# HOW TO CREATE AN AUGMENTED DATASET 

1. Go to createaugmentations.py. 

2. Modify the parameter at the end of the file:

first argument : number of images targeted in each (can be MORE THAN 803)
second argument : location of the new directory
third argument : location of the source directory (including the parent directory)

 augmentationdata(50, "Small_dataset", "Small_dataset/S_datas_labels_cb_bw")

3. Run the file. A new dataset directory is created. 

4. Go to augmentationNN.ipynb notebook. Modify the name of the source directory (the one that has just been created) and the new model name.

5. Run the notebook with the augmented datas.