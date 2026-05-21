# Checkpoints y repasos

Este archivo sirve para medir avance. Marca con una `x` cuando lo hagas.

## Checkpoint semanal

- [ ] Puedo explicar que piezas hice y para que sirven
- [ ] Ejecute el codigo de las piezas con codigo
- [ ] Tengo al menos un error registrado y corregido
- [ ] Puedo conectar lo aprendido con stock/ventas/cotizaciones
- [ ] Se que pieza sigue y por que

## Repaso por pieza

Formato recomendado:

```text
Pieza:
Fecha:
D+1:
D+3:
D+7:
Punto debil:
Correccion:
```

## Preguntas de recuperacion

Usalas sin mirar los archivos.

- Que diferencia hay entre texto libre y JSON validable?
- Por que una tool no debe ejecutar acciones sin validacion?
- Que parte decide el modelo y que parte decide Python?
- Cuando conviene workflow y cuando agente?
- Que endpoint expondria FastAPI y que no expondria?
- Que caso de stock puede generar una venta incorrecta?
- Como probarias que el extractor de pedido no inventa cantidades?
- Por que el agente no debe ser la fuente de verdad?

## Mini examenes

### Despues de pieza 07

- extraer producto, cantidad y urgencia de 5 mensajes
- explicar por que JSON ayuda a una app
- nombrar 3 errores de extraccion

### Despues de pieza 12

- mostrar `/health`
- mostrar `/extraer-pedido`
- explicar donde vive la API key
- explicar que validaria antes de registrar una venta

### Despues de pieza 18

- demo de venta
- demo de cotizacion
- demo de ajuste de stock
- demo de error: producto inexistente o stock insuficiente
- mostrar al menos 5 evals pasando
