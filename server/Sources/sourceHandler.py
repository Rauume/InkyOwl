from flask import Flask, jsonify, request, Blueprint, current_app
import random
from collections import namedtuple

from Sources import redditSource, uploadedImage, randomNumber

source_page = Blueprint('sources', __name__)

sources = [
    {"name": "Reddit", "active": True},
    {"name": "Uploaded Images", "active": False},
    {"name": "Immich", "active": True},
]

def get_new_image():
    # Select a random image source
    active_sources = filter(lambda s: s["active"] == True, sources)
    selected_source = random.choice(list(active_sources))
    # newSelected = list(active_sources)
    
    print(f"Selected source: {selected_source['name']}")
    
    match selected_source["name"]:
        case "Reddit":
            return redditSource.get_new()
        case "Immich":
            print("Immich source not implemented yet")
            return None
        case _:
            raise ValueError("Unknown source")
        
    return None

@source_page.route("/get", methods=['GET'])
def get_sources():
    return jsonify(sources), 200

@source_page.route("/set", methods=['POST'])
def set_sources():
    if request.method == 'POST':
        
        data : str = request.get_json()
            
        for source in sources:
            if source["name"] == data['name']: #If source is in list
                source["active"] = bool(data['active']) #set the active state
                
                print(f"Set {source['name']} to {source['active']}")
                return "OK"
        
        return jsonify({"error": "Source not found"}), 404