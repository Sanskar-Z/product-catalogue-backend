import pytest
from service import create_app, db
from tests.factories import fake_products


@pytest.fixture()
def app():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.app_context():
        db.drop_all(); db.create_all()
        db.session.add_all(fake_products()); db.session.commit()
        yield app
        db.session.remove(); db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
