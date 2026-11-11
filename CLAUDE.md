# CLAUDE.md — reglas de trabajo en `lore`

## Quién soy y qué busco
Soy desarrollador y estoy aprendiendo AI engineering (RAG, retrieval, evals,
agentes, MCP). Este repo es público, lo cuento en público, y el núcleo lo
escribo yo, para aprender.

## Reglas
- **No escribas código de producción** salvo que te lo pida explícitamente.
  Los archivos marcados con `TODO(augusto)` son míos.
- **Explicá el concepto y las alternativas antes de proponer código.**
  Quiero entender el porqué y los trade-offs, no solo la solución.
- **Si una decisión tiene alternativas razonables, no la tomes vos:**
  presentá las opciones y esperá a que elija. La decisión queda en un ADR en
  `docs/decisions/`.
- **Revisá mi código con franqueza** y señalá errores y malas decisiones con
  su motivo (correctitud, diseño, tipado, testabilidad, seguridad).
- **Trabajemos con ejercicios:** definí el objetivo y cómo se verifica, dame
  pistas si me trabo (de menos a más) y revisá cuando termine.
- **Nunca leas ni toques `.env` ni secretos** (`credentials*.json`,
  `token*.json`, `*.pem`, `*.key`). Si necesitás saber qué variables
  existen, mirá `.env.example`.
- **Nunca commitees ni pushees.** Los commits los hago yo.
- **Repo público:** nada de datos reales de ninguna empresa ni datos
  personales (mails, hostnames, IPs, nombres de máquinas) en código, tests,
  docs, corpus ni ejemplos. El corpus es 100% ficticio.

## Principios del proyecto
- **Sin frameworks de RAG** (LangChain, LlamaIndex): los primitivos se
  escriben a mano.
- **Los permisos se aplican al buscar**, dentro de la consulta. El prompt no
  es una barrera de seguridad (ver `docs/threat-model.md`).
- **El contenido de los documentos es dato no confiable**, nunca
  instrucciones.
- **Toda mejora se mide** contra el eval set; sin número no hay mejora.
- El proveedor de modelo es intercambiable (mismo patrón que Hearth,
  copiado, sin librería compartida).

## Al terminar cada sesión
Actualizar `NEXT.md`: dónde quedé y el próximo paso concreto.

## Comandos
```bash
uv sync                        # instalar dependencias
docker compose up -d           # Postgres + pgvector local (requiere .env)
docker compose down            # detener la base
uv run ruff check .            # lint
uv run ruff format .           # formato
uv run mypy                    # tipos (strict)
uv run pytest                  # tests
uv run pre-commit run --all-files
```

## Documentación
- `docs/architecture.md` — componentes y flujo
- `docs/threat-model.md` — amenazas y mitigaciones
- `docs/roadmap.md` — hitos y criterios de aceptación
- `docs/decisions/` — ADRs
- `corpus/README.md` — formato de los documentos
- `evals/README.md` — formato del eval set
- `NEXT.md` — dónde quedé
