from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        return []

def read_csv_file():
    products = []
    try:
        with open('products.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '')
    product_id = request.args.get('id')

    error = None
    products_data = []

    if source == 'json':
        products_data = read_json_file()
    elif source == 'csv':
        products_data = read_csv_file()
    else:
        error = "Wrong source"

    # Filter by id if provided
    if product_id and not error:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p['id'] == product_id]
            if filtered_products:
                products_data = filtered_products
            else:
                error = "Product not found"
                products_data = []
        except ValueError:
            error = "Invalid ID format"
            products_data = []

    return render_template('product_display.html', products=products_data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
