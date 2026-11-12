# NEXT

_Actualizado: 2026-11-12_

## Dónde quedé
- Scaffolding commiteado en `main` (protegida: todo cambio va por rama y PR).
- ADR 0002 (cliente de Postgres) y 0003 (embeddings) quedan `proposed`:
  se deciden al empezar M1.
- M0, ejercicio 1 (modelo de acceso) mergeado en `main`: empresa ficticia,
  áreas, roles y ADR 0005.
- GitHub configurado para tracking: wiki y projects desactivados, topics,
  milestones M0–M6 (espejo del roadmap), labels `area:`, `task` y
  `security`, y reporte privado de vulnerabilidades activado.
- PRs abiertas: issue forms + sección "Roadmap and tracking"
  (`chore/issue-forms-and-tracking`) y `SECURITY.md`
  (`docs/security-policy`).

## Próximo paso concreto
- Revisar y mergear las dos PRs.
- Opcional: abrir un issue `task` por cada criterio pendiente de M0,
  asignado al milestone M0.
- M0, ejercicio 2: el chequeo automático del corpus y del dataset (ver
  roadmap M0). Es código, lo escribo yo: campos obligatorios, ids únicos,
  `area` y roles válidos, regla de `employee` del ADR 0005, `source_ids`
  existentes y fuente visible para el rol de cada pregunta respondible.
- Después: generar los 30–50 documentos y las 30 preguntas (contenido,
  delegable).
