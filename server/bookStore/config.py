import os
import pyrebase

class BookStoreConfig:
    MONGODB_SETTINGS = {
        'db': 'admin',
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 27017)),
        'username': os.getenv('DB_USER', ''),
        'password': os.getenv('DB_PASSWORD', ''),
        'connect': False
    }
    FIREBASE_CONFIG = {
        'apiKey': os.getenv('FIREBASE_APIKEY'),
        'authDomain': os.getenv('FIREBASE_APP_DOMAIN'),
        'databaseURL': os.getenv('FIREBASE_DB_URL'),
        'projectId': os.getenv('FIREBASE_PROJECTID'),
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.getenv('FIREBASE_MSG_SENDER_ID'),
        'appId': os.getenv('FIREBASE_APP_ID'),
        'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
    }
    firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
    auth = firebase.auth()
    SECRET_KEY = os.urandom(12).hex()
    JWT_SECRET_KEY = os.urandom(12).hex()
