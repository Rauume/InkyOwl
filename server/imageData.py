import datetime
import json
import sqlite3
import os
from flask import current_app
import attrs

class ImageRequest(dict):
        #Thumbnail? 
        file_name = ""
        url : str = ""
        source = ""
        date_added = ""
        metadata = "" #Location, Date taken
        
        #When creating this object, it assumes the image has already been downloaded and saved to the local filesystem.
        def __init__(self, filename, source):
            print("Creating ImageRequest for: ", filename)
            self.file_name = filename            
            # self.url = f"http://{current_app.config['SERVER_NAME']}/uploads/{self.file_name}", #todo: remove the hardcoded http
            # self.url = f"http://10.0.1.114:3000/uploads/{self.file_name}", #todo: remove the hardcoded http            
            self.url = "".join(["http://10.0.1.114:3000/uploads/",self.file_name])
            self.source = source
            self.date_added = str(datetime.datetime.now()) #needs to be cast to string since json.dumps cant handle datetime
            dict.__init__(self, self.get_metadata())
        
        def get_metadata(self):
            response = {
                "file_name": self.file_name,
                "source": self.source,
                "date_added": self.date_added,
                "url": self.url
            }
            return response


#Handles storing data for images displayed in the frame
class ImageData:
    #todo: On boot, we need to clear the uploads folder, or otherwise store the data for downloaded images.
    
    MAX_RECENT_IMAGES = 5
    images : list[ImageRequest] = []
    
    @staticmethod
    def get_latestimage():
        return ImageData.images[0]
    
    @staticmethod
    def add_image(image: ImageRequest):
        ImageData.images.insert(0, image)
        print("Added: ", image.file_name)
        
        if len(ImageData.images) > ImageData.MAX_RECENT_IMAGES:
            ImageData.images.pop()
        
    @staticmethod
    def get_imagesjson():
        return json.dumps(ImageData.images)