#!/usr/bin/python3

"""Module: Save Python object to a file as JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write object to file in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
