#!/usr/bin/python3
"""Convert CSV to JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON and save it as data.json
    """
    try:
        # Lire les données CSV
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Écrire les données JSON
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
