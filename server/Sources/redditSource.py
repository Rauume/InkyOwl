from flask import Blueprint, render_template, abort, send_file
import random

import DownloadOwl
from imageData import ImageRequest

reddit_page = Blueprint('reddit', __name__)

#todo: load the subreddits from a config file
subreddits = [
    "aww",
    "superbowl",
    "space"
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
    return get_subreddit_new(subreddits[random.randint(0, len(subreddits) - 1)])