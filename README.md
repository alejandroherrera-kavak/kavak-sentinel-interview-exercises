# Ejercicios de entrevista: Backend

Cada carpeta es un mini-servicio independiente en Python 3.11+ con FastAPI y pytest, organizado en capas (`domain`, `application`, `infrastructure`, `presentation`). Arrancan con sus tests en verde.

| Ejercicio | Enunciado |
|---|---|
| `no-contactar/` | Ver `no-contactar/README.md` |
| `conversaciones-abandonadas/` | Ver `conversaciones-abandonadas/README.md` |

## Cómo correr un ejercicio

Necesitas [uv](https://docs.astral.sh/uv/). Dentro de la carpeta del ejercicio:

```bash
uv run pytest -q                                   # tests
uv run uvicorn app.presentation.api:app --reload   # API en http://localhost:8000
```

## Reglas

- Puedes usar el asistente de IA que prefieras. Nos interesa cómo piensas y cómo trabajas con la herramienta.
- Piensa en voz alta y comparte la pantalla con los prompts visibles.
- Todo el código que entregues es tuyo, lo hayas escrito tú o la IA. Te pediremos que lo expliques.
- Pregunta lo que necesites. No hay preguntas tontas.
