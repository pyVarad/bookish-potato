from bookStore.extentions import db


class Books(db.Document):
    name = db.StringField(required=True, max_length=50)
    author = db.StringField(max_length=50)
    genere = db.StringField(max_length=30)
