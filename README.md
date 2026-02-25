# API Inventario (mini)

**Autor:** Juan Lucumi  
**Materia:** Gestión de Configuración de Software  
**Semana:** 5 — Actividad 4  

Repositorio desarrollado como práctica de auditoría y control 
de versiones. Se simuló un repo con errores reales y se corrigió 
con evidencia trazable.

- Endpoints simulados: `GET /products`, `POST /products`

## Cómo ejecutar (simulado)

No se requiere despliegue real. Este repositorio se usa para GCS.
```bash
pytest tests/
```

## Convención

- Commits: `chore/docs/feat/fix` + referencia `ISSUE-xx`
- Versiones: SemVer (`vMAJOR.MINOR.PATCH`)

## Historial de versiones

| Versión | Fecha      | Descripción                              |
|---------|------------|------------------------------------------|
| v1.0.0  | 2026-02-25 | Baseline: estructura + SRS + código base |
| v1.0.1  | 2026-02-25 | fix: corrección hotfix pagos             |
| v1.1.0  | 2026-02-25 | feat: filtro por fecha + env seguro      |