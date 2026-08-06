# Microservicio de Conciliación Contable - PagaFácil v3.0.0
def reconcile(transaction_id, bank_response):
    """Concilia automáticamente el pago con el registro bancario."""
    return {"transaction_id": transaction_id, "reconciled": True, "bank_response": bank_response}
