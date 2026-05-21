# Pieza 13 - MCP intro

## Objetivo

Entender MCP como sistema, no como moda.

## Concepto

MCP significa Model Context Protocol.

Sirve para estandarizar como una app o agente accede a herramientas y datos.

Piezas:

- cliente MCP
- servidor MCP
- tools
- resources
- prompts

## Formula mental

```text
modelo/app -> cliente MCP -> servidor MCP -> tool o resource
```

## Tu problema

En `2-tu-trabajo.md`, disena un servidor MCP para tu gestor de stock.

Debe tener:

- 3 tools
- 2 resources
- 1 prompt
- riesgo principal de cada tool

## Transferencia al demo

MCP no es prioridad antes de entender tools y FastAPI.

En esta pieza solo disenas el contrato. La pregunta es:

```text
Si manana quisiera exponer mi gestor de stock como servidor MCP,
que tools, resources y prompts tendria?
```
