# Ejercicios de entrevista: Backend

`no-contactar/` y `conversaciones-abandonadas/` son mini-servicios independientes en Python 3.11+ con FastAPI y pytest, organizados en capas (`domain`, `application`, `infrastructure`, `presentation`). Arrancan con sus tests en verde. `leer-y-trazar/` no se corre: se lee y se traza a mano.

| Ejercicio | Enunciado |
|---|---|
| `no-contactar/` | Ver `no-contactar/README.md` |
| `conversaciones-abandonadas/` | Ver `conversaciones-abandonadas/README.md` |
| `leer-y-trazar/` | Ver `leer-y-trazar/README.md` |

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
