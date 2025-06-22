from flask import Flask, Response, send_from_directory, request, jsonify, flash, redirect, url_for, g, current_app, stream_with_context
from flask_cors import CORS
import json, os

from imageData import ImageData, ImageRequest
from Sources import redditSource, uploadedImage, randomNumber, sourceHandler
import frameLogic
from messageAnnouncer import MessageAnnouncer


IMAGES_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_RECENT_IMAGES = 5

recent_images = []
current_image : ImageRequest = None
announcer = MessageAnnouncer()

def create_app(config_file=None):
    #Create and configure the app.
    app = Flask(__name__, instance_relative_config=True, static_folder=STATIC_FOLDER, static_url_path='')
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        UPLOAD_FOLDER = IMAGES_FOLDER,
        SERVER_NAME = '10.0.1.114:3000'
    )

    if config_file is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(config_file)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # using flask-cors, since we are hosting both a front end svelte, 
    # and back end flask on different ports. https://github.com/corydolphin/flask-cors
    CORS(app)
    app.config['JSON_SORT_KEYS'] = False
    app.json.sort_keys = False
    return app

print('Booting Up Inky-Owl backend.')

app = create_app()
app.register_blueprint(redditSource.reddit_page, url_prefix='/reddit')
app.register_blueprint(uploadedImage.upload_page, url_prefix='/upload')
app.register_blueprint(randomNumber.random_page, url_prefix='/random')
app.register_blueprint(sourceHandler.source_page, url_prefix='/source')

@app.route("/current_image", methods=['GET'])
def get_current_image():
    # return the current image displayed on the photoframe
    return jsonify(current_image.get_metadata())

@app.route("/recent_images", methods=['GET'])
def get_recent_images():
    print("Getting recent images " + str(len(recent_images)))
    return jsonify([image.get_metadata() for image in recent_images])

@app.route("/get_new_image", methods=['GET'])
def get_new_image():
    print("Getting new image")
    newImage = sourceHandler.get_new_image()
    # frameLogic.display_image(newImage)
    
    if newImage is None:
        return jsonify({"error": "No image found"}), 500
    
    add_new_image(newImage)
    return "OK"

@app.route('/uploads/<filename>')
def download_file(filename):
    print("Getting: ", filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# SSE announcing when the current_image changes.
@app.route('/image_updates')
def current_image_stream():
    
    def stream():
        messages = announcer.listen()
        
        while True:
            message = messages.get()
            
            yield f"data: {json.dumps(message)}\n\n"
            
    return Response(stream(), mimetype="text/event-stream")


def add_new_image(image : ImageRequest):
    global current_image
    # Check if the image is already in the list
    for recentImage in recent_images:
        if recentImage.file_name == image.file_name:
            recent_images.remove(recentImage)            
            print("Image already exists in recent images., removing it and adding to front.")

    # If the list is full, remove the oldest image
    if len(recent_images) >= MAX_RECENT_IMAGES:
        recent_images.pop(0)

    # Add the new image to the list
    recent_images.append(image)
    current_image = image
    announcer.announce(current_image)
    
    print(f"Added new image: {image}")


#Register universal add new image to the app
app.add_new_image = add_new_image

#Debug default Owl
add_new_image(ImageRequest("Great_Horned_Owl_at_twilight_Mojave_Desert.jpg", "manual"))
app.run(debug=True)
