# This file contains mappings of Hebrew/English characters and their corresponding UTF-8 hexadecimal representations.

# Mapping for Hebrew characters
utf8_heb_hex_mapping = {
    'א': 'd790', 'ב': 'd791', 'ג': 'd792', 'ד': 'd793', 'ה': 'd794', 'ו': 'd795', 'ז': 'd796', 'ח': 'd797',
    'ט': 'd798', 'י': 'd799', 'ך': 'd79a', 'כ': 'd79b', 'ל': 'd79c', 'ם': 'd79d', 'מ': 'd79e', 'ן': 'd79f',
    'נ': 'd7a0', 'ס': 'd7a1', 'ע': 'd7a2', 'ף': 'd7a3', 'פ': 'd7a4', 'ץ': 'd7a5', 'צ': 'd7a6', 'ק': 'd7a7',
    'ר': 'd7a8', 'ש': 'd7a9', 'ת': 'd7aa'
}

# Mapping for English characters
utf8_eng_hex_mapping = {}
# During import, the loops below will execute and populate the utf8_eng_hex_mapping dictionary
# with the hexadecimal values for uppercase and lowercase English letters.
for i in range(26):
    utf8_eng_hex_mapping[chr(65 + i)] = hex(65 + i)[2:]
    utf8_eng_hex_mapping[chr(97 + i)] = hex(97 + i)[2:]
