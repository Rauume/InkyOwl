from asyncio.windows_events import NULL
import os
import shutil
import glob
import random

    
imagesDirectory = "C:/Users/cam/Desktop/New folder/Project/Images/"
metaImageList = ''.join([imagesDirectory, "ImagesMetaInfo.txt"])

totalImages = glob.glob('*.jpg')

images = [str]
seenImages = [str]

def GetRandomImage():
    #if we've seen all images, wipe file
    if (len(seenImages) >= len(totalImages)):
        #wipes the metaImageList
        open(metaImageList, 'w').close()
        seenImages.clear()
        SaveImageMetaData()
        
    
    #Get image
    while True:
        image = random.sample(totalImages, 1)
        if not (image in seenImages): 
            return image


def SaveImageMetaData():
    with (open(metaImageList, 'w') as info):
        for item in images:
            
            #inserts the split string
            if (item in seenImages[0]):
                info.write("Seen:")
            
            #writes the image directory
            info.write(str(item[1]))

def UpdateImageList():
    totalImages = glob.glob('*.jpg')
    
    # #clear non-existent images
    # with (open(metaImageList, 'w') as info):
    #     for item in images:
    #         if not (item in info.read):
    #             images.remove(item)
        
    
    # #update images Array
    # if (files > images):
    #     images = files
        
    SaveImageMetaData()

#run code

print ("Hello")
    
    #Get all images' references
# with (open(metaImageList, 'w') as info):
#     images = info.readlines()
#     seenImages = info.read().split("Seen:")
    
UpdateImageList()
    
print(str(GetRandomImage()))