from flask import Flask
from flask_restful import Api
from bookStore.config import BookStoreConfig
from bookStore.auth.routes import initialize_route


def create_app(config):
    bookStore = Flask(__name__)
    api = Api(bookStore)
    initialize_route(api)
    return bookStore


application = create_app(BookStoreConfig)
