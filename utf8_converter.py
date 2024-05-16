# This file contains a function for converting text to UTF-8 hexadecimal representation.

from constants import utf8_hex_mapping

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
        if char in utf8_hex_mapping:
            hex_representation += utf8_hex_mapping[char]
        else:
            hex_representation += char.encode('utf-8').hex()

    return hex_representation
