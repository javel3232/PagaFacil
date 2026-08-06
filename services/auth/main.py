# Microservicio de Autenticación - PagaFácil
# SemVer: feat → sube MINOR (v3.1.0)

ROLES = ["residente", "propietario", "arrendatario", "administrador"]

def authenticate(user, password):
    """Valida credenciales de usuarios del sistema."""
    if not user or not password:
        return {"status": "error", "message": "Credenciales inválidas"}
    return {"status": "ok", "user": user}

def assign_role(user, role):
    """Asigna rol a un usuario registrado."""
    if role not in ROLES:
        return {"status": "error", "message": f"Rol inválido. Roles válidos: {ROLES}"}
    return {"status": "ok", "user": user, "role": role}
