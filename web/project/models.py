from datetime import datetime
from slugify import slugify
from sqlalchemy import event
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Hits(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    title_url = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    author_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artists", backref="singer")

    def __repr__(self):
        return f"{self.title}"

    def __init__(self, title, author_id, author):
        self.title = title
        self.author_id = author_id
        self.artist = author
        pass

    @staticmethod
    def urlify(target, val, oldval, initiator):
        if val and (not target.title_url or val != oldval):
            target.title_url = slugify(val)


event.listen(Hits.title, "set", Hits.urlify, retval=False)


class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    hit = db.relationship("Hits", backref="author")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class HitsSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "title_url", "created_at", "artist")
        ordered = True

    artist = fields.Nested("ArtistSchema")


class AllHitsSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "title_url")
        ordered = True


class ArtistSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name")
        ordered = True
