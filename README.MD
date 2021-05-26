# RESTHits

The idea of this application is to create a sample Flask-Based API for music radio hits with full support for CRUD methods.

## Basic technologies

* Python 3.6 / 3.7 
* Black code formatter
* Unit and functional test written in pytest
* Flask 1.0 with SQLAlchemy
* Flask-Marshmallow for json convert responses to JSON format
* Basic SQLite database
* Support for Docker containers
* Use sample random data generator (Faker)

### To-Do-List (Update 26.05.2021)

- [x] limit all hits to display in ```/api/v1/hits```, and sort all positions by creation date
- [ ] write functional test for API URL's
- [x] dockerize the app
- [x] - add post and put method to add and edit artists:
    - [x] ```/api/v1/artists``` - for POST
    - [x] ```/api/v1/artists/<id>``` for GET, PUT and DELETE

#### Available url's

1. [GET] ``` /api/v1/hits ``` - for list of all songs in database

2. [POST] ` api/v1/hits ` - for add hit to database

3. [GET] ``` /api/v1/hits/<title_url> ``` - for detail hit

4. [PUT] ``` /api/v1/hits/<title_url> ``` - for update specified hit

5. [DELETE] ``` /api/v1/hits/<title_url> ``` - for delete specified hit

6. [GET] ``` /api/v1/artists ``` - for list of all artists in database

7. [POST] ``` /api/v1/artists ``` - for add a new artist to database

8. [PUT] ``` /api/v1/hits/<title_url> ``` - for update specified artist

9. [DELETE] ``` /api/v1/hits/<title_url> ``` - for delete specified artist


## RUN APP
Application is currently dockerized , so the running it is pretty straightforward.

1. Clone repository on your computer
2. Navigate to the project root and create the following environmnet files:
    - `.env` - for storing application variables; feel free to copy example below:
        ```bash
            # flask app settings
            FLASK_APP=project/__init__.py
            FLASK_ENV=development
            SECRET_KEY=dev
            # flask app database settings
            DATABASE_URL=postgresql://hits_api_user:hits_api_password@db:5432/rest_hits
            DATABASE=postgres
            SQL_HOST=db
            SQL_PORT=5432 
        ```
    - `env.db` - for storing postgres container database; feel free to copy the example below:
        ```bash
            # envs required for postgres db configuration
            POSTGRES_USER=hits_api_user
            POSTGRES_PASSWORD=hits_api_password
            POSTGRES_DB=rest_hits
        ```
3. Execute command:
    ```bash
        # for build and start environmnent
        docker-compose up -d --build
        # for stop and remove the enviromnent
        docker-compose down -v # -v removes stored volumes as well
    ```