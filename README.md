# PagaFácil — Documento Técnico de Implementación

Sistema simulado de pagos fintech para el recaudo de cuotas de administración y arriendos en edificios y conjuntos residenciales colombianos. Construido bajo arquitectura de microservicios con estrategia GitFlow, versionamiento semántico y pipeline CI/CD automatizado con Docker.

---

## 1. Repositorio en Git

URL: https://github.com/javel3232/PagaFacil.git

### Estructura del proyecto

```
PagaFacil/
├── .github/
│   └── workflows/
│       └── ci-cd.yml              Pipeline CI/CD unificado
├── scripts/
│   ├── version_manager.py         Gestor de versiones semántico
│   └── automation.py              Automatizador de flujo GitFlow
├── services/
│   ├── auth/main.py               Autenticación y roles de usuarios
│   ├── billing/main.py            Generación y cancelación de facturas
│   ├── payments/main.py           Integración pasarela PSE
│   ├── conciliation/main.py       Conciliación contable automática
│   ├── notifications/main.py      Envío de notificaciones
│   └── reports/main.py            Panel administrativo de reportes
├── tests/
│   └── test_services.py           Pruebas unitarias de todos los módulos
├── Dockerfile                     Imagen Docker del sistema
├── COMMITS.md                     Convención de commits
├── version.json                   Versión actual del sistema
├── requirements.txt               Dependencias Python
└── README.md                      Este documento
```

### Inicialización

```bash
git clone https://github.com/javel3232/PagaFacil.git
cd PagaFacil
pip install -r requirements.txt
```

---

