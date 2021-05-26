from flask.cli import FlaskGroup
from faker import Faker
from project import app
from project.models import db
from project.models import Artists, Hits


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("create_data")
def create_data():
    count = 0
    session = db.session()
    while count < 100:
        faker = Faker()
        artist = Artists(first_name=faker.first_name(), last_name=faker.last_name())
        db.session.add(artist)
        hit = Hits(
                title=faker.text(max_nb_chars=30), author_id=artist.id, author=artist
            )
        db.session.add(hit)
        count += 1
    session.commit()


if __name__ == "__main__":
    cli()
