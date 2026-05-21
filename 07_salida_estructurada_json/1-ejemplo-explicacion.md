# Pieza 07 - Salida estructurada JSON

## Objetivo

Pedir respuestas que una app pueda validar.

## Concepto

Texto libre es comodo para leer.

JSON es mejor para software.

Una app necesita campos estables:

```json
{
  "producto": "cafe",
  "cantidad": 3,
  "urgente": true
}
```

## Formula

```text
mensaje humano -> modelo -> JSON -> validacion -> accion
```

## Tu problema

En `2-main.py`, pedi al modelo que extraiga de este mensaje:

```text
Hola, necesito 3 paquetes de cafe para hoy. Si no hay, avisame.
```

Campos:

- producto
- cantidad
- urgente
- duda_del_cliente

Imprimi el JSON resultante.

## Transferencia al demo

Esta pieza es la puerta entre lenguaje humano y software.

Sin JSON validable, el sistema no puede saber con seguridad si el usuario quiere
vender, cotizar, cargar stock o hacer un ajuste.

Formula aplicada:

```text
mensaje humano -> intencion + datos -> validacion -> siguiente accion
```

## Criterio de terminado

La pieza esta bien si podes explicar:

- que campos son obligatorios
- que haces si falta cantidad
- que haces si el producto no existe
- por que no conviene registrar una venta desde texto libre
