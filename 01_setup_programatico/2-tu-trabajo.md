# Pieza 01 - Mi contrato de aprendizaje

## Objetivo general

Quiero aprender a construir software con OpenAI desde codigo, usando Python y
FastAPI, mientras desarrollo una demo real conectada con mi proyecto
`python-from-zero-lab`.

La meta no es aprender IA de forma teorica ni solo usar ChatGPT como usuario.
La meta es entender como una aplicacion real puede usar un modelo para
interpretar lenguaje humano, pedir tools seguras y operar sobre un sistema.

## Proyecto guia

El proyecto guia es un gestor de stock, ventas y cotizaciones.

Problemas actuales:

- cargar mucho stock manualmente
- mirar movimientos manualmente
- hacer cambios de stock manuales
- desactivar muchos productos a mano
- vender manualmente
- cotizar manualmente

Primer demo que quiero construir:

- cargar stock en lote interactuando con un agente
- consultar movimientos y encontrar problemas rapido
- hacer ajustes de stock con ayuda del agente
- desactivar productos con validacion
- vender con agente
- cotizar con agente

## Idea central del sistema

El humano escribe en lenguaje natural. El agente interpreta lo que el humano
quiere hacer. Python y FastAPI ejecutan la logica real del sistema.

Formula mental:

```text
mensaje humano -> OpenAI interpreta -> JSON/tool -> Python valida -> sistema ejecuta -> respuesta
```

OpenAI no debe ser la fuente de verdad. El modelo puede razonar, redactar y
pedir acciones, pero la verdad del sistema vive en Python, datos, validaciones,
logs, stock, ventas y reglas de negocio.

## Rol de cada parte

### Yo como estudiante

Estoy aprendiendo como junior. Necesito una curva guiada, con practica real,
errores controlados y correcciones tecnicas.

Mi forma de avance esperada:

```text
1. leo y no entiendo
2. leo y rompo cosas
3. leo y entiendo un poco
4. leo y voy entendiendo, rompo menos
5. puedo explicar, modificar y verificar
```

Hoy me ubico cerca de la etapa 2. Por eso necesito consignas claras, practica
paso a paso y revision como profesor/tecnico.

### La IA como profesor/tecnico

Quiero usar la IA como herramienta de aprendizaje:

- explicar conceptos dificiles
- dar consignas concretas
- revisar codigo
- detectar errores de razonamiento
- pedirme que explique lo que hice
- conectarlo todo con una demo real

## Que quiero aprender

Quiero adaptar a OpenAI los temas principales de cursos orientados a Claude y
Anthropic, porque mi stack de trabajo usa OpenAI.

Temas principales:

- acceso a la API desde codigo
- uso de API keys y variables de entorno
- llamadas basicas al modelo
- conversaciones multi-turn
- instrucciones y prompts de sistema
- control de modelo, costo y longitud
- streaming
- salida estructurada en JSON
- evaluacion de prompts
- datasets de prueba
- grading con codigo o modelo
- prompt engineering
- uso de tools/function calling
- manejo de multiples tools
- conversaciones con tools
- RAG y busqueda sobre datos propios
- embeddings y busqueda lexical
- FastAPI como backend/API propia
- MCP: tools, resources y prompts
- Codex como herramienta de trabajo en repos
- workflows vs agentes
- evals, guardrails y observabilidad

## Prioridad de estudio

No todo tiene la misma prioridad para mi proyecto. El orden importante es:

1. OpenAI SDK y Responses API.
2. Structured outputs para convertir lenguaje humano en datos.
3. Tools/function calling para conectar el modelo con funciones Python.
4. FastAPI para exponer una API segura.
5. Workflows y agentes para decidir cuando usar pasos fijos o decision del modelo.
6. Evals y guardrails para medir si el sistema funciona y evitar errores.
7. RAG si necesito responder con reglas, documentos o datos propios.
8. MCP despues de entender tools y FastAPI.
9. Codex para trabajar mejor sobre repos reales.

## Temas que puedo dejar para mas adelante

Por ahora no son prioridad:

- Bedrock
- Vertex AI
- Computer Use
- PDFs e imagenes
- RAG avanzado
- MCP avanzado
- busqueda multi-indice
- integraciones reales con sistemas externos

Primero necesito entender bien el nucleo:

```text
agent loop + tools + policy + prompt + evals + FastAPI
```

## Relacion con arquitecturas de agentes comerciales

Tambien quiero entender el patron general de un agente comercial real aplicado
a un producto.

La idea importante es:

```text
el agente conversa y razona
el backend de integracion ejecuta side effects
las fuentes reales guardan la verdad
los evals y logs detectan regresiones
```

Prioridades para estudiar ese tipo de arquitectura, en terminos generales:

1. Flujo real de producto:
   entrada de datos -> backend de integracion -> sistema de negocio ->
   comunicacion con usuario -> accion final.
2. Contrato backend/agente:
   el agente no toca sistemas externos ni datos sensibles directo.
3. Agent loop:
   validaciones, permisos, modos de ejecucion, estados bloqueantes, policy,
   respuesta y revision humana cuando haga falta.
4. Tools:
   entender que tools consultan datos y cuales modifican estado.
5. Prompt y skills:
   tono humano, no inventar precios, links ni credenciales, no saltear
   etapas.
6. Evals y observabilidad:
   medir el agente desde su API o contrato interno, no desde integraciones
   externas reales.

## Criterio de pieza terminada

Una pieza esta terminada cuando:

- hice mi intento en el archivo correspondiente
- el codigo corre, o puedo defender el diseno si no hay codigo
- entiendo que problema resuelve
- puedo explicar entradas y salidas
- puedo nombrar al menos un caso que puede fallar
- puedo decir como lo verifique
- pedi correccion antes de avanzar

## Criterio de demo buena

La demo final tiene que ser entendible para otra persona. Debe mostrar:

- input humano
- intencion detectada
- JSON o tool usada
- validacion del sistema
- accion ejecutada
- cambio de stock/venta/cotizacion
- respuesta final
- caso de error controlado
- pruebas o evals basicos

Si alguien externo ve el repo, quiero que entienda que este no es solo un
ejercicio suelto: es un camino de aprendizaje aplicado a un producto real.
