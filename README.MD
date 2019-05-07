# RESTHits

The idea of this application is to create a sample Flask-Based API for music radio hits with full support for CRUD methods.

##Basic technologies

* Python 3.6 / 3.7 
* Black code formatter
* Unit and functional test written in pytest
* Flask 1.0 with SQLAlchemy
* Flask-Marshmallow for json convert responses to JSON format
* Basic SQLite database
* Support for Docker containers
* Use sample random data generator (Faker)

### To-Do-List (Update 07.05.2019)

- limit all hits to display in ```/api/v1/hits```, and sort all positions by creation date
- write functional test for API URL's
- dockerize the app
- [POST] - ```/api/v1/artists``` - for edit artists

#### Available url's

1. [GET] ``` /api/v1/hits ``` - for list of all songs in database

2. [POST] ` api/v1/hits ` - for add hit to database

3. [GET] ``` /api/v1/hits/<title_url> ``` - for detail hit

4. [PUT] ``` /api/v1/hits/<title_url> ``` - for update specified hit

5. [DELETE] ``` /api/v1/hits/<title_url> ``` - for delete specified hit

6. [GET] ``` /api/v1/artists ``` - for list of all artists in database


## RUN APP

1. Clone repository on your PC.
2. Create new virtualenv and install requirements by ```pip install -r requirements.txt```
3. In app top-level directory run ```python init_db.py``` for generate random data to database
4. Run ```export FLASK_APP=rest_hits.py```, and next ``` flask run ```
