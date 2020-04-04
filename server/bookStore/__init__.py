from flask import Flask
from bookStore.config import BookStoreConfig

def create_app(config):
    bookStore = Flask(__name__)
    return bookStore

application = create_app(BookStoreConfig)

@application.route('/')
def index():
    return "Hello World..."