#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(file):
    """Read JSON file and return data."""
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv(file):
    """Read CSV file and return data as list of dictionaries."""
    products = []
    try:
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row = {k.strip(): v.strip() for k, v in row.items()}
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except (FileNotFoundError, KeyError, ValueError):
        return []
    return products


@app.route('/products')
def products():
    """Display products from JSON or CSV based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=[])

    products_data = read_json('products.json') if source == 'json' else read_csv('products.csv')

    if product_id:
        try:
            product_id = int(product_id)
            products_data = [p for p in products_data if p['id'] == product_id]
            if not products_data:
                return render_template('product_display.html', error="Product not found", products=[])
        except ValueError:
            return render_template('product_display.html', error="Invalid product id", products=[])
    
    return render_template('product_display.html', products=products_data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)