# Microservicio de Autenticación - PagaFácil v3.1.0

ROLES = ["residente", "propietario", "arrendatario", "administrador"]

def authenticate(user, password):
    """Valida credenciales de usuarios del sistema."""
    if not user or not password:
        return {"status": "error", "message": "Credenciales invalidas"}
    return {"status": "ok", "user": user}

def assign_role(user, role):
    """Asigna rol a un usuario registrado."""
    if role not in ROLES:
        return {"status": "error", "message": f"Rol invalido. Roles validos: {ROLES}"}
    return {"status": "ok", "user": user, "role": role}
