# Microservicio de Facturación - PagaFácil
# SemVer: fix → sube PATCH (v3.2.1)

CONCEPTOS_VALIDOS = ["administracion", "arriendo", "parqueadero", "multa"]

def generate_invoice(resident_id, amount, concept):
    """Genera factura de cuota de administración o arriendo."""
    if concept not in CONCEPTOS_VALIDOS:
        return {"status": "error", "message": f"Concepto inválido: {concept}"}
    return {
        "invoice_id": f"INV-{resident_id}",
        "amount": amount,
        "concept": concept,
        "status": "generada"
    }

def cancel_invoice(invoice_id, reason):
    """Cancela una factura generada."""
    return {"invoice_id": invoice_id, "status": "cancelada", "reason": reason}
