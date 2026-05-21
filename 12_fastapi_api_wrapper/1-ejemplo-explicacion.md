# Pieza 12 - FastAPI wrapper

## Objetivo

Exponer una mini API que use OpenAI por atras.

## Concepto

Una app real no llama OpenAI desde cualquier lado.

Normalmente tenes tu backend:

```text
cliente -> FastAPI -> OpenAI -> FastAPI -> cliente
```

El backend guarda la API key y valida entradas.

## Formula

```python
@app.post("/extraer-pedido")
def extraer_pedido(payload):
    ...
```

## Tu problema

En `2-main.py`, crea una app FastAPI con:

- `GET /health`
- `POST /extraer-pedido`

Primero `POST /extraer-pedido` puede devolver una respuesta fija.

Despues le conectamos OpenAI.

## Como probar

```bash
uvicorn 2-main:app --reload
```

## Transferencia al demo

FastAPI es el puente entre agente y sistema.

En una version real, el agente no toca archivos ni base de datos directamente.
Llama a endpoints o tools que validan:

```text
POST /extraer-pedido
POST /cotizar
POST /ventas
POST /stock/ajustes
GET /stock/{producto}
```

En esta pieza solo implementas lo minimo. La idea es aprender la forma:

```text
request -> schema -> validacion -> respuesta JSON
```

## Criterio de terminado

La pieza esta bien si podes:

- levantar el servidor
- abrir `/health`
- mandar un POST a `/extraer-pedido`
- explicar por que la API key queda en backend
- explicar que validaciones agregarias antes de vender
