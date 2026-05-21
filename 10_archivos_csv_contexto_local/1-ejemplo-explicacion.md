# Pieza 10 - Archivos y CSV local

## Objetivo

Usar datos propios antes de meter RAG.

## Concepto

No todo requiere embeddings.

Si tenes pocos productos, un CSV leido por Python alcanza.

## Formula

```text
CSV -> Python lee -> filtro simple -> contexto -> modelo
```

## Ejemplo

CSV:

```text
producto,precio,stock
cafe,4500,8
yerba,3000,5
```

Contexto:

```text
Producto cafe: precio 4500, stock 8
```

## Tu problema

En `2-main.py`, crea o lee un CSV simple de productos.

Despues:

- busca un producto por nombre
- arma un texto de contexto
- pedile al modelo que redacte una respuesta corta para cliente

## Transferencia al demo

Este es el primer paso para que el asistente use datos propios.

Campos recomendados para el CSV:

```text
id,nombre,precio,stock,activo
```

Regla: si el dato esta en el CSV, el modelo puede redactar. Si no esta, el
modelo no lo inventa.
