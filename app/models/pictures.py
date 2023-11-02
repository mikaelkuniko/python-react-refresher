from .db import db, environment, SCHEMA, add_prefix_for_prod

class User(db.Model, UserMixin):
    __tablename__ = 'pictures'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(40), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'link': self.username,

        }
