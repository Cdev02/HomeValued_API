import pytest
import src.utils.validation as uf


def test_validate_data():
    assert uf.validate_data(1, 2, 1, 15, 90.6, "Laureles", "cra 72",
                            4, "no-integral", True) == True
    assert uf.validate_data(1, 2, 1, 15, 90.6, "Laureles",
                            "cra 72", 4, "no-integral", True) == True
    assert uf.validate_data(3, 3, 2, 10, 120.5, "Envigado",
                            "calle 10", 3, "integral", False) == True
    assert uf.validate_data(2, 1, 3, 5, 80.2, "El Poblado",
                            "cra 34", 5, "no-integral", True) == True
    assert uf.validate_data(1, 1, 1, 20, 60.0, "Belén",
                            "calle 20", 2, "integral", False) == True
    assert uf.validate_data(1.5, 2, 1, 15, 90.6, "Laureles",
                            "cra 72", 4, "no-integral", True) == False
    assert uf.validate_data(1, 2, 1, 15, -90.6, "Laureles",
                            "cra 72", 4, "no-integral", True) == False
    assert uf.validate_data(1, 2, 1, 15, 90.6, "Laureles",
                            "cra 72", 7, "no-integral", True) == False
    assert uf.validate_data(1, 2, 1, 15, 90.6, "Laureles",
                            "cra 72", 4, "semi-integral", True) == False
    assert uf.validate_data(1, 2, 1, 15, 90.6, "Laureles",
                            "cra 72", 4, "no-integral", "sí") == False
    assert uf.validate_data(1, 2, 1, 15, 90.6, "",
                            "cra 72", 4, "no-integral", True) == False
