#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("JSON file does not contain a dictionary")
    return data
