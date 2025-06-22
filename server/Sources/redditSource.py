from flask import Blueprint, render_template, abort, send_file, jsonify, request
import random

import DownloadOwl
from imageData import ImageRequest

reddit_page = Blueprint('reddit', __name__)

#todo: load the subreddits from a config file
#todo: Verify subreddits exist when added.

subreddits = [    
    {"name": "aww", "active": True},
    {"name": "superbowl", "active": True},
    {"name": "catloaf", "active": False},
]

def get_subreddit_new(subreddit):
    print("Getting: r/", subreddit)
    filename = DownloadOwl.DownloadLatestImage(subreddit)
    
    if filename is None:
        print("No image found for subreddit:", subreddit)
        abort(404)
    
    imageRequest = ImageRequest(filename, f"Reddit: r/{subreddit}")
    
    return imageRequest

def get_new():
    print("Getting Random Image")
    return get_subreddit_new(subreddits[random.randint(0, len(subreddits) - 1)]["name"])

@reddit_page.route("/get")
def get_subreddit_list():
    return jsonify(subreddits), 200

@reddit_page.route("/set", methods=['POST'])
def set_subreddit_list():
    global subreddits
    if request.method == 'POST':
        data : str = request.get_json()        
        subreddits = data
        print(subreddits)    
    return 'OK'