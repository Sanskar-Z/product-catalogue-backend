"""Reusable fake products for tests."""
from service.models import Product


def fake_product(**overrides):
    values = {
        'name': 'Eco Water Bottle', 'description': 'Reusable stainless-steel bottle',
        'price': 19.99, 'category': 'Kitchen', 'available': True,
    }
    values.update(overrides)
    return Product(**values)


def fake_products():
    return [
        fake_product(name='Eco Water Bottle', category='Kitchen', available=True),
        fake_product(name='Desk Lamp', category='Home', available=True, price=29.5),
        fake_product(name='Trail Backpack', category='Outdoor', available=False, price=49.0),
    ]
