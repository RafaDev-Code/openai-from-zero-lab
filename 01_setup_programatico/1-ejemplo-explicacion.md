# Pieza 01 - Setup programatico

## Objetivo

Definir como vas a aprender OpenAI desde codigo.

## Concepto

Esta ruta no es sobre "usar mejor ChatGPT".

Es sobre construir software que usa OpenAI.

Vas a trabajar con:

- Python
- OpenAI SDK
- Responses API
- JSON validable
- funciones propias como tools
- documentos como contexto
- APIs propias
- MCP
- Codex
- Agents SDK
- evals

## Formula mental

```text
entrada -> codigo -> llamada OpenAI -> validacion -> accion -> verificacion
```

## Ejemplo

Problema:

```text
Un cliente escribe "quiero 3 cafes para hoy".
```

Flujo programatico:

```text
mensaje -> extraer JSON -> consultar stock -> decidir -> responder -> guardar venta
```

## Tu problema

En `2-tu-trabajo.md`, escribi:

- que queres poder programar al final
- que partes te interesan mas: API, tools, RAG, MCP, agentes, evals
- que cosas de uso humano dejamos afuera por ahora
- como vas a saber que una pieza esta terminada

## Sintesis del contrato

Tu respuesta original queda como fuente. La sintesis operativa esta en
`3-contrato-aprendizaje.md`.

Antes de avanzar a la pieza 02, tenes que poder decir:

- cual es la demo final
- que rol cumple OpenAI
- que rol cumple Python/FastAPI
- que acciones no debe ejecutar el agente sin validacion
