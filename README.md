# openai-from-zero-lab

Laboratorio para aprender OpenAI programaticamente construyendo una demo real:
un asistente operativo de stock, ventas y cotizaciones.

La idea central:

```text
estudiante: vos
IA: profesor + tecnico
repo: cuaderno de practica + taller de construccion
demo final: agente operativo sobre stock y ventas
```

Este repo no apunta a "usar mejor ChatGPT" como usuario final. Apunta a
construir software que usa OpenAI: SDK, Responses API, instrucciones, JSON,
tools, RAG, FastAPI, MCP, Codex, workflows/agentes, evals y guardrails.

## Resultado esperado

Al terminar, tenes que poder explicar y mostrar una demo que resuelve estos
problemas:

- cargar mucho stock con ayuda de un agente
- mirar movimientos y encontrar anomalias rapido
- hacer ajustes de stock con validacion
- desactivar productos con criterio y registro
- vender descontando stock
- cotizar usando productos, precios y reglas

La demo no debe ser magia. Debe ser explicable:

```text
mensaje -> intencion -> JSON validado -> tool segura -> accion local/API -> log -> respuesta
```

## Metodo de aprendizaje

Vamos a usar practicas con buena evidencia educativa:

- practica de recuperacion: responder sin mirar antes de leer la solucion
- repeticion espaciada: repasar piezas despues de 1, 3 y 7 dias
- ejemplos trabajados con retirada gradual: primero ves formula, despues haces vos
- practica deliberada: corregir errores concretos, no solo "seguir mirando"
- intercalado: mezclar API, Python, FastAPI, tools y evals en el mismo proyecto
- autoexplicacion: poder decir que entra, que sale, que falla y como se verifica
- feedback frecuente: cada pieza termina con revision tecnica

La guia completa esta en
[00_metodo_aprendizaje/README.md](00_metodo_aprendizaje/README.md).

Documentos clave:

- [proyecto_demo.md](00_metodo_aprendizaje/proyecto_demo.md): que demo estamos construyendo
- [mapa_anthropic_openai.md](00_metodo_aprendizaje/mapa_anthropic_openai.md): como se adapta el curso a OpenAI
- [plan_sesiones.md](00_metodo_aprendizaje/plan_sesiones.md): agenda sugerida de estudio
- [rubrica_revision.md](00_metodo_aprendizaje/rubrica_revision.md): como voy a corregirte
- [checkpoints.md](00_metodo_aprendizaje/checkpoints.md): repasos y mini examenes

## Estructura

Cada pieza tiene:

```text
1-ejemplo-explicacion.md  -> pizarron
2-main.py o 2-tu-trabajo.md -> tu intento
```

El pizarron ensena la formula. Tu archivo es donde practicas. La correccion viene
despues de tu intento, no antes.

## Flujo de cada pieza

1. Lee el objetivo y cerra el archivo.
2. Escribi de memoria que problema resuelve.
3. Lee el ejemplo.
4. Implementa o disena en `2-*`.
5. Ejecuta/verifica.
6. Pedime revision con:

```text
termine pieza NN. Revisame como profesor/tecnico.
```

Para pedir una buena correccion usa
[00_metodo_aprendizaje/como_pedir_correccion.md](00_metodo_aprendizaje/como_pedir_correccion.md).

## Ruta corta

```text
01                 contrato de aprendizaje
02-07              OpenAI desde Python
08-12              tools, datos propios y FastAPI
13-15              MCP, contratos y Codex en repos
16-18              workflows/agentes, evals y demo final
```

La ruta completa esta en [ruta.md](ruta.md).

## Requisitos

Desde la pieza 02:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Despues completas `OPENAI_API_KEY` en `.env`.

Los ejemplos usan `OPENAI_MODEL` desde `.env`. Si no lo definis, usamos
`gpt-5-mini` como modelo de aprendizaje por costo/velocidad.

## Regla de avance

No pases de pieza hasta poder explicar:

- que problema resuelve
- que entrada recibe
- que salida produce
- que puede fallar
- como lo verificaste
- como se conecta con la demo final

La regla dura pero justa: una pieza esta terminada cuando corre, se entiende y
se puede corregir.
