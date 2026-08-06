# PagaFácil — Documento Técnico de Implementación

> Sistema simulado de pagos fintech para el recaudo de cuotas de administración y arriendos en edificios y conjuntos residenciales colombianos.

---

## 1. Repositorio en Git

**URL:** https://github.com/javel3232/PagaFacil.git

### Estructura del proyecto

```
PagaFacil/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          ← Pipeline CI/CD
├── scripts/
│   ├── version_manager.py     ← Gestor de versiones semántico
│   └── automation.py          ← Automatizador de flujo GitFlow
├── services/
│   ├── auth/main.py           ← Autenticación de usuarios
│   ├── billing/main.py        ← Generación de facturas
│   ├── payments/main.py       ← Integración pasarela PSE
│   ├── conciliation/main.py   ← Conciliación contable
│   ├── notifications/main.py  ← Envío de notificaciones
│   └── reports/main.py        ← Panel administrativo
├── tests/
│   └── test_services.py       ← Pruebas unitarias
├── COMMITS.md                 ← Convención de commits
├── version.json               ← Versión actual del sistema
├── requirements.txt           ← Dependencias Python
└── README.md                  ← Este documento
```

### Inicialización del repositorio

```bash
git clone https://github.com/javel3232/PagaFacil.git
cd PagaFacil
pip install -r requirements.txt
```

---

## 2. Estrategia de Branching — GitFlow

PagaFácil implementa **GitFlow** como estrategia de control de versiones:

```
main ──────────────────────────────────────► producción estable
  │
  └── develop ──────────────────────────────► integración continua
        │
        ├── feature/auth-module ──────────► módulo autenticación
        ├── feature/payments-pse ─────────► módulo pagos PSE
        ├── feature/billing-invoices ─────► módulo facturación
        │
        └── release/v3.0.0 ───────────────► preparación de versión
              │
              └── hotfix/v3.0.1 ───────────► corrección urgente
```

### Reglas de fusión

| Origen | Destino | Acción |
|--------|---------|--------|
| `feature/*` | `develop` | merge --no-ff |
| `develop` | `release/*` | merge --no-ff |
| `release/*` | `main` | merge --no-ff + tag |
| `release/*` | `develop` | sincronización |
| `hotfix/*` | `main` | merge --no-ff + tag |

---

## 3. Versionamiento Semántico (SemVer)

Formato: **MAJOR.MINOR.PATCH**

| Tipo commit | Impacto | Ejemplo |
|-------------|---------|---------|
| `feat` | MINOR +1, PATCH=0 | v3.0.0 → v3.1.0 |
| `fix` | PATCH +1 | v3.1.0 → v3.1.1 |
| `break` | MAJOR +1, MINOR=0, PATCH=0 | v3.1.1 → v4.0.0 |

### Evolución de versiones en PagaFácil

| Versión | Descripción |
|---------|-------------|
| v1.0.0 | Sistema monolítico — registro manual de pagos |
| v2.0.0 | Integración directa con pasarela bancaria PSE |
| v3.0.0 | Separación en microservicios |
| v3.1.0 | feat(auth): validación de roles y credenciales |
| v3.2.0 | feat(payments): integración bancos PSE |
| v3.2.1 | fix(billing): validación de conceptos de factura |
| v3.3.0 | feat(automation): script automatizador GitFlow |

---

## 4. Convención de Commits

Formato estándar **Conventional Commits**:

```
<tipo>(<módulo>): <descripción> | v<version> | <fecha>
```

### Tipos permitidos

| Tipo | Uso | Versión |
|------|-----|---------|
| `feat` | Nueva funcionalidad | MINOR |
| `fix` | Corrección de bug | PATCH |
| `break` | Cambio incompatible | MAJOR |
| `chore` | Mantenimiento | — |
| `docs` | Documentación | — |
| `test` | Pruebas | — |
| `ci` | Pipeline | — |

---

## 5. Pipeline CI/CD

El pipeline está configurado en `.github/workflows/ci-cd.yml` y se activa automáticamente en cada push.

### Flujo del pipeline

```
push a develop/main
        │
        ▼
  ┌─────────────┐
  │   BUILD     │  Verifica estructura de microservicios
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │    TEST     │  flake8 (lint) + pytest (pruebas unitarias)
  └──────┬──────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌──────────┐
│STAGING│ │PRODUCCIÓN│
│develop│ │  main    │
└───────┘ └──────────┘
```

### Jobs configurados

```yaml
build       → instala dependencias y verifica microservicios
test        → lint con flake8 + pruebas con pytest
deploy-staging     → se activa en rama develop
deploy-production  → se activa en rama main
```

---

## 6. Automatización de Procesos

### Script version_manager.py
Gestiona commits con versionamiento semántico interactivo:
```bash
python scripts/version_manager.py
```

### Script automation.py
Automatiza el flujo GitFlow completo:
```bash
python scripts/automation.py
```

Opciones disponibles:
```
1. Crear rama feature
2. Cerrar rama feature → develop
3. Crear rama release
4. Cerrar rama release → main
5. Hacer commit con SemVer automático
6. Ver log de commits
7. Ver ramas
```

---

## 7. Evidencias

### Log de commits

```
* c40a125 (HEAD -> develop) feat(automation): agregar script de automatizacion GitFlow y versionamiento | v3.3.0 | 2026-08-05
* 021de9b ci(pipeline): configurar jobs build, test y deploy staging/produccion | 2026-08-05
* d527306 docs(commits): agregar convencion de commits del proyecto | 2026-08-05
* 07b958b chore(version): actualizar version.json a v3.2.1 tras merge de features | 2026-08-05
| * e70751d (feature/billing-invoices) fix(billing): corregir validacion de conceptos y agregar cancelacion de facturas | v3.2.1 | 2026-08-05
| * bb2fa5f (feature/payments-pse) feat(payments): integrar bancos PSE y consulta de estado de transaccion | v3.2.0 | 2026-08-05
| * 3daa61c (feature/auth-module) feat(auth): agregar validacion de roles y credenciales | v3.1.0 | 2026-08-05
* 66db584 (release/v3.0.0, main, hotfix/v3.0.1) feat(project): estructura inicial microservicios PagaFacil v3.0.0
```

### Ramas creadas

```
main
develop
feature/auth-module
feature/payments-pse
feature/billing-invoices
release/v3.0.0
hotfix/v3.0.1
```

---

## 8. Modelo de Gestión de Configuración

### Principios aplicados

| Principio | Implementación |
|-----------|---------------|
| Trazabilidad | Cada commit incluye tipo, módulo, versión y fecha |
| Automatización | Scripts Python para commits, ramas y versiones |
| Integración continua | GitHub Actions en cada push |
| Separación de ambientes | staging (develop) y producción (main) |
| Versionamiento semántico | SemVer MAJOR.MINOR.PATCH en version.json |
| Branching estructurado | GitFlow con ramas feature, release y hotfix |

### Flujo completo de un cambio

```
1. python scripts/automation.py → opción 1 (crear feature)
2. Desarrollar el cambio en la rama feature/*
3. python scripts/automation.py → opción 5 (commit con SemVer)
4. python scripts/automation.py → opción 2 (cerrar feature → develop)
5. git push origin develop       → activa pipeline staging
6. python scripts/automation.py → opción 3 (crear release)
7. python scripts/automation.py → opción 4 (cerrar release → main)
8. git push origin main          → activa pipeline producción
```

---

*Documento generado para PagaFácil v3.3.0 — 2026-08-05*
