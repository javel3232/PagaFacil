# Microservicio de Pagos PSE - PagaFácil v3.0.0
def process_payment(invoice_id, bank_code, amount):
    """Procesa pago a través de la pasarela bancaria PSE."""
    return {"transaction_id": f"TXN-{invoice_id}", "status": "pending", "bank": bank_code}
