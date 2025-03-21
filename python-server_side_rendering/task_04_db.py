from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sql_database(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')

        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })

        conn.close()
    except Exception as e:
        # Handle database errors silently
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
        if product_id:
            try:
                product_id = int(product_id)
                products_data = [p for p in products_data if p['id'] == product_id]
                if not products_data:
                    error = "Product not found"
            except ValueError:
                error = "Invalid ID format"
                products_data = []
    elif source == 'csv':
        products_data = read_csv_file()
        if product_id:
            try:
                product_id = int(product_id)
                products_data = [p for p in products_data if p['id'] == product_id]
                if not products_data:
                    error = "Product not found"
            except ValueError:
                error = "Invalid ID format"
                products_data = []
    elif source == 'sql':
        if product_id:
            try:
                product_id = int(product_id)
                products_data = read_sql_database(product_id)
                if not products_data:
                    error = "Product not found"
            except ValueError:
                error = "Invalid ID format"
                products_data = []
        else:
            products_data = read_sql_database()
    else:
        error = "Wrong source"

    return render_template('product_display.html', products=products_data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
