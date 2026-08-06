# PagaFácil

Sistema simulado de pagos tipo fintech para el recaudo de cuotas de administración y arriendos en edificios y conjuntos residenciales colombianos.

## Arquitectura de Microservicios

| Servicio | Descripción |
|---|---|
| auth | Autenticación de usuarios |
| billing | Generación de facturas |
| payments | Integración con pasarela PSE |
| conciliation | Conciliación contable automática |
| notifications | Envío de alertas y notificaciones |
| reports | Panel administrativo de reportes |

## Estrategia de Branching (GitFlow)

```
main        → producción estable
develop     → integración continua
feature/*   → nuevas funcionalidades
release/*   → preparación de versiones
hotfix/*    → correcciones urgentes en producción
```

## Versionamiento Semántico (SemVer)

Formato: `MAJOR.MINOR.PATCH`

- `feat(módulo): descripción` → sube MINOR (v3.1.0)
- `fix(módulo): descripción`  → sube PATCH (v3.0.1)
- `break(módulo): descripción` → sube MAJOR (v4.0.0)

## Uso del Version Manager

```bash
python scripts/version_manager.py
```

## Pipeline CI/CD

- `develop` → build + test + deploy staging
- `main`    → build + test + deploy producción

## Versión actual: v3.0.0
