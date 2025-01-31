from flask import Flask, send_from_directory, request, jsonify, flash, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename #used to prevent uploading to protected areas of the filesystem
import random
import json, os

from imageData import ImageData

# IMAGES_FOLDER = '../client/static'
IMAGES_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


print('Booting Up Inky-Owl backend.')
app = Flask(__name__, instance_relative_config =False, static_folder=STATIC_FOLDER, static_url_path='')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
# using flask-cors, since we are hosting both a front end svelte, 
# and back end flask on different ports. https://github.com/corydolphin/flask-cors
CORS(app) 

@app.route("/api/rand", methods=['GET'])
def get_rand():
    
    print("Getting Random Number")
    randomNumber = random.randint(0, 100)

    response = {
        "randomNumber": str(randomNumber), 
        "otherRandomVariable": "Hello"
    }
    
    return response

@app.route("/api/last_image", methods=['GET'])
def get_lastImage():
    print("Serving last shown image")
    # show the current image displayed on the photoframe    
    return ImageData.get_lastimage()

@app.route("/last_image_file", methods=['GET'])
def get_lastImageFile():
    print("Serving last shown image")
    filenames = next(walk(app.config['UPLOAD_FOLDER']), (None, None, []))[2]  # [] if no file
    print(filenames)
    
    return app.send_static_file('testOwl.jpg')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/api/upload_image", methods=['POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            addedImage = ImageData.add_image(filename, "upload_image")
            print(addedImage.date_added)
            return 'OK'
        
@app.route('/uploads/<filename>')
def download_file(filename):
    print("Getting: ", filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/api/set_image", methods=['GET'])
def set_image(imageName):
    #inkDisplay.DisplayImage(imageName)
    print("Updating frame.")
    
@app.route("/api/recent_images", methods=['GET'])
def recent_images():
    print("Returning recent images")
    return ImageData.get_imagesjson()
    


#Debug, remove later
# ImageData.add_image("20240909_150641.jpg", "manual")
ImageData.add_image("Great_Horned_Owl_at_twilight_Mojave_Desert.jpg", "manual")


app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',3000)))