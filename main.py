from utf8_converter import utf8_hex_representation


def main():
    input_text = input("Enter the text: ")
    hex_representation = utf8_hex_representation(input_text)
    print(hex_representation)


# If the script is executed directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()
