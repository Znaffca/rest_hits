from project import db, create_app
from project.models import Artists, Hits
from faker import Faker
app = create_app('api.cfg')
with app.app_context():
    db.create_all()
    try:
        num = int(input("Ile pozycji w bazie danych chcesz dodać: "))
        count = 0
        while count < num:
            faker = Faker()
            artist = Artists(first_name=faker.first_name(), last_name=faker.last_name())
            db.session.add(artist)
            hit = Hits(title=faker.text(max_nb_chars=30), author_id=artist.id, author=artist)
            db.session.add(hit)
            count += 1
        db.session.commit()
        print("Zakończono generowanie danych!")
    except ValueError:
        print("Nieprawidłowe dane")
