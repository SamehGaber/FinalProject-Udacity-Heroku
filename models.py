#import app.py from .
#import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
#import json
from flask_migrate import Migrate
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

#database_path ='postgresql://postgres:password@localhost:5432/heroku_test2'
database_path ='postgres://qlfkgvonuvefbf:ae2b27298cfd7b5132e45794b2c5701bdcba85d50e3225fcd2de98f899daaf09@ec2-35-172-85-250.compute-1.amazonaws.com:5432/d4qlj16su5ipd4'
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config.from_object('config')
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #migrate = Migrate(app,db)
    with app.app_context():
      db.create_all()


    
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
# movie is the child and Actor is the parent 
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    release_date = db.Column(db.String(120),nullable=False)
    #actors =db.relationship("Helper_table", backref="movie")
    actors = db.relationship("Actor", secondary="helper_table",backref="movies")


    def __init__(self, title, release_date):
      self.title = title
      self.release_date = release_date

    def insert(self):
      db.session.add(self)
      db.session.commit()
  
    def update(self):
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()

    def format(self):
      return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date,
        'actors': [actor.id for actor in self.actors]
      }
   
   
class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120),nullable=False )  
    #movies = db.relationship("Helper_table", backref="actor")

    def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender
      

    def insert(self):
      db.session.add(self)
      db.session.commit()
  
    def update(self):
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()

    def format(self):
      return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender': self.gender,
      }


  


class Helper_table(db.Model):
    __tablename__ = 'helper_table'
    Actor_id = db.Column(db.Integer ,db.ForeignKey('actor.id'), primary_key=True)
    Movie_id = db.Column(db.Integer ,db.ForeignKey('movie.id'), primary_key=True)


