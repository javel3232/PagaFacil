# Convención de Commits - PagaFácil

## Formato
```
<tipo>(<módulo>): <descripción corta> | v<version> | <fecha>
```

## Tipos permitidos
| Tipo | Cuándo usarlo | Impacto versión |
|------|--------------|-----------------|
| feat | Nueva funcionalidad | MINOR |
| fix | Corrección de bug | PATCH |
| break | Cambio incompatible | MAJOR |
| chore | Tareas de mantenimiento | ninguno |
| docs | Documentación | ninguno |
| test | Pruebas | ninguno |
| ci | Pipeline CI/CD | ninguno |

## Ejemplos válidos
```
feat(auth): agregar autenticacion por token JWT | v3.1.0 | 2026-08-05
fix(payments): corregir timeout en pasarela PSE | v3.2.1 | 2026-08-05
break(billing): cambiar estructura de factura | v4.0.0 | 2026-08-05
docs(readme): actualizar guia de instalacion | 2026-08-05
test(conciliation): agregar pruebas de conciliacion | 2026-08-05
ci(pipeline): agregar job de deploy a staging | 2026-08-05
```

## Reglas
- Descripción en minúsculas y en español
- Máximo 72 caracteres en la descripción
- Siempre incluir el módulo afectado
- Un commit por cambio lógico, no mezclar módulos
