from flask import Flask, render_template, request
from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from algorithms.affine import affine_encrypt, affine_decrypt
from algorithms.hill import hill_encrypt, hill_decrypt
from algorithms.playfair import playfair_encrypt, playfair_decrypt

import json
import os

app = Flask(__name__)


# =========================
# SAVE HISTORY
# =========================

def save_history(data):

    filename = "history.json"

    history = []

    if os.path.exists(filename):

        with open(filename, "r") as f:

            history = json.load(f)

    history.append(data)

    with open(filename, "w") as f:

        json.dump(history, f, indent=4)


# =========================
# MAIN PAGE
# =========================

@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    process = []

    algorithm = ""

    if request.method == "POST":

        text = request.form["text"]

        algorithm = request.form["algorithm"]

        mode = request.form["mode"]

        try:

            # =========================
            # CAESAR
            # =========================

            if algorithm == "caesar":

                key = int(request.form["key"])

                # VALIDASI KEY

                if key < 1 or key > 25:

                    result = "Key Caesar harus antara 1 sampai 25"

                else:

                    if mode == "encrypt":

                        result, process = caesar_encrypt(
                            text,
                            key
                        )

                    else:

                        result, process = caesar_decrypt(
                            text,
                            key
                        )

            # =========================
            # VIGENERE
            # =========================

            elif algorithm == "vigenere":

                key = request.form["key"]

                if mode == "encrypt":

                    result, process = vigenere_encrypt(
                        text,
                        key
                    )

                else:

                    result, process = vigenere_decrypt(
                        text,
                        key
                    )

            # =========================
            # AFFINE
            # =========================

            elif algorithm == "affine":

                a = int(request.form["a"])

                b = int(request.form["b"])

                if mode == "encrypt":

                    result, process = affine_encrypt(
                        text,
                        a,
                        b
                    )

                else:

                    result, process = affine_decrypt(
                        text,
                        a,
                        b
                    )

            # =========================
            # HILL
            # =========================

            elif algorithm == "hill":

                key = request.form["matrix"]

                if mode == "encrypt":

                    result, process = hill_encrypt(
                        text,
                        key
                    )

                else:

                    result, process = hill_decrypt(
                        text,
                        key
                    )

            # =========================
            # PLAYFAIR
            # =========================

            elif algorithm == "playfair":

                key = request.form["key"]

                if mode == "encrypt":

                    result, process = playfair_encrypt(
                        text,
                        key
                    )

                else:

                    result, process = playfair_decrypt(
                        text,
                        key
                    )

            # =========================
            # SAVE HISTORY
            # =========================

            if result and "Error" not in result:

                save_history({

                    "algorithm": algorithm,

                    "mode": mode,

                    "text": text,

                    "result": result

                })

        except Exception as e:

            result = f"Error: {str(e)}"

    return render_template(

        "index.html",

        result=result,

        process=process,

        algorithm=algorithm

    )


# =========================
# HISTORY PAGE
# =========================

@app.route("/history")
def history():

    filename = "history.json"

    history_data = []

    if os.path.exists(filename):

        with open(filename, "r") as f:

            history_data = json.load(f)

    return render_template(

        "history.html",

        history=history_data

    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(debug=True)