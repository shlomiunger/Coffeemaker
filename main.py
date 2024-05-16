from utf8_converter import utf8_hex_representation

def main():
    input_text = input("Enter the text: ")
    hex_representation = utf8_hex_representation(input_text)
    print("UTF-8 Hexadecimal Representation:", hex_representation)

if __name__ == "__main__":
    main()