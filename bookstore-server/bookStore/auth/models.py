from bookStore.extentions import db


class Users(db.Document):
    id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True, max_length=50)
    email = db.EmailField()
