import pytest
from project.models import Artists, Hits
from project import create_app, db


@pytest.fixture
def create_artist():
    artist = Artists(first_name="Mark", last_name="Wahlberg")
    return artist


@pytest.fixture
def create_test_client():
    flask_app = create_app('test.cfg')
    client_test = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield client_test

    ctx.pop()


@pytest.fixture
def init_db():
    db.create_all()
    artist = create_artist
    hit = Hits(title="All you need is lol", author=artist, author_id= artist.id)
    db.session.add(artist, hit)
    db.session.commit()
    yield db

    db.drop_all()

