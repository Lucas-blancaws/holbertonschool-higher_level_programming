#!/usr/bin/python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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


def read_sql(database):
    """Read data from SQLite database and return as list of dictionaries."""
    products = []
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        conn.close()
    except sqlite3.Error:
        return []
    return products


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source", products=[])

    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    elif source == 'sql':
        products_data = read_sql('products.db')

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
