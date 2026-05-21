# Pieza 05 - Conversacion y estado

## Objetivo

Sostener contexto entre llamadas.

## Concepto

Una app conversacional necesita recordar el hilo.

Con Responses API podes encadenar una respuesta con otra usando el id anterior.

## Formula

```python
primera = client.responses.create(
    model=model,
    input="Estoy armando un sistema de stock.",
)

segunda = client.responses.create(
    model=model,
    previous_response_id=primera.id,
    input="Dame el primer dato que deberia guardar por producto.",
)
```

## Tu problema

En `2-main.py`, hace dos llamadas encadenadas:

1. Decile al modelo que estas construyendo un gestor de stock.
2. Pedile que proponga 3 campos para una venta.

Imprimi las dos respuestas con titulos.

## Transferencia al demo

El estado importa cuando una conversacion tiene varios pasos:

```text
cliente pide cotizacion
despues cambia cantidad
despues confirma compra
```

La app tiene que saber que "confirmo" se refiere al pedido anterior. Aun asi,
los datos criticos deben quedar estructurados en tu sistema, no solo en memoria
del modelo.
