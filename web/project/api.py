from flask import request, jsonify, Blueprint
from sqlalchemy import desc
from .models import (
    HitsSchema,
    AllHitsSchema,
    ArtistSchema,
    ArtistDetailSchema,
    Hits,
    Artists,
    db,
)


hit_schema = HitsSchema()
hits_schema = AllHitsSchema(many=True)
artist_schema = ArtistDetailSchema()
artists_schema = ArtistSchema(many=True)


api_bp = Blueprint("api", __name__)


@api_bp.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "405", "message": "Method not allowed"}), 405


@api_bp.errorhandler(404)
def not_found(e):
    return jsonify({"error": "404", "message": "Not found"}), 404


@api_bp.route("/api/v1/hits", methods=["GET", "POST"])
def hits():
    if request.method == "GET":
        hit_list = Hits.query.order_by(desc(Hits.created_at))
        result = hits_schema.dump(hit_list)
        return jsonify(result), 200
    elif request.method == "POST":
        title = request.json["title"]
        artist_id = request.json["artist_id"]
        new_hit = Hits(
            title=title, author_id=artist_id, author=Artists.query.get(artist_id)
        )
        db.session.add(new_hit)
        db.session.commit()
        return hit_schema.jsonify(new_hit), 201


@api_bp.route("/api/v1/hits/<title_url>", methods=["GET", "PUT", "DELETE"])
def single_hit(title_url):
    hit = Hits.query.filter_by(title_url=title_url).first_or_404()
    if request.method == "GET":
        return hit_schema.jsonify(hit), 200

    elif request.method == "PUT":
        hit.title = request.json["title"]
        hit.author_id = request.json["artist_id"]
        db.session.commit()
        return hit_schema.jsonify(hit), 201

    elif request.method == "DELETE":
        db.session.delete(hit)
        db.session.commit()
        return jsonify({"Message": f"{hit.title} succesfully deleted"}), 200


@api_bp.route("/api/v1/artists", methods=["GET", "POST"])
def artists():
    if request.method == "GET":
        artists = Artists.query.all()
        return jsonify(artists_schema.dump(artists)), 200
    elif request.method == "POST":
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        new_artist = Artists(first_name=first_name, last_name=last_name)
        db.session.add(new_artist)
        db.session.commit()
        return artist_schema.jsonify(new_artist), 200


@api_bp.route("/api/v1/artists/<id>", methods=["GET", "PUT", "DELETE"])
def get_artist(id):
    artist = Artists.query.get_or_404(id)
    if request.method == "GET":
        return artist_schema.jsonify(artist), 200
    elif request.method == "PUT":
        artist.first_name = request.json["first_name"]
        artist.last_name = request.json["last_name"]
        db.session.commit()
        return artist_schema.jsonify(artist), 201
    elif request.method == "DELETE":
        db.session.delete(artist)
        db.session.commit()
        return (
            jsonify(
                {
                    "Message": f"{artist.first_name} {artist.last_name} with id {artist.id} succesfully deleted"
                }
            ),
            200,
        )
