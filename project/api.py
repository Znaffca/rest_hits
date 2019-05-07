from flask import request, jsonify, Blueprint
from sqlalchemy import desc
from project.models import HitsSchema, AllHitsSchema, ArtistSchema, Hits, Artists, db

hit_schema = HitsSchema()
hits_schema = AllHitsSchema(many=True)
artist_schema = ArtistSchema(many=True)

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
        hit_list = Hits.query.order_by(desc(Hits.created_at)).limit(20)
        result = hits_schema.dump(hit_list)
        return jsonify(result.data), 200
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


@api_bp.route("/api/v1/artists", methods=["GET"])
def get_artist():
    artists = Artists.query.all()
    return jsonify(artist_schema.dump(artists).data), 200
