#!/usr/bin/python3
"""
Module that defines a function to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON format and writes it to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
