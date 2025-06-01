from flask import Blueprint, current_app
from flask import request, flash, redirect, current_app
from werkzeug.utils import secure_filename #used to prevent uploading to protected areas of the filesystem
import os

from imageData import ImageData, ImageRequest


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
upload_page = Blueprint('upload', __name__)
currentImage = None

#todo: Notes for downloading images
# Each *source* needs a seperate download method, since they all handle gathering images differently.
# Eg. Uploading images from the frontend requtires handling the file upload request (Which by nature has no url to download an image from), 
# while the reddit source needs to handle downloading an image from a url.
# Not yet sure about how to handle immich, but thats more likely to be a simple url download.

@upload_page.route("/", methods=['POST'])
def upload_image():
    print("Setting image")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Ensure the uploads directory exists
            os.makedirs("uploads", exist_ok=True)

            #Saving
            file_path = os.path.join("server/uploads", filename)
            file.save(file_path)
            newImage = ImageRequest(filename, "upload_image")
            current_app.add_new_image(newImage)
            
            print(newImage.date_added)
            return 'OK'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS