# Plan de sesiones

Usalo como guia flexible. Si una pieza cuesta, se queda mas tiempo ahi. El
objetivo no es ir rapido; es construir dominio.

## Sesion 1: contrato y entorno

Piezas:

- 01
- 02

Entregable:

- contrato entendido
- `.env` preparado
- script que imprime modelo

Repaso:

- explicar por que la API key no va en codigo

## Sesion 2: primera llamada y control de respuesta

Piezas:

- 03
- 04

Entregable:

- primera llamada real
- dos respuestas con instrucciones distintas

Repaso:

- diferenciar prompt/instructions de validacion real

## Sesion 3: conversacion y streaming

Piezas:

- 05
- 06

Entregable:

- conversacion encadenada
- respuesta por streaming

Repaso:

- que cosas pueden vivir en contexto y que cosas deben guardarse en datos

## Sesion 4: JSON para software

Pieza:

- 07

Entregable:

- extractor de pedido

Repaso:

- 5 mensajes distintos extraidos a JSON

## Sesion 5: tools locales

Piezas:

- 08
- 09

Entregable:

- consultar stock sin OpenAI
- consultar stock con tool pedida por modelo

Repaso:

- explicar quien decide y quien ejecuta

## Sesion 6: datos propios y reglas

Piezas:

- 10
- 11

Entregable:

- productos desde CSV
- reglas/documentos buscados antes de responder

Repaso:

- cuando alcanza CSV y cuando conviene RAG

## Sesion 7: FastAPI

Pieza:

- 12

Entregable:

- `/health`
- `/extraer-pedido`

Repaso:

- request, schema, validacion, response

## Sesion 8: contratos de sistema

Piezas:

- 13
- 14

Entregable:

- tools/resources/prompts disenados
- contratos de tools criticas

Repaso:

- distinguir tools de lectura y tools de escritura

## Sesion 9: Codex sobre repos

Pieza:

- 15

Entregable:

- 3 pedidos buenos para Codex

Repaso:

- objetivo, alcance, archivos, verificacion

## Sesion 10: workflows y agente

Pieza:

- 16

Entregable:

- workflow de pedido

Repaso:

- decidir que parte es fija y que parte requiere agente

## Sesion 11: evals y guardrails

Pieza:

- 17

Entregable:

- 5 casos de prueba
- guardrails minimos

Repaso:

- explicar un bug que los evals detectarian

## Sesion 12: demo integrada

Pieza:

- 18

Entregable:

- cotizacion
- venta
- ajuste de stock
- errores controlados

Repaso:

- demo completa explicada paso a paso
