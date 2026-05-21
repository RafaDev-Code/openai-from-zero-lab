"""
Pieza 02 - Entorno y OpenAI SDK

Objetivo:
- cargar `.env`
- leer `OPENAI_MODEL`
- imprimir el modelo elegido

Restriccion:
- no hagas una llamada a OpenAI todavia

Verificacion:
- `python3 2-main.py`
"""

# Escribi tu solucion aca.
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("OPENAI_MODEL")
print(f"El modelo elegido es: {model}")

