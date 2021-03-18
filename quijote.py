from os import path
import re

ruta_quijote = path.join("examples", "files", "quijote.txt")

def palabras_quijote(ruta_quijote):
    patron = re.compile("[a-záéíóúüñçA-ZÑÇÁÉÍÓÚÜ]")
    palabra = ""

    with open(ruta_quijote, "r", encoding="utf8") as quijote:
        while True:
            letra = quijote.read(1)

            if not letra:
                break
            elif patron.match(letra):
                palabra += letra
            elif palabra:
                yield palabra
                palabra = ""

print([palabra for palabra in palabras_quijote(ruta_quijote)])