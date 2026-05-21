# Pieza 16 - Agents SDK y workflows

## Objetivo

Entender cuando usar workflow y cuando agente.

## Concepto

Workflow:

```text
pasos conocidos de antemano
```

Agente:

```text
el modelo decide pasos usando tools
```

No todo necesita agente.

## Formula

```text
si los pasos son fijos -> workflow
si los pasos dependen del caso -> agente
```

## Tu problema

En `2-main.py`, modela sin SDK real:

- funcion `consultar_stock`
- funcion `registrar_venta`
- funcion `workflow_pedido(mensaje)`

El workflow puede tener pasos fijos.

Despues lo pasamos al Agents SDK.

## Transferencia al demo

Primero pensa como workflow. Despues decidimos si hace falta agente.

Ejemplo workflow:

```text
extraer pedido -> consultar stock -> calcular total -> registrar venta -> responder
```

Ejemplo agente:

```text
usuario pide algo ambiguo -> decidir si cotizar, vender, ajustar o pedir datos
```

## Criterio de terminado

La pieza esta bien si podes justificar:

- que pasos son fijos
- donde aparece decision
- que tools usaria un agente
- que accion requiere confirmacion humana
