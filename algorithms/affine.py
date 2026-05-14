def mod_inverse(a, m):

    for x in range(1, m):

        if (a * x) % m == 1:
            return x

    return None


def affine_encrypt(text, a, b):

    result = ""
    process = []

    for char in text.upper():

        if char.isalpha():

            x = ord(char) - 65

            encrypted = (a * x + b) % 26

            enc_char = chr(encrypted + 65)

            process.append(
                f"({a}*{x}+{b}) mod 26 = {encrypted} -> {enc_char}"
            )

            result += enc_char

        else:
            result += char

    return result, process


def affine_decrypt(text, a, b):

    result = ""
    process = []

    a_inv = mod_inverse(a, 26)

    if a_inv is None:
        raise ValueError("Nilai a tidak memiliki invers modulo 26")

    for char in text.upper():

        if char.isalpha():

            y = ord(char) - 65

            decrypted = (a_inv * (y - b)) % 26

            dec_char = chr(decrypted + 65)

            process.append(
                f"{a_inv}*({y}-{b}) mod 26 = {decrypted} -> {dec_char}"
            )

            result += dec_char

        else:
            result += char

    return result, process