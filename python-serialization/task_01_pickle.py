#!/usr/bin/python3

"""serialize"""


import pickle


class CustomObject:
    """CustomObject"""

    def __init__(self, name, is_student, age):
        """Initialize a student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serialize a Python dictionary using pickle and save it to a file
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    @classmethod
    def deserialize(cls, filename):
        """
        Load and deserialize a pickle file into a Python dictionary
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
