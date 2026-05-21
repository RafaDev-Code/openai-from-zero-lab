# Ruta

La ruta esta ordenada para aprender construyendo. Cada pieza suma una capacidad
al mismo producto final: un asistente operativo para stock, ventas y
cotizaciones.

```text
fundamentos OpenAI -> datos y tools -> API propia -> contratos -> agente -> evals
```

## Norte del proyecto

El agente no es la fuente de verdad. La fuente de verdad es tu sistema:

```text
productos + stock + movimientos + ventas + cotizaciones + reglas
```

El agente conversa, interpreta y pide tools. Las acciones reales pasan por
funciones propias o por FastAPI.

El detalle de la demo esta en
[00_metodo_aprendizaje/proyecto_demo.md](00_metodo_aprendizaje/proyecto_demo.md).

## Fases

| Fase | Piezas | Meta | Demo acumulada |
| --- | --- | --- | --- |
| 0 | 01 | contrato de aprendizaje | definir que vamos a construir y como se corrige |
| 1 | 02-07 | OpenAI desde Python | extraer pedidos y responder con JSON validable |
| 2 | 08-12 | tools, datos y FastAPI | consultar stock, vender, cotizar y exponer endpoints |
| 3 | 13-15 | contratos, MCP y Codex | disenar tools seguras y trabajar mejor sobre repos |
| 4 | 16-18 | agente, evals y demo | asistente operativo verificable |

## Tabla de piezas

| Pieza | Concepto | Lo que aprendes | Entregable |
| --- | --- | --- | --- |
| 01 | setup programatico | contrato estudiante/IA y problema real | contrato de aprendizaje aplicado |
| 02 | OpenAI SDK | entorno, `.env`, cliente y modelo | script que lee configuracion |
| 03 | Responses API | primera llamada desde Python | respuesta simple sobre stock |
| 04 | instrucciones y tokens | controlar tono, rol y longitud | dos respuestas para perfiles distintos |
| 05 | conversacion y estado | sostener contexto entre turnos | mini dialogo sobre gestor de stock |
| 06 | streaming | mostrar avance en vivo | guia operativa por streaming |
| 07 | salida estructurada | pedir JSON validable | extractor de pedido |
| 08 | function calling manual | tools sin magia | funciones locales de stock |
| 09 | function calling OpenAI | modelo pide una tool, Python ejecuta | consulta de stock con tool |
| 10 | CSV/contexto local | usar datos propios sin RAG | respuesta usando productos locales |
| 11 | RAG simple | buscar fragmentos antes de responder | respuesta basada en reglas/documentos |
| 12 | FastAPI wrapper | exponer backend propio | `/health` y `/extraer-pedido` |
| 13 | MCP intro | tools/resources/prompts como contrato | diseno MCP para stock |
| 14 | MCP server minimo | contratos de tools | especificacion de tools criticas |
| 15 | Codex en repos | pedir cambios verificables | prompts de trabajo sobre repos |
| 16 | workflows/agentes | distinguir pasos fijos de decision agente | workflow de pedido |
| 17 | evals/guardrails | medir y bloquear errores | dataset chico de pruebas |
| 18 | proyecto final | integrar todo | asistente operativo demo |

## Como estudiar cada pieza

Usa este ciclo:

```text
recordar -> leer -> implementar -> ejecutar -> explicar -> corregir -> repasar
```

Antes de abrir el ejemplo, responde:

- que creo que resuelve esta pieza
- donde aparece en la demo final
- que error peligroso podria cometer

Despues de terminar, responde:

- cual fue el input
- cual fue el output
- que valide
- que caso rompe mi solucion
- que cambiaria si esto fuera para produccion

## Regla de avance

No avances si solo "viste" el tema. Avanzas cuando podes hacer estas 4 cosas:

- ejecutar o presentar el entregable
- explicar la formula mental sin mirar
- nombrar al menos 2 fallos posibles
- decir como se probaria

## Repasos espaciados

Cada pieza entra en tres repasos:

```text
D+1: explicar de memoria la formula
D+3: rehacer la pieza o una variante chica
D+7: conectarla con otra pieza del proyecto
```

La agenda esta en
[00_metodo_aprendizaje/checkpoints.md](00_metodo_aprendizaje/checkpoints.md).
