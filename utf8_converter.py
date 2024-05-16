# This file contains a function for converting Hebrew/English text to UTF-8 hexadecimal representation.

# Import the Hebrew and English Hexadecimal dictionaries from the constants module
from constants import utf8_heb_hex_mapping, utf8_eng_hex_mapping


def utf8_hex_representation(text):
    """
    Converts input text to its UTF-8 hexadecimal representation.
    Args:
        text (str): Input text to be converted.
    Returns:
        str: UTF-8 hexadecimal representation of the input text.
    """
    hex_representation = ''

    for char in text:
        # If the character is in the Hebrew mapping dictionary:
        if char in utf8_heb_hex_mapping:
            hex_representation += utf8_heb_hex_mapping[char]
        # If the character is in the English mapping dictionary:
        elif char in utf8_eng_hex_mapping:
            hex_representation += utf8_eng_hex_mapping[char]
        # If the character is not in either mapping dictionary, assume it is a special character
        else:
            hex_representation += char.encode('utf-8').hex()

    # Return the final UTF-8 hexadecimal representation
    return hex_representation
