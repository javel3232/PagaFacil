#!/usr/bin/env python3
"""
PagaFácil - Automatizador de procesos de desarrollo
Gestiona el flujo GitFlow, versionamiento semántico y commits
"""
import subprocess
import json
import os
from datetime import datetime

ROOT = os.path.join(os.path.dirname(__file__), "..")
VERSION_FILE = os.path.join(ROOT, "version.json")


def run(cmd, capture=False):
    result = subprocess.run(cmd, cwd=ROOT, capture_output=capture, text=True)
    if capture:
        return result.stdout.strip()
    return result.returncode


def load_version():
    with open(VERSION_FILE) as f:
        return json.load(f)


def save_version(v):
    with open(VERSION_FILE, "w") as f:
        json.dump(v, f, indent=2)


def get_version_str():
    v = load_version()
    return f"{v['major']}.{v['minor']}.{v['patch']}"


def bump_version(tipo):
    v = load_version()
    if tipo == "major":
        v["major"] += 1; v["minor"] = 0; v["patch"] = 0
    elif tipo == "minor":
        v["minor"] += 1; v["patch"] = 0
    else:
        v["patch"] += 1
    save_version(v)
    return get_version_str()


def current_branch():
    return run(["git", "branch", "--show-current"], capture=True)


def crear_feature():
    nombre = input("Nombre del feature (ej: auth-jwt): ").strip()
    rama = f"feature/{nombre}"
    run(["git", "checkout", "develop"])
    run(["git", "checkout", "-b", rama])
    print(f"✅ Rama '{rama}' creada desde develop")


def cerrar_feature():
    rama = current_branch()
    if not rama.startswith("feature/"):
        print("❌ Debes estar en una rama feature/*"); return
    run(["git", "checkout", "develop"])
    run(["git", "merge", "--no-ff", rama, "-m",
         f"chore(merge): integrar {rama} en develop | {datetime.now().strftime('%Y-%m-%d')}"])
    run(["git", "branch", "-d", rama])
    print(f"✅ Feature '{rama}' integrado en develop y eliminado")


def crear_release():
    version = get_version_str()
    rama = f"release/v{version}"
    run(["git", "checkout", "develop"])
    run(["git", "checkout", "-b", rama])
    print(f"✅ Rama '{rama}' creada desde develop")


def cerrar_release():
    rama = current_branch()
    if not rama.startswith("release/"):
        print("❌ Debes estar en una rama release/*"); return
    version = rama.replace("release/v", "")
    run(["git", "checkout", "main"])
    run(["git", "merge", "--no-ff", rama, "-m",
         f"chore(release): publicar v{version} en main | {datetime.now().strftime('%Y-%m-%d')}"])
    run(["git", "tag", f"v{version}"])
    run(["git", "checkout", "develop"])
    run(["git", "merge", "--no-ff", rama, "-m",
         f"chore(release): sincronizar v{version} en develop | {datetime.now().strftime('%Y-%m-%d')}"])
    run(["git", "branch", "-d", rama])
    print(f"✅ Release v{version} publicado en main y sincronizado en develop")


def hacer_commit():
    tipos = {"1": ("feat", "minor"), "2": ("fix", "patch"), "3": ("break", "major"),
             "4": ("chore", None), "5": ("docs", None), "6": ("test", None), "7": ("ci", None)}
    print("\nTipo de commit:")
    print("1. feat  → nueva funcionalidad (MINOR)")
    print("2. fix   → corrección de bug   (PATCH)")
    print("3. break → cambio incompatible (MAJOR)")
    print("4. chore → mantenimiento")
    print("5. docs  → documentación")
    print("6. test  → pruebas")
    print("7. ci    → pipeline")
    opcion = input("Elige: ").strip()
    if opcion not in tipos:
        print("Opción inválida"); return
    prefijo, tipo_v = tipos[opcion]
    modulo = input("Módulo (auth/billing/payments/conciliation/notifications/reports): ").strip()
    descripcion = input("Descripción: ").strip()
    if tipo_v:
        version = bump_version(tipo_v)
        msg = f"{prefijo}({modulo}): {descripcion} | v{version} | {datetime.now().strftime('%Y-%m-%d')}"
    else:
        msg = f"{prefijo}({modulo}): {descripcion} | {datetime.now().strftime('%Y-%m-%d')}"
    run(["git", "add", "."])
    run(["git", "commit", "-m", msg])
    print(f"✅ Commit: {msg}")


def ver_log():
    log = run(["git", "log", "--oneline", "--all", "--graph", "--decorate"], capture=True)
    print("\n📋 Historial de commits:\n")
    print(log)


def ver_ramas():
    ramas = run(["git", "branch", "-a"], capture=True)
    print("\n🌿 Ramas del proyecto:\n")
    print(ramas)


def main():
    while True:
        print("\n" + "=" * 45)
        print("  PagaFácil - Automatizador de Desarrollo")
        print(f"  Versión actual: v{get_version_str()}")
        print(f"  Rama actual:    {current_branch()}")
        print("=" * 45)
        print("1. Crear rama feature")
        print("2. Cerrar rama feature → develop")
        print("3. Crear rama release")
        print("4. Cerrar rama release → main")
        print("5. Hacer commit")
        print("6. Ver log de commits")
        print("7. Ver ramas")
        print("0. Salir")
        opcion = input("\nElige opción: ").strip()
        opciones = {
            "1": crear_feature, "2": cerrar_feature,
            "3": crear_release, "4": cerrar_release,
            "5": hacer_commit, "6": ver_log, "7": ver_ramas
        }
        if opcion == "0":
            print("👋 Hasta luego"); break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
