# Proyecto demo: asistente operativo de stock y ventas

Este es el producto que guia todo el aprendizaje.

## Problema

Hoy hay tareas manuales que consumen tiempo y son faciles de hacer mal:

- cargar mucho stock
- mirar movimientos
- hacer cambios de stock
- desactivar productos
- vender
- cotizar

## Solucion buscada

Un asistente que converse, entienda la intencion y use tools seguras para operar
el sistema.

```text
usuario -> agente -> tool -> sistema -> respuesta
```

## Principio clave

El agente no toca la verdad directamente. El agente pide acciones. El sistema
valida y ejecuta.

```text
agente conversa y decide
Python/FastAPI valida y ejecuta
base/datos guardan la verdad
evals miden calidad
logs permiten auditar
```

## Capacidades de la demo

### 1. Cargar stock en lote

Input ejemplo:

```text
Carga 10 cafe molido, 5 yerba organica y 3 filtros.
```

Debe producir:

- items detectados
- validacion de productos
- confirmacion antes de modificar
- movimientos de stock registrados

### 2. Mirar movimientos

Input ejemplo:

```text
Mostrame movimientos raros de esta semana.
```

Debe producir:

- filtro por fecha/tipo/producto
- resumen legible
- posibles anomalias
- recomendacion de revision

### 3. Ajustar stock

Input ejemplo:

```text
El cafe quedo en 7 unidades reales. Ajustalo.
```

Debe producir:

- stock anterior
- stock nuevo
- motivo requerido
- movimiento de ajuste

### 4. Desactivar productos

Input ejemplo:

```text
Desactiva todos los productos sin stock que no se venden hace 60 dias.
```

Debe producir:

- lista candidata
- reglas aplicadas
- confirmacion
- productos desactivados

### 5. Vender

Input ejemplo:

```text
Vende 2 cafe y 1 filtro.
```

Debe producir:

- disponibilidad
- total
- descuento de stock
- venta registrada

### 6. Cotizar

Input ejemplo:

```text
Cotizame 4 cafe y 2 yerba para retirar hoy.
```

Debe producir:

- items
- precios
- total
- condiciones
- respuesta para cliente

## Modelo de datos inicial

```text
Producto:
- id
- nombre
- precio
- stock
- activo

Movimiento:
- id
- producto_id
- tipo: carga | venta | ajuste | desactivacion
- cantidad
- motivo
- fecha

Venta:
- id
- items
- total
- fecha

Cotizacion:
- id
- items
- total
- estado
- fecha
```

## Tools iniciales

- `buscar_producto`
- `consultar_stock`
- `cargar_stock_lote`
- `listar_movimientos`
- `ajustar_stock`
- `desactivar_producto`
- `cotizar_pedido`
- `registrar_venta`
- `solicitar_revision_humana`

## Guardrails minimos

- No vender producto inactivo.
- No vender mas stock del disponible sin marcarlo como pendiente.
- No ajustar stock sin motivo.
- No desactivar en lote sin mostrar candidatos y pedir confirmacion.
- No inventar precios.
- No inventar productos.
- Toda accion que modifica datos genera movimiento/log.

## Demo final esperada

La demo puede ser CLI o FastAPI al principio. Lo importante es que muestre:

```text
entrada humana
extraccion estructurada
tool elegida
validacion
accion
respuesta final
eval o prueba
```
