import requests
r = requests.get('https://www.reddit.com/r/Superbowl/new/.json', headers = {'User-agent': 'owlObserver test'})

def DownloadLatestImage():
    keyval = "data"
    data = r.json()
    url = ""
    pos = -1 #seeding to start in first position
    
    #reddit automatically converts all images to jpg
    while (url.endswith(('.jpg'))== False):
        pos+= 1
        url = data[keyval]['children'][pos]['data']['url_overridden_by_dest']
        print(url)
        if pos > 10: #don't make too many attempts
            break
    
    if pos < 11:
        response = requests.get(url)
        if response.status_code == 200:
            with open("hello.jpg", 'wb') as f:
                f.write(response.content)
                
DownloadLatestImage()