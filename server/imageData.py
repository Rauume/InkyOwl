import datetime
import json

#Handles storing data for images displayed in the frame
class ImageData:
    
    images = []
    
    # a sub-class containing the data of idividual images.
    class FrameImage(dict):
        file_name = ""
        url = ""
        source = ""
        date_added = ""
        #Size?
        # last_accessed= ""
        
        def __init__(self, filename, source):
            self.file_name = filename
            self.source = source
            self.date_added = str(datetime.datetime.now()) #needs to be cast to string since json.dumps cant handle datetime
            self.url = ("http://10.0.1.114:3000/uploads/"+filename)
            # self.last_accessed = 'never'
            dict.__init__(self, self.get_metadata())
        
        def get_metadata(self):
            response = {
                "file_name": self.file_name,
                "source": self.source,
                "date_added": self.date_added,
                "url": self.url
                # "last_accessed": self.last_accessed
            }
            return response
    
    @staticmethod
    def get_currentimage():
        return ImageData.images[0]
    
    # @staticmethod
    # def set_currentimage(value: imageData):
    #     currentImage = ImageData["test"]
        
    @staticmethod
    def add_image(imageName, source):
        print("adding ", imageName)
        new_image = ImageData.FrameImage(imageName, source)
        ImageData.images.append(new_image)
        print("Added: ", new_image.file_name)
        return new_image
        
    @staticmethod
    def get_imagesjson():
        return json.dumps(ImageData.images)
        
if __name__ == '__main__':
    print("Hello")
    
    ImageData.add_image("20240909_150641.jpg", "manual")
    ImageData.add_image("Great_Horned_Owl_at_twilight_Mojave_Desert.jpg", "manual")
    # print(newImage.get_metadata())
    print(ImageData.get_imagesjson())