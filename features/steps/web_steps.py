"""Behave step definitions for product catalogue operations."""
import json
from behave import given, when, then


@when('I read the product named "{name}"')
def read_product(context, name):
    product = next((p for p in __import__('service.models', fromlist=['Product']).Product.query.all() if p.name == name), None)
    context.response_text = json.dumps(product.to_dict() if product else {})


@when('I update the product "{name}" price to {price:f}')
def update_product(context, name, price):
    from service.models import Product
    product = Product.query.filter_by(name=name).first()
    if product:
        product.price = price
        from service import db
        db.session.commit()
    context.response_text = json.dumps(product.to_dict() if product else {})


@when('I delete the product named "{name}"')
def delete_product(context, name):
    from service import db
    from service.models import Product
    product = Product.query.filter_by(name=name).first()
    if product: db.session.delete(product); db.session.commit()
    context.response_text = json.dumps([p.to_dict() for p in Product.query.all()])


@when('I list all products')
def list_products(context):
    from service.models import Product
    context.response_text = json.dumps([p.to_dict() for p in Product.query.all()])


@when('I search products by category "{category}"')
def search_category(context, category):
    from service.models import Product
    context.response_text = json.dumps([p.to_dict() for p in Product.find_by_category(category)])


@when('I search products by availability "{available}"')
def search_availability(context, available):
    from service.models import Product
    context.response_text = json.dumps([p.to_dict() for p in Product.find_by_availability(available.lower() == 'true')])


@when('I search products by name "{name}"')
def search_name(context, name):
    from service.models import Product
    context.response_text = json.dumps([p.to_dict() for p in Product.find_by_name(name)])


@then('the response should contain "{text}"')
def response_contains(context, text):
    assert text.lower() in context.response_text.lower(), f'{text!r} not found in {context.response_text}'


@then('the response should not contain "{text}"')
def response_not_contains(context, text):
    assert text.lower() not in context.response_text.lower(), f'{text!r} unexpectedly found in {context.response_text}'


@then('the message "{message}" should be present')
def message_present(context, message):
    assert message in context.response_text
