from examples.scrapper import obtener_noticias
import json

resultado, numero_peticiones = obtener_noticias()

categorias = {noticia["categoria"] for noticia in resultado}

titulos_por_autor = {autor: [noticia["titulo"] for noticia in resultado if noticia["autor"] == autor]\
                     for autor in {noticia["autor"] for noticia in resultado}}

print(json.dumps(titulos_por_autor, indent=4))