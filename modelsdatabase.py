"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

      id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = True) 
  playlist_id = db.Column(db.Integer,  db.ForeignKey('playlist.id'))



class Song(db.Model):
    """Song."""

   
  id = db.Column(db.Integer, primary_key = True)
  artist = db.Column(db.String(40), index = True,unique = False)
  title = db.Column(db.String(70), index = True, unique = False)
  n = db.Column(db.Integer, index = False, unique = False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    
  id = db.Column(db.Integer, primary_key = True)
  items = db.relationship('Item', backref='playlist', lazy='dynamic')


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
