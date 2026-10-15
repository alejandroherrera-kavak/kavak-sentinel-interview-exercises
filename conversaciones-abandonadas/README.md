# Conversaciones abandonadas

Sentinel levanta una flag de "abandono" cuando un cliente lleva más de 24 horas sin respuesta. Implementa el caso de uso `DetectAbandonedConversations` para que el endpoint `GET /conversations/abandoned` devuelva esas conversaciones. Añade los tests que consideres.

## Correr

```bash
uv run pytest -q
uv run uvicorn app.presentation.api:app --reload
curl 'localhost:8000/conversations/abandoned?hours=24'
```
