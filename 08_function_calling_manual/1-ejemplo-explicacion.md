# Pieza 08 - Function calling manual

## Objetivo

Entender tools sin OpenAI todavia.

## Concepto

Una tool es una funcion que tu sistema sabe ejecutar.

Antes de conectarla al modelo, tiene que funcionar sola.

## Formula

```text
input -> funcion Python -> resultado verificable
```

## Ejemplo

```python
stock = {"cafe": 8}

def consultar_stock(producto):
    return stock.get(producto, 0)
```

## Tu problema

En `2-main.py`, arma:

- diccionario de stock
- funcion `consultar_stock(producto)`
- funcion `descontar_stock(producto, cantidad)`
- 3 pruebas manuales con `print`

No uses OpenAI en esta pieza.

## Transferencia al demo

Antes de que el modelo pida tools, tus tools tienen que ser correctas sin
modelo.

En esta pieza empezas a separar:

```text
agente = decide que necesita
tool Python = valida y ejecuta
```

## Casos que tenes que probar

- producto existente
- producto inexistente
- descuento mayor al stock disponible

Si alguno de esos casos no esta pensado, todavia no hay tool segura.
