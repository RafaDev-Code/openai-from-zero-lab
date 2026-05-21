# Contrato de aprendizaje

Este archivo sintetiza tu `2-tu-trabajo.md` en un plan operativo.

## Objetivo

Aprender OpenAI programaticamente construyendo una demo seria sobre el proyecto
de Python:

```text
gestor de stock y ventas -> asistente operativo con IA
```

Mientras avanzas, tambien tenes que entender FastAPI y como una app real expone
funciones seguras para que un agente las use.

## Que vamos a construir

Primer demo:

- cargar stock en lote con agente
- consultar movimientos y detectar problemas
- ajustar stock con motivo
- desactivar productos
- registrar ventas
- generar cotizaciones

## Que NO vamos a hacer al principio

- integraciones reales con sistemas externos
- mensajeria real
- RAG avanzado si todavia alcanza CSV o busqueda simple
- MCP avanzado antes de entender tools y FastAPI

## Dinamica

Vos trabajas como estudiante que construye.

Yo trabajo como profesor/tecnico que:

- explica el concepto
- revisa el codigo
- pide justificacion
- detecta riesgos
- te hace practicar de memoria
- conecta cada pieza con la demo final

## Criterio de pieza terminada

Una pieza esta terminada si:

- el archivo `2-*` tiene tu intento
- lo ejecutaste o lo podes defender si es diseno
- podes explicar input, output y validacion
- sabes nombrar un caso que falla
- pediste correccion

## Criterio de demo buena

La demo es buena si una persona tecnica puede ver:

- datos iniciales
- mensaje del usuario
- extraccion o decision del modelo
- tool ejecutada
- validacion del sistema
- cambio de estado
- log/movimiento
- respuesta final
- prueba/eval

## Norte tipo agente comercial

Un agente comercial real sirve como referencia conceptual:

```text
agente conversa y razona
backend de integracion ejecuta side effects
fuentes reales guardan la verdad
evals y logs cuidan regresiones
```

En este repo la version chica es:

```text
OpenAI -> tools Python -> FastAPI -> datos de stock/ventas -> evals
```
