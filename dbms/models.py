# -*- coding: utf-8 -*-
from rdb import db

class Intent(db.Model):
    """ Intent """

    __tablename__ = 't_intent'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    description = db.Column(db.String)
    ts = db.Column(db.Integer)
    commiter_id = db.Column(db.Integer)
    confirmed = db.Column(db.Integer)

    def __init__(self, user_id, description):
        self.user_id = user_id
        self.description = description
        self.commiter_id = 0
        self.confirmed = 0

    def __repr__(self):
        return u"<Intent id:{}, user_id: {}, desc:{}>".format(self.id, self.user_id, self.description).encode('utf-8')

class BibleVerse(db.Model):
    """ Model class for Bible quote """

    __tablename__ = "t_bible_verse"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    def __init__(self, text, address):
        self.text = text
        self.address = address

    def __repr__(self):
        return u"BibleVerse id:{}, text:{}, address:{}".format(self.id, self.text, self.address)
