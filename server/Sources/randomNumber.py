from flask import Blueprint
import random

random_page = Blueprint('random', __name__)

@random_page.route('/')
def index():
    print("Getting Random Number")
    randomNumber = random.randint(0, 100)

    response = {
        "randomNumber": str(randomNumber), 
        "otherRandomVariable": "Hello"
    }
    
    return response