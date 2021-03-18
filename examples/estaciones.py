import os

class Estacion:
    def __init__(self, codigo, descripcion, latitud, longitud, direccion, cp, poblacion, provincia, pais, cercanias, feve):
        self.codigo = codigo
        self.descripcion = descripcion
        self.latitud = float(latitud.replace(",", "."))
        self.longitud = float(longitud.replace(",", "."))
        self.direccion = direccion
        self.cp = cp
        self.poblacion = poblacion
        self.provincia = provincia
        self.pais = pais
        self.cercanias = cercanias.lower() == "si"
        self.feve = feve.lower() == "si"

    def __str__(self):
        return f"Estación #{self.codigo} - {self.poblacion} - {self.provincia}"


if __name__ == "__main__":
    import re
    import tracemalloc

    tracemalloc.start()

    def iter_quijote():
        letra_regex = re.compile("[a-záéíóúüñçA-ZÁÉÍÓÚÜÑÇ]")

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "quijote.txt"), "r", encoding="utf8") as f:

            palabra = ""
            while True:
                letra = f.read(1)

                if not letra:
                    break
                elif letra_regex.match(letra):
                    palabra += letra
                elif palabra:
                    yield palabra
                    palabra = ""

    palabras = iter_quijote()

    for palabra in palabras:
        print(estacion)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
