def validate_numeric_values(value, type_of_value):
    if isinstance(value, type_of_value):
        if value >= 0:
            return False
        return True
    return True


def validate_text_fixed_values(value, values_list):
    if isinstance(value, str):
        if value in values_list:
            return False
        return True
    return True


def validate_physical_characteristics(nivel_propiedad, numero_banos, numero_pisos, antiguedad, area_propiedad):
    result_list = []
    result = None
    for item in [nivel_propiedad, numero_banos, numero_pisos, antiguedad]:
        result = validate_numeric_values(item, int)
        result_list.append(result)
    result_list.append(validate_numeric_values(area_propiedad, float))
    return result_list


def validate_location_characteristics(barrio, direccion, estrato):
    estrato_failed = None
    location_failed = None
    if isinstance(estrato, int):
        if estrato in [1, 2, 3, 4, 5, 6]:
            estrato_failed = False
        else:
            estrato_failed = True
    else:
        estrato_failed = True

    if isinstance(barrio, str) and isinstance(direccion, str):
        if barrio != "" and direccion != "":
            location_failed = False
        else:
            location_failed = True
    else:
        location_failed = True
    return (estrato_failed, location_failed)


def validate_non_numeric_data(tipo_cocina, garage):
    tipo_cocina_failed = None
    garage_failed = None

    tipo_cocina_failed = validate_text_fixed_values(
        tipo_cocina, ['integral', 'no-integral'])
    if isinstance(garage, bool):
        garage_failed = False
    else:
        garage_failed = True
    return (tipo_cocina_failed, garage_failed)


def validate_data(nivel_propiedad, numero_banos, numero_pisos, antiguedad, area_propiedad, barrio, direccion, estrato, tipo_cocina, garage):
    result_physical = validate_physical_characteristics(
        nivel_propiedad, numero_banos, numero_pisos, antiguedad, area_propiedad)
    result_location = validate_location_characteristics(
        barrio, direccion, estrato)
    result_non_numerical = validate_non_numeric_data(tipo_cocina, garage)

    result_physical = result_physical == [False, False, False, False, False]
    result_location = result_location == (False, False)
    result_non_numerical = result_non_numerical == (False, False)

    if result_location == True and result_physical == True and result_non_numerical == True:
        return True
    return False
