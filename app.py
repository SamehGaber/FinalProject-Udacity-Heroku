import os
from flask import Flask, request, abort, jsonify , render_template, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from models import Movie , Actor ,setup_db ,db
from auth import AuthError, requires_auth , get_token_auth_header

# app configuration # 
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__,template_folder='./templates')
  CORS(app)
  moment = Moment(app)
  setup_db(app)

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Contro-Allow-Headers','Content-Type ,Authorization')
    response.headers.add('Access-Contro-Allow-Headers','GET, POST ,PATCH , DELETE ,OPTIONS')
    response.headers.add('Access-Control-Allow-Origin' ,  'http://localhost:5000')
    return response 

  
  #redirect to login page 
  @app.route('/', methods=['GET','DELETE'])
  def index():
    return render_template('index.html')

  #login page API 
  @app.route('/login', methods=['GET','POST'])
  def login():
    return render_template("index.html")

  #login page call back API 
  @app.route('/user-page', methods=['GET','POST'])
  def user_logged():
    return render_template("logged.html")

  #list all the actors 
  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(self):
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]
    if len(formatted_actors) == 0:
        abort(404)

    return jsonify({
      'success': True ,
      'actors' : formatted_actors ,
      'total_actors' : len(formatted_actors)
    })
   
  # adding a new actor 
  @app.route('/actors', methods=['post'])
  @requires_auth('post:actors')
  def add_new_actor(self): 
    body = request.get_json()
    name= body.get('name', None)
    age= body.get('age', None)
    gender= body.get('gender', None)
    
    
    actor = Actor(name=name, age=age , gender=gender)
    actor.insert()
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    return jsonify ({
      'success': True ,
      'actors' : formatted_actors ,
      'total_actors' : len(formatted_actors) ,
      'created' : actor.id 
      })
  
  # updating  a specifc actor 
  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    if actor is None:
       abort(404)
    body = request.get_json()
    actor.name = body.get('name', actor.name)
    actor.age = body.get('age', actor.age)
    actor.gender = body.get('gender', actor.gender)
    actor.update()
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    return jsonify ({
      'success': True ,
      'actors' : formatted_actors ,
      'modified_actor' : id 
      })

  #deleting a specifc actor 
  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(id):
    selected_actor=Actor.query.get(id)
    if selected_actor is None:
      abort(404)
    selected_actor.delete()

    return jsonify ({
        'success': True ,
        'deleted' : id 
      })

  #listing all the movies 
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(self):   
    movies = Movie.query.all()
    formatted_movies = [movie.format() for movie in movies]
    if len(formatted_movies) == 0:
        abort(404)

    return jsonify({
      'success': True ,
      'movies' : formatted_movies ,
      'total_movies' : len(formatted_movies)
    })

  # adding a new movie 
  @app.route('/movies', methods=['post'])
  @requires_auth('post:movies')
  def add_new_movie(self): 
    body = request.get_json()
    title= body.get('title', None)
    release_date= body.get('release_date', None)
    actors=Actor.query.filter(Actor.id.in_(body.get('actors', None))).all()
    print(actors)
    movie = Movie(title=title, release_date=release_date )
    movie.actors = actors
    movie.insert()
    movies = Movie.query.all()
    formatted_movies = [movie.format() for movie in movies]

    return jsonify ({
      'success': True ,
      'movies' : formatted_movies ,
      'total_movies' : len(formatted_movies) ,
      'created' : movie.id 
      })
      
  #editing an exist movie 
  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(id):
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    if movie is None:
       abort(404)

    body = request.get_json()
    movie.title = body.get('title', None)
    movie.release_date = body.get('release_date', None)
    movie.actors = Actor.query.filter(Actor.id.in_(body.get('actors', None))).all()
    movie.update()
    movies = Movie.query.all()
    formatted_movies = [movie.format() for movie in movies]

    return jsonify ({
      'success': True ,
      'movies' : formatted_movies ,
      'modified_movie' : id 
      })

  # deleting a specifc movie 
  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(id):
    selected_movie=Movie.query.get(id)
    if selected_movie is None:
       abort(404)

    selected_movie.delete()

    return jsonify ({
         'success': True ,
         'deleted' : id 
       })
 

  #Error Handeling 
  @app.errorhandler(404)
  def unprocessable(error):
     return jsonify({
       "success" : False,
       "error" : 404 ,
       "message" : "resource not found "
     }) ,404

  @app.errorhandler(400)
  def bad_request(error):
     return jsonify({
       "success" : False,
       "error" : 400 ,
       "message" : "bad request "
     }) ,400

  @app.errorhandler(405)
  def method_not_found(error):
     return jsonify({
       "success" : False,
       "error" : 405 ,
       "message" : "Method not found "
     }) ,405

  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
       response = jsonify(ex.error)
       response.status_code = ex.status_code
       return response


  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)