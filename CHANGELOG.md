# Changelog

Todas las versiones notables de este proyecto se documentan aquí.  
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).  
Versionado sigue [SemVer](https://semver.org/lang/es/).

---

## [Unreleased]

- Implementación completa de REQ-003 filtro por fecha (ISSUE-21)

---

## [v1.1.0] — 2026-01-25

### Added
- REQ-003: Placeholder para filtro de productos por fecha (ISSUE-21)
- `config/.env.example`: archivo ejemplo seguro para variables de entorno
- `.gitignore`: excluye `config/.env` y otros archivos sensibles
- `.github/pull_request_template.md`: plantilla de PR con trazabilidad obligatoria

### Fixed
- Eliminado `config/.env` del tracking de Git (secreto versionado por error)
- Corregido mensaje de commit no descriptivo `"update stuff"` → `"chore: remove secrets from repo, add env example (ISSUE-21)"`

### Changed
- SRS v1 actualizado con REQ-003 y RNF-003

---

## [v1.0.1] — 2026-01-20

### Fixed
- `fix: hotfix pagos 1% (ISSUE-20)` — corrección en lógica de cálculo de pagos
- CHANGELOG actualizado con entrada para esta versión

### Notes
- Commit original carecía de referencia ISSUE-xx; corregido retroactivamente en documentación

---

## [v1.0.0] — 2026-01-15

### Added
- Baseline: estructura del repositorio (`/docs`, `/src`, `/tests`, `/config`, `/.github`)
- `src/app.py`: implementación de `list_products()` y `add_product()`
- `tests/test_app.py`: pruebas unitarias para REQ-001 y REQ-002
- `docs/SRS/SRS_v1.md`: requisitos REQ-001, REQ-002, RNF-001, RNF-002
- `README.md`: descripción del proyecto y convenciones
- `CHANGELOG.md`: inicialización del registro de cambios

### Notes
- Tag `v1.0` eliminado (no cumplía SemVer); reemplazado por `v1.0.0`
- Tag `release-1.1` eliminado (formato inconsistente); reemplazado por `v1.1.0`
