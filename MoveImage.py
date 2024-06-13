from asyncio.windows_events import NULL
from cmath import inf
from genericpath import exists
import os
import shutil
import glob
import random

    
imagesDirectory = "C:/Users/cam/Desktop/New folder/Project/Images/"
metaImageList = ''.join([imagesDirectory, "ImagesMetaInfo.txt"])

totalImages = glob.glob('*.jpg')
seenImages = [str]


# The function for getting a new random image for a directory
def GetRandomImage():
    #First, check for all images in directory
    UpdateImageList()
    
    #check if we've seen all images.
    if (len(seenImages) >= len(totalImages)):
        #wipes the metaImageList
        open(metaImageList, 'w+').close()
        seenImages.clear()
    
    #Get image
    while True:
        image = random.sample(totalImages, 1)
        if not (str(image[0]) in seenImages):
            # Add new image to seen images
            seenImages.append(str(image[0]))
            SaveImageMetaData()
            # Return the new image
            return image


def SaveImageMetaData():
    open(metaImageList, 'w+').close()
    
    with (open(metaImageList, 'a') as info):
        for item in seenImages:
            #writes the image directory
            newLine = ''.join([item, '\n'])
            info.write(newLine)

def UpdateImageList():
    global totalImages 
    global seenImages
    totalImages = glob.glob('*.jpg')
    
    if exists(metaImageList):
        with (open(metaImageList, 'r') as info):
            seenImages = info.read().splitlines()
    else:
        open(metaImageList, 'w+').close()
        
    VerifySeenImages()

# If images have been removed from the directory, remove them from metaImageList
def VerifySeenImages():
    for seen in seenImages:
        if not seen in totalImages:
            seenImages.remove(seen)
            

#run code
print(str(GetRandomImage()))