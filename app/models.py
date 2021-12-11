from datetime import datetime
from app import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    uuid = db.Column(db.String(36), unique=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    # category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))

    def __init__(self, title, slug, content, uuid, created_on, updated_on, category_id):
        self.title = title
        self.slug = slug
        self.content = content
        self.uuid = uuid
        self.created_on = created_on
        self.updated_on = updated_on
        # self.category_id = category_id

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])

    def to_dict(self):
        return {
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'uuid': self.uuid,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            # 'category_id': self.category_id
        }


# class Category(db.Model):
#     __tablename__ = 'categories'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     slug = db.Column(db.String(255), nullable=False)
#     created_on = db.Column(db.DateTime(), default=datetime.utcnow)
#     posts = db.relationship('Post', backref='category')
#
#     def __repr__(self):
#         return "<{}:{}>".format(id, self.name)
#
#
# class Tag(db.Model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     slug = db.Column(db.String(255), nullable=False)
#     created_on = db.Column(db.DateTime(), default=datetime.utcnow)
#
#     def __repr__(self):
#         return "<{}:{}>".format(id, self.name)
