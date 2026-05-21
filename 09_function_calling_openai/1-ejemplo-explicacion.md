# Pieza 09 - Function calling con OpenAI

## Objetivo

Dejar que el modelo pida una funcion propia.

## Concepto

El modelo no ejecuta tus funciones.

El modelo pide una tool. Tu codigo decide si la ejecuta y le devuelve el
resultado.

## Formula

```text
usuario -> modelo pide tool -> Python ejecuta -> modelo responde
```

## Ejemplo mental

Usuario:

```text
Tenemos cafe?
```

Tool pedida:

```text
consultar_stock(producto="cafe")
```

Resultado local:

```json
{"producto": "cafe", "stock": 8}
```

## Tu problema

En `2-main.py`, conecta una tool `consultar_stock`.

Debe existir:

- stock local en Python
- definicion de tool para el modelo
- ejecucion local cuando el modelo la pida
- respuesta final al usuario

No agregues ventas todavia.

## Transferencia al demo

Esta pieza muestra el contrato mas importante:

```text
el modelo puede pedir
tu codigo decide
tu codigo ejecuta
tu codigo devuelve resultado
```

El modelo no debe modificar stock directamente. Primero aprende a consultar.

## Criterio de terminado

La pieza esta bien si podes mostrar:

- el mensaje del usuario
- la tool que el modelo pidio
- los argumentos de la tool
- el resultado local
- la respuesta final
