# No contactar

Soporte necesita poder marcar a un cliente como "no contactar" para que el bot deje de escribirle. Impleméntalo en este servicio.

## Correr

```bash
uv run pytest -q
uv run uvicorn app.presentation.api:app --reload
curl -X POST localhost:8000/messages -H 'content-type: application/json' -d '{"customer_id":"c1","text":"hola"}'
```
