import datetime

from flask import render_template, request
from flask_restful import Resource
from app import app, api, db
from .models import Post


@app.route('/')
def home():
    return render_template('index.html')


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}


class Articles(Resource):
    def get(self, uuid=None):
        if not uuid:
            posts = db.session.query(Post).all()
            return [f.to_dict() for f in posts], 200
        post = db.session.query(Post).filter_by(uuid=uuid).first()
        if not post:
            return "", 404
        return post.to_dict(), 200

    def post(self):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            post = Post(
                title=film_json['title'],
                slug=film_json['slug'],
                content=film_json['content'],
                uuid=film_json.get('uuid'),
                created_on=datetime.datetime.strptime(film_json['created_on'], '%B %d, %Y'),
                updated_on=datetime.datetime.strptime(film_json['created_on'], '%B %d, %Y'),
                # category_id=''
            )
            db.session.add(post)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully', 'uuid': post.uuid}, 201

    def put(self, uuid):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Post).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    slug=film_json['slug'],
                    content=film_json['content'],
                    uuid=film_json.get('uuid'),
                    created_on=datetime.datetime.strptime(film_json['created_on'], '%B %d, %Y'),
                    updated_on=datetime.datetime.strptime(film_json['created_on'], '%B %d, %Y'),
                    # category_id=''
            )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 200

    def patch(self, uuid):
        film = db.session.query(Post).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        film_json = request.json
        title = film_json.get('title'),
        slug = film_json.get('slug'),
        content = film_json.get('content'),
        uuid = film_json.get('uuid'),
        created_on = datetime.datetime.strptime(film_json['created_on'], '%B %d, %Y'),
        updated_on = datetime.datetime.strptime(film_json['created_on'], '%B %d, %Y'),

        if title:
            film.title = title
        elif slug:
            film.slug = slug
        elif content:
            film.content = content
        elif uuid:
            film.uuid = uuid
        elif created_on:
            film.created_on = created_on
        elif updated_on:
            film.updated_on = updated_on

        db.session.add(film)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        post = db.session.query(Post).filter_by(uuid=uuid).first()
        if not post:
            return "", 404
        db.session.delete(post)
        db.session.commit()
        return '', 204


api.add_resource(Articles, '/articles', '/articles/<uuid>', strict_slashes=False)
api.add_resource(Smoke, '/smoke', strict_slashes=False)
