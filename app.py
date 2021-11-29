from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    genre = db.Column(db.String, nullable=False)
    mpaa_rating = db.Column(db.String)
    poster_img = db.Column(db.String, unique=True)

    def __init__(self, title, genre, mpaa_rating, poster_img):
        self.title = title
        self.genre = genre
        self.mpaa_rating = mpaa_rating
        self.poster_img = poster_img

class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'genre', 'mpaa_rating', 'poster_img')

movie_schema = MovieSchema()
multi_movie_schema = MovieSchema(many=True)













if __name__ == "__main__":
    app.run(debug = True)