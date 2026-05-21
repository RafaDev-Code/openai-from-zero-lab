# Pieza 14 - MCP server minimo

## Objetivo

Disenar el contrato de un servidor MCP chico.

## Concepto

Antes de programar MCP, defini contratos.

Una tool clara tiene:

- nombre
- descripcion
- parametros
- salida
- errores

## Formula

```text
tool clara = nombre + parametros + salida + errores
```

## Tu problema

En `2-tu-trabajo.md`, escribi el contrato completo para estas tools:

- `consultar_stock`
- `registrar_venta`
- `listar_productos`

No programes todavia.

## Transferencia al demo

Un contrato claro evita que el agente use una tool de forma ambigua.

Para cada tool agrega:

- si modifica datos o solo consulta
- que permisos requiere
- que errores puede devolver
- que debe loguear
