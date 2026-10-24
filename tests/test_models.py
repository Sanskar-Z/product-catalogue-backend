from service import db
from service.models import Product


def test_read_product(app):
    with app.app_context():
        product = Product.query.filter_by(name='Eco Water Bottle').first()
        assert product is not None and product.price == 19.99


def test_update_product(app):
    with app.app_context():
        product = Product.query.filter_by(name='Eco Water Bottle').first()
        product.price = 22.0; db.session.commit()
        assert db.session.get(Product, product.id).price == 22.0


def test_delete_product(app):
    with app.app_context():
        product = Product.query.filter_by(name='Eco Water Bottle').first()
        product_id = product.id; db.session.delete(product); db.session.commit()
        assert db.session.get(Product, product_id) is None


def test_list_all_products(app):
    with app.app_context():
        assert Product.query.count() == 3


def test_find_by_name(app):
    with app.app_context():
        assert [p.name for p in Product.find_by_name('bottle')] == ['Eco Water Bottle']


def test_find_by_category(app):
    with app.app_context():
        assert len(Product.find_by_category('Kitchen')) == 1


def test_find_by_availability(app):
    with app.app_context():
        assert len(Product.find_by_availability(False)) == 1
