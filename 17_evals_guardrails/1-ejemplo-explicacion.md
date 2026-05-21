# Pieza 17 - Evals y guardrails

## Objetivo

Medir calidad antes de confiar.

## Concepto

Una demo que funciona una vez no alcanza.

Necesitas casos de prueba.

Eval:

```text
entrada -> salida esperada -> salida real -> score
```

Guardrail:

```text
regla que bloquea una salida peligrosa o inutil
```

## Formula

```text
dataset chico -> ejecutar -> comparar -> corregir -> repetir
```

## Tu problema

En `2-main.py`, crea 5 casos de prueba para extractor de pedidos.

Cada caso debe tener:

- mensaje
- producto esperado
- cantidad esperada
- urgente esperado

Despues imprime cuantos casos pasaron.

## Transferencia al demo

Esta pieza evita confiar en una demo que solo funciono una vez.

Casos minimos para tu proyecto:

- pedido claro
- pedido sin cantidad
- producto inexistente
- stock insuficiente
- pedido ambiguo entre venta y cotizacion

Guardrails minimos:

- no inventar cantidad
- no inventar precio
- no vender producto inactivo
- no ajustar stock sin motivo
- pedir confirmacion antes de acciones en lote
