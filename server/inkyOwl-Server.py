from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import random
import json, os

import imageData



print('Booting Up Inky-Owl backend.')
app = Flask(__name__, instance_relative_config =True, static_folder='../client/static', static_url_path='')
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


@app.route("/last_image_file", methods=['GET'])
def get_lastImageFile():
    print("Serving last shown image")
    
    return app.send_static_file('testOwl.jpg')

app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',3000)))