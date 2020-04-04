import os


class BookStoreConfig:
    MONGODB_SETTINGS = {
        'db': 'admin',
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 27017)),
        'username': os.getenv('DB_USER', ''),
        'password': os.getenv('DB_PASSWORD', ''),
        'connect': False
    }
