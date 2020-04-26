import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Movie , Actor ,setup_db ,db

class CapestoneTestCase(unittest.TestCase):
    """This class represents the capestone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capestone_test"
        self.database_path ='postgresql://postgres:password@localhost:5432/capestone_test'
        setup_db(self.app, self.database_path)
        self.auth_header_casting_director = {'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEUTFSRFExTlRVMU0wTkdSVUpFTjBRM00wVkdSa1k0UVVZNE4wRXlOVEV3UVRJM05EVTNPQSJ9.eyJpc3MiOiJodHRwczovL3NhbWVobWFobW91ZC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDg5MDY1MTYzMzUxMzE5MzY5OTIiLCJhdWQiOlsiaHR0cDovL0NhcGVzdG9uZV9GU05EIiwiaHR0cHM6Ly9zYW1laG1haG1vdWQuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4NzkwNjM2NSwiZXhwIjoxNTg3OTEzNTY1LCJhenAiOiI0Z1VlclVyV0w3UThtVnBiS290RXNJZUpQdXlRVjQwRyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.26XNDt05c0WdBtpr4hHv1GvLgJ6tMeZfOLvdgBOlibL9HvhEMZhNUcuIYS2H4YAXqePLJnFzYFzru6El7XVZWpdNbdW0VUIVwP9qY6ucPjTXeSeuiN3v3ZpyBgTq2OnptAcq2I8NWK6nVllIu3VortrDIkOIT7p9QNGg1rlZp1PNZOixLwrL23Yosr2BWPCSZQS-mWUcaLBYBMIvN4oUzz5B478S9dbymbhIIspeD5ETV1TxwXq4Ag7unD527trVOQ0x02S-lmTpm4_Oe5obkS4ZbWyRZWC7fH2hpBEBXhVS333dZcjeFGuCppFv-JdfyjxN9xv3ofH3tJ--JR9mkg"}
        self.auth_header_Executive_director = {'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEUTFSRFExTlRVMU0wTkdSVUpFTjBRM00wVkdSa1k0UVVZNE4wRXlOVEV3UVRJM05EVTNPQSJ9.eyJpc3MiOiJodHRwczovL3NhbWVobWFobW91ZC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTA0NzIzMjA2MDIyMDExNzUwNTEiLCJhdWQiOlsiaHR0cDovL0NhcGVzdG9uZV9GU05EIiwiaHR0cHM6Ly9zYW1laG1haG1vdWQuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4NzkwNDEzNywiZXhwIjoxNTg3OTExMzM3LCJhenAiOiI0Z1VlclVyV0w3UThtVnBiS290RXNJZUpQdXlRVjQwRyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ehjGNLbm0b8EUsA5fexrRicUvG7Ye-EI4nXhVZ5q5TXRpsxGLs_y2E5fCK1kVqftOi9kwEsWPEpFF4cA7gqli86RepDC8q_bWY9f40315rjRzLPyp8XY2_yM_X1yf25mWg4B4UqrOdLPpQHXtiEoBmpKmOHM3_JO9ZWamlL7aPxsVYNGvZvCV1UFZhrfIEy-UBy60SmxgDJyApsNC2NLc-a-F7bp75LGNB4otMf9dOYEMbxwQfnTO6xjq7i_vEwMbMMElBzwVQJGd3j-oIl9LevjyrEMO7T4u3NtGUJGaRV6GhC-6kUF3p4KC5Mc3zRjY5nqRX6bfcr6QwZW-HSLGw"}
        self.auth_header_director_assistant = {'Authorization': "Bearer "}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    
   #Actors endpoints test cases  
    #testing getting all actors 
    def test_get_actors(self):
        res = self.client().get('/actors' ,headers=self.auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    #Testing adding a new actor(successful trial )
    def test_add_actor(self):
        res = self.client().post('/actors',
        json={'name': ' fake actor',
              'age': '55',
              'gender': 'fake female'
              },headers=self.auth_header_Executive_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    #test editing an actor (successful trial)
    def test_patch_actor(self):
        res = self.client().patch('actors/7',
        json={'name': 'dalia mahmoud ',
               'age': 20,
               'gender': 'female',
                },headers=self.auth_header_Executive_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #test editing an actor ( non-successful trial)
    def test_patch_actor_2(self):
        res = self.client().patch('actors/24',
        json={'name': 'sameh gaber karar ',
               'age': 44,
               'gender': 'male',
                } ,headers=self.auth_header_Executive_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found ")
 

    #testing deleting an actor (successful trial)
    def test_delete_actor(self):
        res = self.client().delete('/actors/9' ,headers=self.auth_header_Executive_director)
        data =json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    #testing deleting a actor ( non-successful trial)
    def test_delete_actor_2(self):
        res = self.client().delete('/actors/102' ,headers=self.auth_header_Executive_director)
        data =json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], "resource not found ")



   #Movies endpoints test cases  

    
    #testing getting all movies 
    def test_get_movies(self):
        res = self.client().get('/movies' ,headers=self.auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(len(data['movies']))
      
    #Testing adding a new movie 
    def test_add_movie(self):
        res = self.client().post('/movies',
        json={'title': 'too hot to handel',
              'release_date': '25nd april ',
              'actors': [7,10]
              } ,headers=self.auth_header_Executive_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(len(data['movies']))

    #test editing a movie (successful trail)
    def test_patch_movie(self):
        res = self.client().patch('movies/11',
        json={'title': 'lacasa is over ',
               'release_date': 'october ao',
               'actors': []

                } ,headers=self.auth_header_Executive_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))
    
    #test editing a movie (non-successful trial)
    def test_patch_movie_2(self):
        res = self.client().patch('movies/22',
        json={'title': 'my movie ',
               'release_date': 'a long ago',
               'actors': [4,5]

                } , headers=self.auth_header_Executive_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found ")
    
    #testing deleting a movie (successful trial )
    def test_delete_movie(self):
        res = self.client().delete('/movies/10',headers=self.auth_header_Executive_director) 
        data =json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    
    #testing deleting a movie (non-successful trial ))
    def test_delete_movie_2(self):
        res = self.client().delete('/movies/102', headers=self.auth_header_Executive_director)
        data =json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], "resource not found ")
    
    #testing deleting a movie ( RBAC test- casting director can`t delete movies from DB)
    def test_delete_movie_3(self):
        res = self.client().delete('/movies/10' , headers=self.auth_header_casting_director)
        data =json.loads(res.data)
        self.assertEqual(res.status_code,403)

    #Testing adding a new movie ( RBAC test - cating director can`t add new movies )
    def test_add_movie(self):
        res = self.client().post('/movies',
        json={'title': 'Elite',
              'release_date': '25th april ',
              'actors': [7]
              } , headers=self.auth_header_casting_director )
        data = json.loads(res.data)
        self.assertEqual(res.status_code,403)

    
    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()