from flask import Flask
import random
import json, os

print('Booting Up Inky-Owl backend.')

app = Flask(__name__, instance_relative_config =True, static_url_path='/../../client/public')

# # Path for the main svelte page
# @app.route("/")
# def base():
#     return send_from_directory('../../client/public', 'index.html')

@app.route('/')
def hello():
    return 'Hello, World!'

app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',8080)))