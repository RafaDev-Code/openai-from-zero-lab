# Pieza 03 - Responses API basico

## Objetivo

Hacer la primera llamada real a OpenAI desde Python.

## Concepto

La Responses API recibe un input y devuelve una respuesta del modelo.

## Formula

```python
response = client.responses.create(
    model=model,
    input="Explica que es una API en una frase.",
)

print(response.output_text)
```

## Tu problema

En `2-main.py`, hace un script que:

- cree un cliente OpenAI
- use `OPENAI_MODEL`
- pregunte que es stock en lenguaje simple
- imprima solo el texto final

## Como probar

```bash
python3 2-main.py
```

## Transferencia al demo

Esta es la primera vez que Python le pide razonamiento o redaccion al modelo.

Todavia no hay tools ni stock real. Solo estas comprobando:

```text
Python -> OpenAI -> texto -> Python imprime
```

Despues esa misma forma se usa para redactar respuestas de cotizacion, errores
de stock y mensajes para cliente.
