import sys
sys.setrecursionlimit(10000000)

def text_to_hex(text):
    hex_string = ''.join([hex(ord(c))[2:].zfill(2) for c in text])
    return hex_string

def hex_to_binary(hex_string):
    binary = bin(int(hex_string, 16))[2:]
    return binary

def binary_to_byte_code(binary_string):
    byte_code = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_code.append(int(byte, 2))
    return byte_code

colors = [
    '\033[31m',  # red
    '\033[32m',  # green
    '\033[33m',  # yellow
    '\033[34m',  # blue
    '\033[35m',  # purple
    '\033[36m',  # cyan
]

color_index = 0

while True:
    text_input = input("Enter a text string (type 'quit' to exit, type 'clear' to clear the file): ")
    if text_input.lower() == 'quit':
        break
    elif text_input.lower() == 'clear':
        with open('output.txt', 'w') as f:
            f.write("")
        print("File cleared.")
        continue

    hex_representation = text_to_hex(text_input)
    binary = hex_to_binary(hex_representation)
    byte_code = binary_to_byte_code(binary)

    with open('output.txt', 'a') as f:
        f.write("Hexadecimal representation: " + hex_representation + "\n")
        f.write("Binary representation: " + binary + "\n")
        f.write("Byte code representation: " + str(byte_code) + "\n")

    color = colors[color_index % len(colors)]
    color_index += 1

    sys.stdout.write(color + "Hexadecimal representation: " + hex_representation + "\033[0m\n")
    sys.stdout.write(color + "Binary representation: " + binary + "\033[0m\n")
    sys.stdout.write(color + "Byte code representation: " + str(byte_code) + "\033[0m\n")
