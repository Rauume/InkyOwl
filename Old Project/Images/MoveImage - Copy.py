import os
import shutil
import glob
import random

    
    #os.rename("Shown", "NextToShow")
    #os.rename("Next", "Shown")
    #os.rename("NextToShow", "Next")
    
metaImageList = "C:/Users/cam/Desktop/New folder/Project/Images/ImagesMetaInfo.txt"
    
#try to get files in current directory
imagesDirectory = "C:/Users/cam/Desktop/New folder/Project/Images"
#print(''.join([imagesDirectory, "/*.jpg"]))

files = glob.glob(''.join([imagesDirectory, "/*.jpg"]))
dest = ''.join([imagesDirectory, "/Shown"])

#if no images in current directory
if not (files):
    #get files from the 'already shown' directory
    files = glob.glob(''.join([dest, "/*.jpg"]))
    
    #move files from 'already shown' to 'yet to show'
    for f in enumerate(files, 0):
        shutil.move(f[1], os.path.join(imagesDirectory, os.path.basename(str(f[1]))))
        print(os.path.basename(str(f[1])))
        
#try get files again
files = glob.glob(''.join([imagesDirectory, "/*.jpg"]))
to_be_moved = random.sample(files, 1)     

if not os.path.exists(dest):
    os.makedirs(dest)

shutil.move(to_be_moved[0], dest)