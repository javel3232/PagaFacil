#!/usr/bin/env python3
"""
PagaFácil - Gestor de versiones semántico
Automatiza commits siguiendo Conventional Commits + SemVer
"""
import subprocess
import json
import os
from datetime import datetime

VERSION_FILE = os.path.join(os.path.dirname(__file__), "..", "version.json")

def load_version():
    with open(VERSION_FILE) as f:
        return json.load(f)

def save_version(v):
    with open(VERSION_FILE, "w") as f:
        json.dump(v, f, indent=2)

def bump(tipo):
    v = load_version()
    if tipo == "major":
        v["major"] += 1; v["minor"] = 0; v["patch"] = 0
    elif tipo == "minor":
        v["minor"] += 1; v["patch"] = 0
    else:
        v["patch"] += 1
    save_version(v)
    return f"{v['major']}.{v['minor']}.{v['patch']}"

def git_commit(mensaje, tipo_version="patch"):
    version = bump(tipo_version)
    subprocess.run(["git", "add", "."], cwd=os.path.join(os.path.dirname(__file__), ".."))
    commit_msg = f"{mensaje} | v{version} | {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=os.path.join(os.path.dirname(__file__), ".."))
    subprocess.run(["git", "tag", f"v{version}"], cwd=os.path.join(os.path.dirname(__file__), ".."))
    print(f"\n✅ Commit realizado: {commit_msg}")
    return version

def show_log():
    result = subprocess.run(
        ["git", "log", "--oneline", "-10"],
        capture_output=True, text=True,
        cwd=os.path.join(os.path.dirname(__file__), "..")
    )
    print("\n📋 Últimos 10 commits:\n")
    print(result.stdout if result.stdout else "No hay commits aún.")

def main():
    print("=" * 40)
    print("  PagaFácil - Version Manager")
    print("=" * 40)
    v = load_version()
    print(f"  Versión actual: v{v['major']}.{v['minor']}.{v['patch']}")
    print("=" * 40)
    print("1. feat  → minor bump  (nueva funcionalidad)")
    print("2. fix   → patch bump  (corrección de bug)")
    print("3. break → major bump  (cambio incompatible)")
    print("4. Ver log de commits")
    print("0. Salir")

    opcion = input("\nElige opción: ").strip()

    if opcion == "0":
        return
    if opcion == "4":
        show_log()
        return

    tipos = {"1": ("feat", "minor"), "2": ("fix", "patch"), "3": ("break", "major")}
    if opcion not in tipos:
        print("Opción inválida"); return

    prefijo, tipo_v = tipos[opcion]
    modulo = input("Módulo afectado (auth/billing/payments/conciliation/notifications/reports): ").strip()
    descripcion = input("Descripción del cambio: ").strip()
    mensaje = f"{prefijo}({modulo}): {descripcion}"

    version = git_commit(mensaje, tipo_v)
    print(f"🏷️  Nueva versión: v{version}\n")

if __name__ == "__main__":
    main()
