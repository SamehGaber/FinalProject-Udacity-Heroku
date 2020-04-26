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

Executive Producer
The executive producer extends the permissions of the casting director by adding or deleting movies from the database

API Endpoints
Endpoints GET '/actors' POST '/actors' PATCH '/actors/{actor_id}' DELETE '/actors/{actor_id}' GET '/movies' POST '/movies' PATCH '/movies/{movie_id}' DELETE '/movies/{movie_id}'

GET '/actors'

Fetches actors from the database with name, gender and age
Request Agruments:None
Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string










Add an actor to the database
Request body parameter: JSON Object with age as an integer, gender as a string, name as a string Example payload:




Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string --> Example get actors
Possible Errors:
422 if invalid object is submitted
PATCH '/actors/{actor_id}'

Edit an actor in the database
Path argument: Actor id as a integer
Request body paramers: JSON Object with age as an integr, gender as a string, name as a string Example payload:





Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string --> Example get actors
Possible Errors:
404 if actor does not exist
422 if invalid actor was submitted
DELETE '/actors/{actor_id}'

delete an actor in the database
Path argument: Actor id as a integer
Returns: An object with a list of actors with id as an integer, name as a string, age as an integer, gender as a string --> Example get actors
Possible Errors:
404 if actor does not exist
422 if deletion wasn't possible
GET '/movies'

Fetches actors from the database with title, release date and participating actors
Request Agruments:None
Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids.








Possible Errors:
404 if nothing is found in the database
Post '/movies/'

Add an movies in the database
Request body parameter: JSON Object with title as an string, release_date as a date, actors as an array of actor ids Example payload:





Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids. --> Example get movies
Possible Errors:
422 if invalid movie is submitted
Patch '/movies/{movie_id}'

Edit a movie in the database
Path argument: Movie id as a integer
Request body parameter: JSON Object with title as an string, release_date as a date, actors as an array of actor ids Example payload:





Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids. --> Example get movies
Possible Errors:
404 if movie was not found in the database
422 if invalid object is submitted
Delete '/movies/{movie_id}'

Delete a movie in the database
Path argument: Movie id as a integer
Returns: An object with a list of movie with title as a string, release date as a date and actors as an array of actor ids. --> Example get movies
Possible Errors:
404 if movie was not found in the database
422 if movie could not be deleted
Defined Error handlers:

400 - Bad reqest
401 - token expired / invalid claims / invalid header
403 - unauthorized
404 - Resource not found
405 - Method not found
422 - Unprocessable entity
500 - Internal Server error
Sample Response for 404

{
  "error": 404, 
  "message": "Resource was not found", 
  "success": false
}
Running tests
Tests are prefixed with numbers to sort their test execution

Script for running tests:

dropdb capestone_test
createdb capestone_test
python test_app.py
Hosting
The application is hosted by heroku under the url: 'heroku app' In the test_app.py you can find a convenient script to get the need access token.
