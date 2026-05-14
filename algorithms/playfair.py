def generate_matrix(key):

    key = key.upper().replace("J", "I")

    matrix = []

    used = []

    for char in key:

        if char not in used and char.isalpha():

            used.append(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for char in alphabet:

        if char not in used:

            used.append(char)

    for i in range(0, 25, 5):

        matrix.append(used[i:i+5])

    return matrix


def find_position(matrix, char):

    for i in range(5):

        for j in range(5):

            if matrix[i][j] == char:

                return i, j


def prepare_text(text):

    text = text.upper().replace("J", "I")

    text = ''.join(filter(str.isalpha, text))

    prepared = ""

    i = 0

    while i < len(text):

        a = text[i]

        if i + 1 < len(text):

            b = text[i + 1]

        else:

            b = "X"

        if a == b:

            prepared += a + "X"

            i += 1

        else:

            prepared += a + b

            i += 2

    if len(prepared) % 2 != 0:

        prepared += "X"

    return prepared


def playfair_encrypt(text, key):

    matrix = generate_matrix(key)

    process = []

    # MATRIX DISPLAY

    process.append("PLAYFAIR 5x5 MATRIX")

    for row in matrix:

        process.append(' '.join(row))

    # PREPARED TEXT

    text = prepare_text(text)

    process.append(f"PREPARED TEXT: {text}")

    result = ""

    for i in range(0, len(text), 2):

        a = text[i]

        b = text[i + 1]

        row1, col1 = find_position(matrix, a)

        row2, col2 = find_position(matrix, b)

        # SAME ROW

        if row1 == row2:

            enc1 = matrix[row1][(col1 + 1) % 5]

            enc2 = matrix[row2][(col2 + 1) % 5]

            rule = "Same Row"

        # SAME COLUMN

        elif col1 == col2:

            enc1 = matrix[(row1 + 1) % 5][col1]

            enc2 = matrix[(row2 + 1) % 5][col2]

            rule = "Same Column"

        # RECTANGLE

        else:

            enc1 = matrix[row1][col2]

            enc2 = matrix[row2][col1]

            rule = "Rectangle Rule"

        process.append(
            f"""
PAIR: {a}{b}

POSITION:
{a} -> ({row1},{col1})
{b} -> ({row2},{col2})

RULE:
{rule}

RESULT:
{enc1}{enc2}
"""
        )

        result += enc1 + enc2

    return result, process


def playfair_decrypt(text, key):

    matrix = generate_matrix(key)

    process = []

    process.append("PLAYFAIR 5x5 MATRIX")

    for row in matrix:

        process.append(' '.join(row))

    result = ""

    for i in range(0, len(text), 2):

        a = text[i]

        b = text[i + 1]

        row1, col1 = find_position(matrix, a)

        row2, col2 = find_position(matrix, b)

        # SAME ROW

        if row1 == row2:

            dec1 = matrix[row1][(col1 - 1) % 5]

            dec2 = matrix[row2][(col2 - 1) % 5]

            rule = "Same Row"

        # SAME COLUMN

        elif col1 == col2:

            dec1 = matrix[(row1 - 1) % 5][col1]

            dec2 = matrix[(row2 - 1) % 5][col2]

            rule = "Same Column"

        # RECTANGLE

        else:

            dec1 = matrix[row1][col2]

            dec2 = matrix[row2][col1]

            rule = "Rectangle Rule"

        process.append(
            f"""
PAIR: {a}{b}

POSITION:
{a} -> ({row1},{col1})
{b} -> ({row2},{col2})

RULE:
{rule}

RESULT:
{dec1}{dec2}
"""
        )

        result += dec1 + dec2

    return result, process