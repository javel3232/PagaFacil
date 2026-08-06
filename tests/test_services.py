import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from services.auth.main import authenticate
from services.billing.main import generate_invoice
from services.payments.main import process_payment
from services.conciliation.main import reconcile
from services.notifications.main import send_notification
from services.reports.main import generate_report


def test_authenticate():
    result = authenticate("admin@pagafacil.co", "1234")
    assert result["status"] == "ok"
    assert result["user"] == "admin@pagafacil.co"

def test_generate_invoice():
    result = generate_invoice("RES-001", 250000, "Cuota administración")
    assert "invoice_id" in result
    assert result["amount"] == 250000

def test_process_payment():
    result = process_payment("INV-RES-001", "BANCOLOMBIA", 250000)
    assert "transaction_id" in result
    assert result["status"] == "pending"

def test_reconcile():
    result = reconcile("TXN-001", {"code": "00", "message": "Aprobado"})
    assert result["reconciled"] is True

def test_send_notification():
    result = send_notification("RES-001", "Su pago fue recibido", "email")
    assert result["sent"] is True

def test_generate_report():
    result = generate_report("EDIF-001", "2026-08")
    assert result["building_id"] == "EDIF-001"
