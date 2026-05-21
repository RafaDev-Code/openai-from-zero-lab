# Metodo de aprendizaje

Este repo funciona como un curso-proyecto. No se trata de mirar videos ni de
copiar soluciones. Se trata de construir una demo real con ciclos cortos de
practica, correccion y repaso.

## Roles

Tu rol como estudiante:

- intentar antes de pedir solucion
- ejecutar el codigo
- explicar que hiciste con tus palabras
- registrar dudas y errores
- pedir correccion cuando hay algo concreto para revisar

Mi rol como IA profesor/tecnico:

- explicar lo justo para que puedas avanzar
- revisar como ingeniero, no solo como tutor amable
- hacer preguntas que obliguen a recuperar de memoria
- detectar huecos de modelo mental
- proponer el siguiente paso mas util
- cuidar que el proyecto siga siendo una demo real

## Ciclo de una pieza

```text
1. pre-test corto
2. ejemplo trabajado
3. intento propio
4. ejecucion/verificacion
5. explicacion de memoria
6. correccion tecnica
7. repaso espaciado
```

## Practicas que vamos a usar

### Practica de recuperacion

Antes de leer una explicacion, intenta responder desde memoria. Aunque falles,
prepara al cerebro para aprender mejor.

Preguntas base:

- que problema resuelve esto
- que entrada necesita
- que salida produce
- que podria salir mal

### Repeticion espaciada

No repasamos todo el mismo dia. Cada pieza se revisa en:

```text
D+1, D+3, D+7
```

En D+1 explicas. En D+3 haces una variante. En D+7 la conectas con otra pieza.

### Ejemplos trabajados con retirada gradual

Primero ves una formula clara. Despues la ayuda baja:

```text
ejemplo completo -> esqueleto -> pista -> intento libre
```

### Practica deliberada

No alcanza con "funciona". Cada correccion apunta a una mejora concreta:

- una validacion que falta
- un caso borde
- un nombre confuso
- una separacion de responsabilidades
- una prueba que falta

### Intercalado

El proyecto mezcla temas. Una pieza de OpenAI se conecta con Python, datos,
FastAPI, tools y evals. Eso evita aprender conceptos aislados que despues no
se transfieren al trabajo real.

### Autoexplicacion

Cada pieza termina con una mini defensa:

```text
Esto recibe...
Esto transforma...
Esto valida...
Esto puede fallar si...
Lo verifique con...
```

## Criterio de dominio

Nivel 1: lo ejecuto siguiendo instrucciones.

Nivel 2: lo modifico para un caso parecido.

Nivel 3: lo explico sin mirar.

Nivel 4: detecto riesgos y lo pruebo.

Nivel 5: lo conecto con el proyecto final.

Para avanzar bien, apunta a nivel 3 en piezas chicas y nivel 4 en piezas que
tocan side effects: stock, ventas, desactivar productos o datos reales.
