# tests/test_app.py
# Pruebas unitarias - API Inventario

import pytest
from src.app import add_product, list_products


def setup_function():
    """Limpia la lista de productos antes de cada prueba."""
    import src.app as app
    app.products.clear()


def test_add_and_list():
    """REQ-001, REQ-002: Agregar y listar productos."""
    add_product("item", 1)
    assert len(list_products()) >= 1


def test_add_product_invalid_name():
    """REQ-002: Nombre vacío debe lanzar ValueError."""
    with pytest.raises(ValueError, match="name required"):
        add_product("", 5)


def test_add_product_negative_qty():
    """REQ-002: Cantidad negativa debe lanzar ValueError."""
    with pytest.raises(ValueError, match="qty must be >= 0"):
        add_product("producto", -1)


def test_list_products_empty():
    """REQ-001: Lista vacía retorna lista."""
    result = list_products()
    assert isinstance(result, list)
