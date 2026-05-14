import numpy as np


def text_to_numbers(text):

    return [ord(c) - 65 for c in text]


def numbers_to_text(nums):

    return ''.join(chr(n % 26 + 65) for n in nums)


def parse_key_matrix(key):

    rows = key.split(";")

    matrix = []

    for row in rows:

        matrix.append(
            list(map(int, row.split(",")))
        )

    return np.array(matrix)


def hill_encrypt(text, key):

    process = []

    key_matrix = parse_key_matrix(key)

    n = key_matrix.shape[0]

    text = text.upper().replace(" ", "")

    while len(text) % n != 0:

        text += "X"

    result = ""

    for i in range(0, len(text), n):

        block = text[i:i+n]

        vector = np.array(
            text_to_numbers(block)
        )

        encrypted = np.dot(
            key_matrix,
            vector
        ) % 26

        enc_text = numbers_to_text(
            encrypted
        )

        process.append(
            f"""
BLOCK: {block}

VECTOR:
{vector.tolist()}

KEY MATRIX:
{key_matrix.tolist()}

MULTIPLICATION RESULT:
{encrypted.tolist()}

OUTPUT:
{enc_text}
"""
        )

        result += enc_text

    return result, process


def matrix_mod_inverse(matrix, modulus):

    det = int(round(np.linalg.det(matrix)))

    det_inv = pow(det, -1, modulus)

    matrix_adj = np.round(det * np.linalg.inv(matrix)).astype(int)

    return (det_inv * matrix_adj) % modulus


def hill_decrypt(text, key):

    process = []

    key_matrix = parse_key_matrix(key)

    inverse_matrix = matrix_mod_inverse(key_matrix, 26)

    n = inverse_matrix.shape[0]

    result = ""

    for i in range(0, len(text), n):

        block = text[i:i+n]

        vector = np.array(text_to_numbers(block))

        decrypted = np.dot(inverse_matrix, vector) % 26

        dec_text = numbers_to_text(decrypted)

        process.append(
            f"{block} -> {vector.tolist()} | "
            f"Decrypted: {decrypted.tolist()} -> {dec_text}"
        )

        result += dec_text

    return result, process