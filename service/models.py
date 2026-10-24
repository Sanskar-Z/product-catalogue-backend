"""Database models for the product catalogue."""
from service import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    description = db.Column(db.String(500), nullable=False, default='')
    price = db.Column(db.Float, nullable=False, default=0.0)
    category = db.Column(db.String(80), nullable=False, default='Other', index=True)
    available = db.Column(db.Boolean, nullable=False, default=True, index=True)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'description': self.description,
            'price': self.price, 'category': self.category, 'available': self.available,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(cls.name.ilike(f'%{name}%')).all()

    @classmethod
    def find_by_category(cls, category):
        return cls.query.filter(cls.category.ilike(category)).all()

    @classmethod
    def find_by_availability(cls, available=True):
        return cls.query.filter_by(available=available).all()
