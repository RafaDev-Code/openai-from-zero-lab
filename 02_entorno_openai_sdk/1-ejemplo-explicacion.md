# Pieza 02 - Entorno y OpenAI SDK

## Objetivo

Preparar Python para llamar a OpenAI.

## Concepto

Una app no debe tener la API key escrita en el codigo.

La key vive en `.env`.

El codigo carga variables y crea un cliente:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
```

## Formula

```text
.env -> load_dotenv() -> OpenAI() -> client listo
```

## Ejemplo

```python
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("OPENAI_MODEL", "gpt-5-mini")

print(model)
```

## Tu problema

En `2-main.py`, hace un script que:

- cargue `.env`
- lea `OPENAI_MODEL`
- imprima el modelo elegido
- no haga llamada a OpenAI todavia

## Como probar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 2-main.py
```

## Transferencia al demo

Esta pieza parece simple, pero es el piso de todo.

En una demo real:

- la API key nunca va escrita en el codigo
- el modelo se cambia por variable de entorno
- el backend puede correr en otra maquina sin tocar el codigo

Si esto esta prolijo, despues FastAPI y los agentes heredan una base sana.
