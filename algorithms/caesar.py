def caesar_encrypt(text, key):

    result = ""
    process = []

    for char in text:

        if char.isalpha():

            shift = 65 if char.isupper() else 97

            old = ord(char) - shift
            new = (old + key) % 26

            encrypted = chr(new + shift)

            process.append(
                f"{char} -> ({old}+{key}) mod 26 = {new} -> {encrypted}"
            )

            result += encrypted

        else:
            result += char

    return result, process


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)