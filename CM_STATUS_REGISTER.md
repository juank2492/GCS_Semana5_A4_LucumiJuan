# CM_STATUS_REGISTER.md
# Registro de Estados de Configuración — API Inventario

> Proyecto: API Inventario (mini) | Semana 5, Actividad 4  
> Responsable del registro: Estudiante GCS  
> Última actualización: 2026-01-25

---

## Leyenda de estados

| Estado         | Descripción                                              |
|----------------|----------------------------------------------------------|
| Registrado     | EC identificado, pendiente de revisión                   |
| En revisión    | Bajo análisis o auditoría                                |
| Aprobado       | Revisado y aceptado por responsable                      |
| Baselined      | Incluido en una línea base formal (tag/release)          |
| En implementación | Siendo modificado activamente                         |
| Integrado      | Fusionado al rama principal mediante PR/MR               |
| Verificado     | Pruebas ejecutadas satisfactoriamente                    |
| Liberado       | Publicado en release oficial                             |
| Retirado       | Fuera de uso, reemplazado o eliminado                    |

---

## Tabla de Elementos de Configuración (EC)

| EC-ID | Elemento de Configuración              | Tipo    | Versión / Ref          | Estado     | Responsable | Evidencia                                      |
|------:|----------------------------------------|---------|------------------------|------------|-------------|------------------------------------------------|
| EC-01 | `docs/SRS/SRS_v1.md`                   | Doc     | v1.1 / tag v1.1.0      | Baselined  | Analista    | commit `docs: update SRS v1.1 (ISSUE-21)` + tag v1.1.0 |
| EC-02 | `src/app.py`                           | Code    | SHA: `abc1234`         | Integrado  | Dev         | PR #2 → main; pruebas en EC-03                 |
| EC-03 | `tests/test_app.py`                    | Test    | SHA: `def5678`         | Verificado | QA          | pytest 4/4 passed; captura en informe PDF      |
| EC-04 | `CHANGELOG.md`                         | Doc     | v1.1.0 / tag v1.1.0    | Aprobado   | PM          | commit `docs: update CHANGELOG v1.1.0` + release notes |
| EC-05 | `.gitignore`                           | Config  | SHA: `ghi9012`         | Aprobado   | DevOps      | commit `chore: remove secrets from repo, add env example (ISSUE-21)` |
| EC-06 | `config/.env.example`                  | Config  | SHA: `ghi9012`         | Integrado  | DevOps      | commit `chore: remove secrets from repo (ISSUE-21)` |
| EC-07 | `.github/pull_request_template.md`     | Process | SHA: `jkl3456`         | Aprobado   | Líder       | commit `chore: add PR template (ISSUE-21)`     |
| EC-08 | `README.md`                            | Doc     | v1.0.0 / tag v1.0.0    | Baselined  | Equipo      | tag v1.0.0 + release notes en GitHub           |
| EC-09 | `config/.env` (RETIRADO)               | Config  | —                      | Retirado   | DevOps      | `git rm --cached config/.env` (ISSUE-21); secreto nunca debió versionarse |
| EC-10 | Tag `v1.0` (RETIRADO)                  | Tag     | —                      | Retirado   | DevOps      | `git push origin :refs/tags/v1.0`; reemplazado por `v1.0.0` |
| EC-11 | Tag `release-1.1` (RETIRADO)           | Tag     | —                      | Retirado   | DevOps      | `git push origin :refs/tags/release-1.1`; reemplazado por `v1.1.0` |
| EC-12 | `docs/CM/CM_STATUS_REGISTER.md`        | Doc     | v1.0 / tag v1.1.0      | Liberado   | PM          | Este documento; commit `docs: add CM status register (ISSUE-21)` |

---

## Resumen de tags/releases

| Tag     | Fecha      | Descripción                               | Estado   |
|---------|------------|-------------------------------------------|----------|
| v1.0    | —          | ❌ Tag inválido (no SemVer)               | Retirado |
| release-1.1 | —      | ❌ Tag inválido (formato inconsistente)   | Retirado |
| v1.0.0  | 2026-01-15 | ✅ Baseline formal                        | Liberado |
| v1.0.1  | 2026-01-20 | ✅ Hotfix pagos                           | Liberado |
| v1.1.0  | 2026-01-25 | ✅ Feature filtro + corrección secretos   | Liberado |

---

## Líneas base definidas

| Baseline | Tag     | Componentes incluidos                                    |
|----------|---------|----------------------------------------------------------|
| BL-01    | v1.0.0  | SRS v1, app.py, test_app.py, README.md, CHANGELOG.md    |
| BL-02    | v1.1.0  | BL-01 + SRS v1.1, .gitignore, .env.example, PR template, CM_STATUS_REGISTER.md |
