# Pieza 18 - Proyecto final asistente operativo

## Objetivo

Unir Python + OpenAI en una app chica y explicable.

## Relacion con python-from-zero-lab

El TP final de Python es el motor:

```text
productos + stock + ventas
```

Este TP final agrega la capa OpenAI:

```text
mensaje cliente -> extraer pedido -> consultar stock -> registrar venta -> responder
```

## Concepto

El proyecto final tiene que poder explicar:

- input del usuario
- estructura JSON
- tool llamada
- validacion
- actualizacion de stock
- respuesta final
- casos de error

## Tu problema

En `2-main.py`, arma la primera version integrada:

- productos en memoria
- ventas en memoria
- extractor de pedido
- consulta de stock
- registro de venta
- respuesta final

Puede empezar sin OpenAI. Despues se conecta pieza por pieza.

## Alcance de la primera demo

La primera demo debe mostrar 3 flujos completos:

- cotizar pedido
- registrar venta con descuento de stock
- ajustar stock con motivo

Y 2 errores controlados:

- producto inexistente
- stock insuficiente

## Arquitectura esperada

```text
datos en memoria
funciones de dominio
extractor de intencion
workflow/agente
respuesta final
evals chicos
```

Despues se puede mover a FastAPI:

```text
CLI o chat -> FastAPI -> servicio de stock/ventas -> OpenAI/tools -> respuesta
```

## Criterio de demo lista

La demo esta lista si podes mostrar:

- estado inicial
- input humano
- decision o JSON extraido
- tool usada
- cambio de stock/venta/cotizacion
- respuesta final
- pruebas basicas pasando
