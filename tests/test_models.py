from project.models import Hits


def test_artist(create_artist):
    assert create_artist.first_name == "Mark"


def test_single_hit(create_artist):
    hit = Hits(
        title="Max Payne Returns", author_id=create_artist.id, author=create_artist
    )
    assert hit.title == "Max Payne Returns" and hit.title_url == "max-payne-returns"
