CAPSTONE PROJECT
Key motivation
This projects provides an API backend for a casting application, which provides CRUD actions for movies and actors and simply manage actors assigned to movies

Getting Started
Installing Dependencies
Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the / directory and running:

pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from a potential frontend server.

Database Setup
With Postgres running, initialize the the database

createdb capestone ( for production )
createdb capestone_test  ( for unit testing )
Running the server
From within the / directory first ensure you are working using your created virtual environment.

Please also set the database URL (sample script assumes postgres runs on port 5432)

To run the server, execute:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Authentication
A script to retrieve the necessary tokens for the three roles are provided in the test_app.py file. Authentication is based on JWT Tokens with role based authentication

User Roles
Casting assistant
A casting assistang can view actors and movies

Casting director
A casting director extends the permissions of the casting assistant by adding and deleting actors from the database. He/She can also modify actors and movies

Executive director
The executive director extends the permissions of the casting director by adding or deleting movies from the database

API Endpoints
Endpoints GET '/actors'
 POST '/actors'
 PATCH '/actors/<int:id>'
 DELETE '/actors/<int:id>' 
 GET '/movies'
 POST '/movies'
 PATCH '/movies/<int:id>'
 DELETE '/movies/<int:id>'

GET '/actors'

Fetches actors from the database with name, gender and age
Request Agruments:None
Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string

{
    "actors": [
        {
            "age": 26,
            "gender": " male",
            "id": 1,
            "name": " sameh mahmoud "
        },
        {
            "age": 22,
            "gender": " female",
            "id": 2,
            "name": " dina mahmoud "
        },
        {
            "age": 27,
            "gender": " male",
            "id": 3,
            "name": " omar badran "
        },
        {
            "age": 26,
            "gender": " female",
            "id": 4,
            "name": " wesal hamam "
        },
        {
            "age": 26,
            "gender": " male",
            "id": 5,
            "name": " hashm omar "
        }
    ],
    "success": true,
    "total_actors": 5
}



Add an actor to the database
Request body parameter: JSON Object with age as an integer, gender as a string, name as a string Example payload:

{
	
"name" : " test actor5 " ,
"age" : 42 ,
"gender" : " male"

}


Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string --> Example get actors

PATCH '/actors/<int:id>'

Edit an actor in the database
Path argument: Actor id as a integer
Request body paramers: JSON Object with age as an integr, gender as a string, name as a string Example payload:

{
	
"name" : " modiefied actor " ,
"age" : 33 ,
"gender" : " female"

}



Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string --> Example get actors
Possible Errors:
404 if actor does not exist

{
    "error": 404,
    "message": "resource not found ",
    "success": false
}


DELETE '/actors/<int:id>'

delete an actor in the database
Path argument: Actor id as a integer
Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string --> Example get actors
Possible Errors:
404 if actor does not exist
{
    "error": 404,
    "message": "resource not found ",
    "success": false
}

GET '/movies'

Fetches actors from the database with title, release date and participating actors
Request Agruments:None
Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids.

{
    "movies": [
        {
            "actors": [
                1,
                2
            ],
            "id": 1,
            "release_date": "july 2008 ",
            "title": " before sun set   "
        },
        {
            "actors": [
                2
            ],
            "id": 2,
            "release_date": "july 2008 ",
            "title": " before sun rise   "
        },
        {
            "actors": [
                3
            ],
            "id": 3,
            "release_date": "july 2010 ",
            "title": " before sun midnight   "
        },
        {
            "actors": [
                4,
                5
            ],
            "id": 4,
            "release_date": "july 2012 ",
            "title": " lacasa del papel   "
        }
    ],
    "success": true,
    "total_movies": 4
}




Possible Errors:
404 if nothing is found in the database
Post '/movies/'

{
    "error": 404,
    "message": "resource not found ",
    "success": false
}

Add an movies in the database
Request body parameter: JSON Object with title as an string, release_date as a date, actors as an array of actor ids Example payload:

{
	
"title" : " test movie  " ,
"release_date" : "july 2020 ",
"actors": [4,5]


}



Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids. --> Example get movies

Patch '/movies/{movie_id}'

Edit a movie in the database
Path argument: Movie id as a integer
Request body parameter: JSON Object with title as an string, release_date as a date, actors as an array of actor ids Example payload:

{
	
"title" : " test editing movie  " ,
"release_date" : "april 2020 ",
"actors": [5]


}


Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids. --> Example get movies
Possible Errors:
404 if movie was not found in the database

{
    "error": 404,
    "message": "resource not found ",
    "success": false
}

Delete '/movies/<int:id>'

Delete a movie in the database
Path argument: Movie id as a integer
Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids. --> Example get movies
Possible Errors:
404 if movie was not found in the database
{
    "error": 404,
    "message": "resource not found ",
    "success": false
}

Defined Error handlers:

400 - Bad reqest
403 - unauthorized
404 - Resource not found
405 - Method not found

Sample Response for 404

{
  "error": 404, 
  "message": "Resource was not found", 
  "success": false
}


Script for running tests:

dropdb capestone_test
createdb capestone_test
python test_app.py

Hosting
The application is hosted by heroku under the url: 'https://udacity-final-project.herokuapp.com' 
