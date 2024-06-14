#!/usr/bin/env python3
import json
from operator import truediv
from typing import final
import requests

def DownloadLatestImage(subreddit):
    response = requests.get(''.join(['https://www.reddit.com/r/', subreddit,'/new/.json']), headers = {'User-agent': 'InkyOwl'})
    keyval = "data"
    data = response.json()
    url = ""
    pos = -1 #seeding to start in first position
    
    #reddit automatically converts all images to jpg
    urlIsValid = False
    while not (urlIsValid):
        print("Attempt {}: {}".format(pos, url))
        pos+= 1
        
        if pos > 10: #don't make too many attempts
            print("Couldn't find a suitable image")
            break
        
        # try loading the current url info.
        try:
            url = data[keyval]['children'][pos]['data']['url_overridden_by_dest'] #Errors out if the key doesnt exist. Eg. the image is a gallery.
        except:
            continue
        
        #check if it already is an image
        if not url.endswith(('.jpeg')):
            #else, try getting the first image of an album
            try:
                url = "https://i.redd.it/" + data[keyval]['children'][pos]['data']['gallery_data']['items'][0]['media_id'] + ".jpg"
            except:
                continue
        
        #Download Image
        response = requests.get(url)
        if response.status_code == 200:
            urlIsValid = True
            with open(''.join([subreddit, ".jpeg"]), 'wb') as f:
                f.write(response.content)
        
        

DownloadLatestImage('aww')