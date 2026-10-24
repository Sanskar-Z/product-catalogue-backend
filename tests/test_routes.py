def test_read_product(client):
    response = client.get('/products/1')
    assert response.status_code == 200 and response.json['name'] == 'Eco Water Bottle'


def test_update_product(client):
    response = client.patch('/products/1', json={'price': 25.0})
    assert response.status_code == 200 and response.json['price'] == 25.0


def test_delete_product(client):
    assert client.delete('/products/1').status_code == 204
    assert client.get('/products/1').status_code == 404


def test_list_all_products(client):
    response = client.get('/products')
    assert response.status_code == 200 and len(response.json) == 3


def test_list_by_name(client):
    response = client.get('/products?name=lamp')
    assert len(response.json) == 1 and response.json[0]['name'] == 'Desk Lamp'


def test_list_by_category(client):
    response = client.get('/products?category=Outdoor')
    assert len(response.json) == 1 and response.json[0]['category'] == 'Outdoor'


def test_list_by_availability(client):
    response = client.get('/products?available=false')
    assert len(response.json) == 1 and response.json[0]['available'] is False
