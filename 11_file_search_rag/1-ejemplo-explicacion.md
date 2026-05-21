# Pieza 11 - File search y RAG

## Objetivo

Responder usando documentos propios.

## Concepto

RAG significa traer informacion relevante antes de responder.

La diferencia con la pieza anterior:

- antes buscabas simple en CSV
- ahora pensas en documentos mas grandes
- la busqueda trae fragmentos relevantes

## Formula

```text
pregunta -> buscar fragmentos -> responder usando solo esos fragmentos
```

## Tu problema

En `2-main.py`, primero simula RAG sin embeddings:

- lista de documentos cortos
- busqueda por palabra clave
- respuesta usando solo el documento encontrado

Despues lo conectamos a file search real.

## Transferencia al demo

RAG entra cuando las reglas ya no caben comodamente en un CSV o en codigo.

Ejemplos de documentos utiles:

- politica de descuentos
- reglas de desactivacion de productos
- guia de ajustes de stock
- condiciones de cotizacion

Regla de oro: si no aparece en los documentos encontrados, el asistente debe
decir que no tiene base suficiente.
