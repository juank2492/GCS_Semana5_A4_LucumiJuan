# API Inventario (mini)

- Endpoints simulados: `GET /products`, `POST /products`
- Objetivo: repo auditable (versiones + estados + trazabilidad)

## Cómo ejecutar (simulado)

- No se requiere despliegue real. Este repositorio se usa para GCS.

```bash
# Instalar dependencias (opcionales para pruebas)
pip install pytest

# Ejecutar pruebas
pytest tests/
```

## Convención

- Commits: `chore/docs/feat/fix` + referencia `ISSUE-xx`
- Versiones: SemVer (`vMAJOR.MINOR.PATCH`)

## Historial de versiones

| Versión  | Fecha      | Descripción                              |
|----------|------------|------------------------------------------|
| v1.0.0   | 2026-01-15 | Baseline: estructura + SRS + código base |
| v1.0.1   | 2026-01-20 | fix: corrección hotfix pagos             |
| v1.1.0   | 2026-01-25 | feat: filtro por fecha + env seguro      |

## Estructura del repositorio

```
/docs/SRS/     → Requisitos del sistema
/docs/CM/      → Documentos de gestión de configuración
/src/          → Código fuente
/tests/        → Pruebas unitarias
/config/       → Configuración (solo ejemplos, sin secretos)
/.github/      → Plantillas de PR
CHANGELOG.md   → Historial de cambios por versión
CM_STATUS_REGISTER.md → Registro de estados de EC
```
