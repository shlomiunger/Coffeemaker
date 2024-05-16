def utf8_hex_representation(text):
    from constants import utf8_hex_mapping

    hex_representation = ''

    for char in text:
        if char in utf8_hex_mapping:
            hex_representation += utf8_hex_mapping[char]
        else:
            hex_representation += char.encode('utf-8').hex()

    return hex_representation