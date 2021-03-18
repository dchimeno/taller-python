from functools import reduce
from examples.scrapper import obtener_noticias
import json

noticias, numero_peticiones = obtener_noticias()

categorias = set(map(lambda x: x["categoria"], noticias))

print(categorias)

def reduce_noticias(x, y):
    resultado = x

    if isinstance(x, tuple):
        autor, titulo = x
        resultado = {autor: titulo}

    autor, titulo = y
    resultado[autor] = titulo + resultado.get(autor, [])

    return resultado

titulos_por_autor = reduce(reduce_noticias, map(lambda x: (x["autor"], [x["titulo"]]), noticias))
#titulos_por_autor = reduce(lambda x, y: {**{x[0]: x[1]}, **{y[0]: y[1] if x[0] != y[0] else [*x[1], *y[1]]}} if isinstance(x, tuple) else {**x, **{y[0]: [*x.get(y[0], []),*y[1]]}}, map(lambda x: (x["autor"], [x["titulo"]]), noticias))

#print(titulos_por_autor)
print(json.dumps(titulos_por_autor, indent=4))
