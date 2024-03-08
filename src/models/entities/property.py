class Property:
    def __init__(
        self,
        id,
        barrio=None,
        estrato=None,
        direccion=None,
        nivel_propiedad=None,
        antiguedad=None,
        area_propiedad=None,
        numero_habitaciones=None,
        garage=None,
        numero_banos=None,
        numero_pisos=None,
        tipo_cocina=None,
        owner=None,
    ) -> None:
        self.id = id
        self.barrio = barrio
        self.estrato = estrato
        self.direccion = direccion
        self.nivel_propiedad = nivel_propiedad
        self.antiguedad = antiguedad
        self.area_propiedad = area_propiedad
        self.numero_habitaciones = numero_habitaciones
        self.garage = garage
        self.numero_banos = numero_banos
        self.numero_pisos = numero_pisos
        self.tipo_cocina = tipo_cocina
        self.owner = owner

    def to_JSON(self):
        return {
            "id": self.id,
            "barrio": self.barrio,
            "estrato": self.estrato,
            "direccion": self.direccion,
            "nivel_propiedad": self.nivel_propiedad,
            "antiguedad": self.antiguedad,
            "area_propiedad": self.area_propiedad,
            "numero_habitaciones": self.numero_habitaciones,
            "garage": self.garage,
            "numero_banos": self.numero_banos,
            "numero_pisos": self.numero_pisos,
            "tipo_cocina": self.tipo_cocina,
            "owner": self.owner,
        }
