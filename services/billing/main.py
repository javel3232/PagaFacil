# Microservicio de Facturación - PagaFácil v3.0.0
def generate_invoice(resident_id, amount, concept):
    """Genera factura de cuota de administración o arriendo."""
    return {"invoice_id": f"INV-{resident_id}", "amount": amount, "concept": concept}
