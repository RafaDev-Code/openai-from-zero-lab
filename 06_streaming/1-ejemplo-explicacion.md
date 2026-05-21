# Pieza 06 - Streaming

## Objetivo

Mostrar una respuesta mientras se genera.

## Concepto

Streaming evita esperar a que termine toda la respuesta.

Sirve para interfaces de chat, CLI y dashboards donde el usuario necesita ver
avance.

## Formula

```python
with client.responses.stream(
    model=model,
    input="Escribi 5 pasos para ordenar un deposito.",
) as stream:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
```

## Tu problema

En `2-main.py`, pedi por streaming:

```text
Dame una guia de 6 pasos para revisar stock antes de abrir el local.
```

La salida tiene que aparecer en vivo.

## Transferencia al demo

Streaming sirve para experiencia de usuario.

En la demo puede usarse para:

- mostrar una explicacion operativa mientras se genera
- responder en chat sin hacer esperar
- dar progreso cuando el agente analiza movimientos

No cambia la logica de negocio. Solo cambia como se muestra la salida.
