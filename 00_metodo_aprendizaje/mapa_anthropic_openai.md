# Mapa Anthropic -> OpenAI

Este repo usa el mapa publico de temas de cursos de Anthropic como inspiracion,
pero todo se practica con OpenAI, Python, FastAPI y Codex.

No se copia contenido del curso. Se traduce la habilidad al stack que vas a usar.

## Mapeo principal

| Tema tipo Anthropic | Adaptacion en este repo | Piezas |
| --- | --- | --- |
| Acceder a la API | OpenAI SDK + `.env` | 02-03 |
| Conversaciones multi-turn | Responses API con estado | 05 |
| System prompts/instructions | `instructions` y reglas de comportamiento | 04 |
| Temperature/modelos/tokens | control de modelo y longitud | 04 |
| Streaming | Responses streaming | 06 |
| Structured data | JSON validable para software | 07 |
| Prompt evaluation | datasets chicos + asserts + revision | 17 |
| Prompt engineering | claridad, ejemplos, restricciones | 04, 07, 17 |
| Tool use | function calling + ejecucion local | 08-09 |
| Multiple tools | tool registry del demo | 16-18 |
| Text edit tool | Codex sobre repos | 15 |
| Web search tool | queda fuera del primer demo operativo | despues |
| RAG/agentic search | busqueda local, documentos, reglas | 10-11 |
| Embeddings/BM25/multi-index | etapa posterior, si el demo lo pide | despues |
| Citations/PDF/image | no prioritario para stock/ventas inicial | despues |
| Prompt caching | optimizacion posterior | despues |
| Code execution/files | scripts Python + Codex | 02-18 |
| MCP tools/resources/prompts | contratos MCP aplicados a stock | 13-14 |
| Claude Code | Codex como colaborador en repo | 15 |
| Agents/workflows | workflow vs agente con tools | 16 |

## Prioridad para tu proyecto real

Primero:

- agent loop
- tools seguras
- prompt/instructions
- structured outputs
- FastAPI
- evals y guardrails

Despues:

- MCP
- RAG mas avanzado
- observabilidad
- prompt caching
- integraciones externas

Mas tarde:

- PDFs, imagenes, computer use, Bedrock/Vertex
- MCP avanzado
- busqueda multi-indice

## Regla practica

Cada tema entra al repo solo si ayuda a responder esta pregunta:

```text
Como mejora el asistente de stock, ventas o cotizaciones?
```