## 2. Estrategia de Branching — GitFlow

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
| feature/* | develop | merge --no-ff |
| develop | release/* | merge --no-ff |
| release/* | main | merge --no-ff + tag |
| hotfix/* | main | merge --no-ff + tag |

### Automatización GitFlow

```bash
python scripts/automation.py
```

Opciones disponibles:
```
1. Crear rama feature
2. Cerrar rama feature a develop
3. Crear rama release
4. Cerrar rama release a main
5. Hacer commit con SemVer automático
6. Ver log de commits
7. Ver ramas
```

---

## 3. Versionamiento Semántico (SemVer)

Formato: MAJOR.MINOR.PATCH

| Tipo commit | Impacto | Ejemplo |
|-------------|---------|---------|
| feat | MINOR +1 | v3.0.0 a v3.1.0 |
| fix | PATCH +1 | v3.1.0 a v3.1.1 |
| break | MAJOR +1 | v3.1.1 a v4.0.0 |

### Evolución de versiones

| Versión | Descripción |
|---------|-------------|
| v1.0.0 | Sistema monolítico — registro manual de pagos |
| v2.0.0 | Integración directa con pasarela bancaria PSE |
| v3.0.0 | Separación en microservicios |
| v3.1.0 | feat(auth): validación de roles y credenciales |
| v3.2.0 | feat(payments): integración bancos PSE |
| v3.2.1 | fix(billing): validación de conceptos de factura |
| v3.3.0 | feat(automation): script automatizador GitFlow |
| v3.4.0 | feat(docker): imágenes Docker por ambiente |

---

## 4. Convención de Commits

Formato: `<tipo>(<módulo>): <descripción> | v<version> | <fecha>`

| Tipo | Uso | Versión |
|------|-----|---------|
| feat | Nueva funcionalidad | MINOR |
| fix | Corrección de bug | PATCH |
| break | Cambio incompatible | MAJOR |
| chore | Mantenimiento | — |
| docs | Documentación | — |
| test | Pruebas | — |
| ci | Pipeline | — |

---

## 5. Pipeline CI/CD

El pipeline está definido en `.github/workflows/ci-cd.yml` y se activa automáticamente en cada push a `develop` o `main`.

### Flujo del pipeline

```
develop:
Build → Deploy DEV → Acceptance Test DEV → Deploy QA → Acceptance Test QA → [Security skipped] → [PDN skipped]

main:
Build → Deploy DEV → Acceptance Test DEV → Deploy QA → Acceptance Test QA → Security Test → Deploy PDN
```

### Descripción de cada stage

| Stage | Descripción | Rama |
|-------|-------------|------|
| Build | Lint + pruebas unitarias + verificación de estructura | develop / main |
| Deploy DEV | Construye imagen Docker pagafacil:dev | develop / main |
| Acceptance Test DEV | Corre el contenedor DEV y valida todos los módulos | develop / main |
| Deploy QA | Construye imagen Docker pagafacil:qa | develop / main |
| Acceptance Test QA | Corre el contenedor QA y valida todos los módulos | develop / main |
| Security Test | Análisis de seguridad con bandit | solo main |
| Deploy PDN | Construye imagen Docker pagafacil:latest y despliega | solo main |

### Imágenes Docker generadas

| Imagen | Ambiente | Activación |
|--------|----------|------------|
| pagafacil:dev | Desarrollo | push a develop o main |
| pagafacil:qa | Calidad | push a develop o main |
| pagafacil:latest | Producción | solo push a main |

---

## 6. Evidencias del Pipeline

A continuación se presentan las evidencias visuales del pipeline CI/CD funcionando en GitHub Actions.

### Pipeline en ejecución — rama develop

Muestra todos los stages del pipeline corriendo desde Build hasta Acceptance Test QA en la rama develop.

![Pipeline develop en ejecucion](https://drive.google.com/uc?export=view&id=1VoCjiMEwURpsHPTNmIc-0YRLIoUx0dXQ)

### Pipeline develop — hasta Acceptance Test QA completado

Todos los stages de develop completados exitosamente hasta Acceptance Test QA.

![Pipeline develop hasta Acceptance QA](https://drive.google.com/uc?export=view&id=1STuqK-p7ZVA2T38m9mh0TywGazQaPW-E)

### Pipeline main — Deploy PDN corriendo

Stage Deploy PDN ejecutándose en la rama main después de pasar todos los stages previos.

![Deploy PDN corriendo](https://drive.google.com/uc?export=view&id=1PXzcKZKnREowImccANmu8PWrXHiuQlZu)

### Pipeline main — todos los stages completados

Vista completa del pipeline en main con todos los stages en verde incluyendo Security Test y Deploy PDN.

![Pipeline completo main](https://drive.google.com/uc?export=view&id=1TcWDuDbt4rlsNEM5BfRy8EdIRdRURAXS)

### Commits en rama develop

Historial de commits en la rama develop siguiendo la convención de Conventional Commits con versionamiento semántico.

![Commits develop](https://drive.google.com/uc?export=view&id=1hb8PU8cTuj7g2nUbg1RzvKRR5_f55KFG)

### Log de despliegue Deploy PDN

Log detallado del stage Deploy PDN mostrando la construcción de la imagen Docker y el despliegue en producción.

![Log Deploy PDN](https://drive.google.com/uc?export=view&id=1nsKr2tN1je7YiYP3f0w_tH8RvxBUZYiN)

---

## 7. Log de Commits

```
*   5a830d6 (main) chore(release): merge develop a main v3.4.0 | 2026-08-05
|
| * 4c8031f (develop) ci(pipeline): usar docker build local sin push a registry | 2026-08-05
| * 46a1060 feat(docker): agregar Dockerfile y deploy de imagenes por ambiente | v3.4.0 | 2026-08-05
| * c40a125 feat(automation): agregar script de automatizacion GitFlow | v3.3.0 | 2026-08-05
| * 021de9b ci(pipeline): configurar jobs build, test y deploy | 2026-08-05
| * d527306 docs(commits): agregar convencion de commits del proyecto | 2026-08-05
| * 07b958b chore(version): actualizar version.json a v3.2.1 | 2026-08-05
| * e70751d fix(billing): corregir validacion de conceptos | v3.2.1 | 2026-08-05
| * bb2fa5f feat(payments): integrar bancos PSE | v3.2.0 | 2026-08-05
| * 3daa61c feat(auth): agregar validacion de roles y credenciales | v3.1.0 | 2026-08-05
|
* 66db584 feat(project): estructura inicial microservicios PagaFacil v3.0.0
```

### Ramas del proyecto

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

| Principio | Implementación |
|-----------|---------------|
| Trazabilidad | Cada commit incluye tipo, módulo, versión y fecha |
| Automatización | Scripts Python para commits, ramas y versiones |
| Contenedorización | Docker por ambiente dev, qa y pdn |
| Integración continua | GitHub Actions en cada push |
| Separación de ambientes | DEV, QA y PDN con imágenes Docker independientes |
| Versionamiento semántico | SemVer MAJOR.MINOR.PATCH en version.json |
| Branching estructurado | GitFlow con ramas feature, release y hotfix |

### Flujo completo de un cambio

```
1. python scripts/automation.py  opcion 1  crear feature
2. Desarrollar el cambio
3. python scripts/automation.py  opcion 5  commit con SemVer
4. python scripts/automation.py  opcion 2  cerrar feature a develop
5. git push origin develop                 activa pipeline DEV y QA
6. git checkout main
7. git merge develop --no-ff               activa pipeline PDN completo
8. git push origin main
```

---

*PagaFácil v3.4.0 — 2026-08-05*
