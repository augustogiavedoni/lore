# NEXT

_Actualizado: 2026-11-11_

## Dónde quedé
- Scaffolding commiteado en `main` (protegida: todo cambio va por rama y PR).
- ADR 0002 (cliente de Postgres) y 0003 (embeddings) quedan `proposed`:
  se deciden al empezar M1.
- M0, ejercicio 1 (modelo de acceso) terminado en la rama
  `docs/m0-access-model`, pendiente de commit y PR:
  - `corpus/README.md`: empresa ficticia (Corvalia), 6 áreas, 6 roles de
    usuario, matriz rol × área, excepciones y regla para decidir
    `allowed_roles`.
  - ADR 0005: los documentos para toda la empresa usan el rol base
    `employee`; una función de roles efectivos lo agrega a cada rol.
  - `evals/examples.jsonl` alineado con los roles nuevos.

## Próximo paso concreto
- Commitear y abrir el PR de `docs/m0-access-model`.
- M0, ejercicio 2: el chequeo automático del corpus y del dataset (ver
  roadmap M0). Es código, lo escribo yo: campos obligatorios, ids únicos,
  `area` y roles válidos, regla de `employee` del ADR 0005, `source_ids`
  existentes y fuente visible para el rol de cada pregunta respondible.
- Después: generar los 30–50 documentos y las 30 preguntas (contenido,
  delegable).
