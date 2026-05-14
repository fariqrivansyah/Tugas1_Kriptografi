def generate_key(text, key):

    key = list(key)
    if len(text) == len(key):
        return key

    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])

    return "".join(key)


def vigenere_encrypt(text, key):

    result = ""
    process = []

    key = generate_key(text, key)

    for i in range(len(text)):

        char = text[i]

        if char.isalpha():

            x = ord(char.upper()) - 65
            k = ord(key[i].upper()) - 65

            encrypted = (x + k) % 26

            enc_char = chr(encrypted + 65)

            process.append(
                f"{char} ({x}) + {key[i]} ({k}) mod 26 = {encrypted} -> {enc_char}"
            )

            result += enc_char

        else:
            result += char

    return result, process


def vigenere_decrypt(text, key):

    result = ""
    process = []

    key = generate_key(text, key)

    for i in range(len(text)):

        char = text[i]

        if char.isalpha():

            x = ord(char.upper()) - 65
            k = ord(key[i].upper()) - 65

            decrypted = (x - k) % 26

            dec_char = chr(decrypted + 65)

            process.append(
                f"{char} ({x}) - {key[i]} ({k}) mod 26 = {decrypted} -> {dec_char}"
            )

            result += dec_char

        else:
            result += char

    return result, process