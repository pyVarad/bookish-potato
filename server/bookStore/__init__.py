from flask import Flask
from flask_restful import Api
from bookStore.extentions import db
from bookStore.config import BookStoreConfig
from bookStore.auth.routes import initialize_route


def create_app(config):
    bookStore = Flask(__name__)
    api = Api(bookStore)
    bookStore.config.from_object(config)

    db.init_app(bookStore)
    initialize_route(api)
    return bookStore


application = create_app(BookStoreConfig)
