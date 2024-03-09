# test to_JSON

from src.models.entities.property import Property


def test_to_JSON():
    prop = Property(1, "Belen", 4, "cra 76", 2, 5,
                    67.8, 3, False, 2, 1, "integral", 1)
    print(prop)
    assert isinstance(prop.to_JSON(), dict) == True


def test_object_creation():
    prop = Property(1, "Belen", 4, "cra 76", 2, 5,
                    67.8, 3, False, 2, 1, "integral", 1)

    assert prop.id == 1
    assert prop.owner == 1
    assert prop.garage == False
    assert prop.tipo_cocina == "integral"
    assert prop.tipo_cocina != "Integral"
