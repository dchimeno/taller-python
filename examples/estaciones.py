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
