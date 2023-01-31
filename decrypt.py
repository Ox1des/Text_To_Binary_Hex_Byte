def binary_to_text(binary):
    text = ""
    binary = binary.zfill(8 * ((len(binary) + 7) // 8))
    binary_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    for byte in binary_list:
        text += chr(int(byte, 2))
    return text

while True:
    binary = input("Enter a binary string: ")
    result = binary_to_text(binary)
    print(result)
    again = input("Would you like to enter another binary string? (yes/no): ")
    if again.lower() == "no":
        break
