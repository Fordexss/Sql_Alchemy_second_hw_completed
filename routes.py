from flask import Flask, json
from sqlalchemy.orm import joinedload

from shop import Delivery, Session, Sale, Client, Product, ProductType

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_main():
    return "Ласкаво просимо на головну сторінку!"


@app.route('/product_types', methods=['GET'])
def get_product_types():
    try:
        with Session() as session:
            product_types = session.query(ProductType).all()
            result = [{'id': pt.id, 'name': pt.name, 'products': [p.name for p in pt.products]} for pt in product_types]
        response = app.response_class(
            response=json.dumps(result, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        print("Помилка у /product_types:", str(e))
        raise


@app.route('/products', methods=['GET'])
def get_products():
    try:
        with Session() as session:
            products = session.query(Product).options(joinedload(Product.type)).all()
            result = [{'id': p.id, 'name': p.name, 'quantity': p.quantity, 'type': p.type.name} for p in products]
        response = app.response_class(
            response=json.dumps(result, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        print("Помилка у /products:", str(e))
        raise


@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    try:
        with Session() as session:
            deliveries = session.query(Delivery).all()
            result = [{'id': d.id, 'date': d.date, 'quantity': d.quantity, 'product_id': d.product_id} for d in
                      deliveries]
        response = app.response_class(
            response=json.dumps(result, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        print("Помилка у /deliveries:", str(e))
        raise


@app.route('/sales', methods=['GET'])
def get_sales():
    try:
        with Session() as session:
            sales = session.query(Sale).all()
            result = [{'id': s.id, 'date': s.date, 'quantity': s.quantity, 'product_id': s.product_id} for s in sales]
        response = app.response_class(
            response=json.dumps(result, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        print("Помилка у /sales:", str(e))
        raise


@app.route('/clients', methods=['GET'])
def get_clients():
    try:
        with Session() as session:
            clients = session.query(Client).all()
            result = [{'id': c.id, 'name': c.name, 'email': c.email, 'products': [p.name for p in c.products]} for c in
                      clients]
        response = app.response_class(
            response=json.dumps(result, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        print("Помилка у /clients:", str(e))
        raise

