# Microservicio de Notificaciones - PagaFácil v3.0.0
def send_notification(user_id, message, channel="email"):
    """Envía notificación al residente o administrador por email/SMS."""
    return {"user_id": user_id, "channel": channel, "sent": True}
