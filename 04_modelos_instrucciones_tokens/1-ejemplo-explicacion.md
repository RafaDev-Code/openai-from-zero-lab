# Pieza 04 - Modelos, instrucciones y tokens

## Objetivo

Controlar como responde el modelo desde codigo.

## Concepto

Una llamada tiene decisiones tecnicas:

- modelo
- instrucciones
- input
- limite de salida

Las instrucciones son reglas de comportamiento. No reemplazan la validacion.

## Formula

```python
response = client.responses.create(
    model=model,
    instructions="Responde para un principiante. Usa frases cortas.",
    input="Explica que es una venta.",
    max_output_tokens=120,
)
```

## Tu problema

En `2-main.py`, hace dos llamadas con el mismo input:

```text
Explica que significa descontar stock.
```

Una debe responder como tutor principiante.

La otra debe responder como tecnico de backend.

Imprimi ambas respuestas.

## Transferencia al demo

Las instrucciones definen comportamiento, pero no reemplazan reglas de sistema.

Ejemplos utiles para la demo:

- responder como vendedor claro y breve
- responder como tecnico cuando se revisa un error
- no inventar stock, precios ni productos
- pedir confirmacion antes de acciones riesgosas

Regla: el prompt orienta; Python valida.
