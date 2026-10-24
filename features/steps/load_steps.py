"""Behave steps to load BDD background product data."""
from service import create_app, db
from service.models import Product


def before_scenario(context, scenario):
    context.app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    context.app_context = context.app.app_context()
    context.app_context.push()
    db.drop_all(); db.create_all()


@given('the following products')
def load_products(context):
    for row in context.table:
        product = Product(
            name=row['name'], description=row['description'], price=float(row['price']),
            category=row['category'], available=row['available'].lower() == 'true')
        db.session.add(product)
    db.session.commit()
