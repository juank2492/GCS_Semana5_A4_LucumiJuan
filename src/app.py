# src/app.py
# API Inventario (simulada) - GCS Semana 5, Actividad 4

products = []


def list_products():
    """REQ-001: Retorna la lista completa de productos."""
    return products


def add_product(name, qty):
    """REQ-002: Agrega un producto con nombre y cantidad >= 0."""
    if not name:
        raise ValueError("name required")
    if qty < 0:
        raise ValueError("qty must be >= 0")
    products.append({"name": name, "qty": qty})
    return True


def filter_products_by_date(from_date, to_date=None):
    """REQ-003: Filtrar productos por fecha de creación.
    
    NOTA: Funcionalidad pendiente de implementación completa.
    Issue de referencia: ISSUE-21
    """
    # Placeholder: implementación pendiente
    raise NotImplementedError("filter by date not yet implemented (ISSUE-21)")
