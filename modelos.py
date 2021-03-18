from datetime import datetime
import hashlib
import json

from examples.scrapper import obtener_noticias

#print(obtener_noticias()[0])

class Noticia:
    
    def __init__(self, fecha_publicacion, enlace, autor, categoria, titulo, resumen):
        self.fecha_publicacion = fecha_publicacion
        self.enlace = enlace
        self.autor = autor
        self.categoria = categoria
        self.titulo = titulo
        self.resumen = resumen

    @property
    def id(self):
        return hashlib.md5(f"{self.fecha_publicacion}{self.autor}".encode()).hexdigest()

    def guardar_obj(self):
        try:
            with open("noticias.json", "r") as f:
                noticias = json.load(f)
        except FileNotFoundError:
            noticias = {}

        noticias[self.id] = {
            "fecha_publicacion": self.fecha_publicacion.strftime("%Y-%m-%d %H:%M:%S"),
            "enlace": self.enlace,
            "autor": self.autor,
            "categoria": self.categoria,
            "titulo": self.titulo,
            "resumen": self.resumen
        }

        with open("noticias.json", "w") as f:
            f.write(json.dumps(noticias, indent=4))

    #def __repr__(self):
    #    return self.__str__()

    def __str__(self):
        return f"{self.fecha_publicacion.strftime('%Y-%m-%d')} - {self.titulo} - {self.autor}"

noticias, num_peticiones = obtener_noticias()

[Noticia(**noticia).guardar_obj() for noticia in noticias]
