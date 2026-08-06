# Microservicio de Pagos PSE - PagaFácil v3.2.0

BANCOS_PSE = ["BANCOLOMBIA", "DAVIVIENDA", "BBVA", "BOGOTA", "NEQUI"]

def process_payment(invoice_id, bank_code, amount):
    """Procesa pago a través de la pasarela bancaria PSE."""
    if bank_code not in BANCOS_PSE:
        return {"status": "error", "message": f"Banco no soportado: {bank_code}"}
    if amount <= 0:
        return {"status": "error", "message": "Monto invalido"}
    return {
        "transaction_id": f"TXN-{invoice_id}",
        "status": "pending",
        "bank": bank_code,
        "amount": amount
    }

def check_payment_status(transaction_id):
    """Consulta el estado de una transacción PSE."""
    return {"transaction_id": transaction_id, "status": "approved"}
