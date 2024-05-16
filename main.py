from utf8_converter import utf8_hex_representation


def main():
    input_text = input("Enter the text: ")
    hex_representation = utf8_hex_representation(input_text)
    print(f"\n{hex_representation}")

    num_bytes = len(hex_representation) // 2
    if num_bytes > 80:
        num_bytes_over_limit = num_bytes - 80
        print(f"\n{num_bytes} bytes - You are {num_bytes_over_limit} bytes over the OP_RETURN limit")


# If the script is executed directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()
