# RESTHits

Projekt polega na utworzeniu prostej aplikacji REST udostępniającej na zadanych url listy hitów radia ESKA.

## Informacje wstępne

* Python 3.6 / 3.7 
* Black (formatowanie i lint kodu)
* Pytest z requests bądź unittest + nose do testów
* Flask 1.0 wraz z SQLAlchemy
* Baza danych PostgreSQL w wersji 9.5+ bądź SQLite
* Docker
* Dozwolone jest używanie zewnętrznych bibliotek


## Wymagania techniczne

Aplikacja wystawia poniżej podane url (w nawiasach zostały podane metody wywołania):

[GET] `/api/v1/hits` (wyświetla listę 20 hitów sortowanych po dacie dodania)

Przykładowa odpowiedź:

```
[
    {
        id: <hitId>,
        title: <title>,
        titleUrl: <titleUrl>
    },
    {
        id: <hitId>,
        title: <title>,
        titleUrl: <titleUrl>
    }
]
```

[GET] `/api/v1/hits/{title_url}` (wyświetla szczegóły pojedynczego hitu)

Przykładowa odpowiedź:

```
{
    id: <hitId>,
    title: <title>,
    titleUrl: <titleUrl>,
    createdAd: <createdAd>,
    artist: {
        id: <artistId>,
        firstName: <firstName>
        lastName: <lastName>
    }
}
```

[POST] `/api/v1/hits` (tworzy nowy hit na podstawie przekazanego obiektu: `artistId`, `title`. Pola `created_at`/`title_url` tworzą się automatycznie)
[PUT] `/api/v1/hits/{title_url}` (aktualizuje wybrany hit, można zaktualizować tylko: `artistId`, `title` oraz `titleUrl`, dodatkowo aktualizacja wypełnia pole `updated_at`)
[DELETE] `/api/v1/hits/{name-url}` (usuwa wybrany hit)


Aplikacja posiada dwie tablice:
- tablica hits (id, artist_id jako klucz obcy, title, title_url, created_at, updated_at)
- tablica artists (id, first_name, last_name, created_at)

Aplikacja powinna posiadać komendę, dzięki której wygeneruje przykładowych artystów i hity do bazy danych. 

Na co zwracać uwagę:
- lint i format kodu powinien zostać zrealizowany za pomocą narzędzia Black (https://github.com/ambv/black)
- aplikacja powinna posiadać podstawowe testy jednostkowe oraz integracyjne (odwiedzające dany adres url jak przeglądarka) zrealizowane za pomocą PyTest bądź unittest & nose  
- każda odpowiedź serwera musi mieć poprawny response code:
    - przy utworzeniu hitu zwracamy 201
    - przy odczycie 200, 204 (no-content) bądź 404
    - w przypadku błędu serwera dostajemy kod 500
    - w przypadku źle wysłanego formularza dostajemy kod 400 (np. wysłaliśmy niepełny obiekt do stworzenia)
- aplikacja powinna mieć Dockerfile umożliwiający zbudowanie jej i uruchomienie z poziomu Dockera 
- kod powinien posiadać README.md z prostą instrukcją umożwiającą uruchomienie aplikacji
- kod powinien zostać stworzony zgodnie z dobrymi praktykami

## Przydatne linki

1. https://httpstatuses.com/
2. https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
3. https://damyanon.net/post/flask-series-testing/

Plusem będzie zastosowanie Static Typings z pythona 3.6+ (https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b)
W razie pytań, proszę o kontakt.