"""REST endpoints for product CRUD and searches."""
from flask import Blueprint, jsonify, request, abort
from service import db
from service.models import Product

bp = Blueprint('products', __name__)


def _payload():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        abort(400, description='A JSON object is required')
    return data


@bp.get('/health')
def health():
    return {'status': 'ok'}


@bp.post('/products')
def create_product():
    data = _payload()
    if not data.get('name'):
        abort(400, description='name is required')
    product = Product(name=data['name'], description=data.get('description', ''),
                      price=float(data.get('price', 0)), category=data.get('category', 'Other'),
                      available=bool(data.get('available', True)))
    db.session.add(product); db.session.commit()
    return jsonify(product.to_dict()), 201


@bp.get('/products')
def list_products():
    if 'name' in request.args:
        products = Product.find_by_name(request.args['name'])
    elif 'category' in request.args:
        products = Product.find_by_category(request.args['category'])
    elif 'available' in request.args:
        value = request.args['available'].lower()
        if value not in ('true', 'false', '1', '0'):
            abort(400, description='available must be true or false')
        products = Product.find_by_availability(value in ('true', '1'))
    else:
        products = Product.query.order_by(Product.id).all()
    return jsonify([p.to_dict() for p in products])


@bp.get('/products/<int:product_id>')
def read_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None: abort(404, description='Product not found')
    return jsonify(product.to_dict())


@bp.patch('/products/<int:product_id>')
@bp.put('/products/<int:product_id>')
def update_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None: abort(404, description='Product not found')
    data = _payload()
    for field in ('name', 'description', 'category', 'available'):
        if field in data: setattr(product, field, data[field])
    if 'price' in data: product.price = float(data['price'])
    db.session.commit()
    return jsonify(product.to_dict())


@bp.delete('/products/<int:product_id>')
def delete_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None: abort(404, description='Product not found')
    db.session.delete(product); db.session.commit()
    return '', 204
