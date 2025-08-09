from flask import Flask as fl, render_template as html, request as respuesta
import random as aleatorio
import string

encritador = fl(__name__)

@encritador.route("/", methods=["GET", "POST"])
def paginaprincipal():
    codigo_final = None
    if respuesta.method == "POST":
        palabra = respuesta.form["password"].strip()
        if palabra:
            # Convertir a mayúsculas y minúsculas aleatoriamente
            letras = [letra.upper() if aleatorio.choice([True, False]) else letra.lower() for letra in palabra]

            # Mezclar las letras
            aleatorio.shuffle(letras)
            codigo = "".join(letras)

            # Insertar ñ o Ñ aleatoria
            posicion_ñ = aleatorio.randint(0, len(codigo))
            letra_ñ = "Ñ" if aleatorio.choice([True, False]) else "ñ"
            codigo = codigo[:posicion_ñ] + letra_ñ + codigo[posicion_ñ:]

            # Insertar números y letras aleatorias hasta llegar a 12 caracteres
            caracteres_extra = string.ascii_letters + string.digits
            while len(codigo) < 12:
                posicion_insertar = aleatorio.randint(0, len(codigo))
                nuevo_caracter = aleatorio.choice(caracteres_extra)
                codigo = codigo[:posicion_insertar] + nuevo_caracter + codigo[posicion_insertar:]

            # Asegurar longitud exacta de 12
            codigo_final = codigo[:12]

    return html("index.html", clave=codigo_final)

if __name__ == '__main__':
    encritador.run(host="0.0.0.0", port=5000, debug=True)