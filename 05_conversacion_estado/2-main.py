"""
Pieza 05 - Conversacion y estado

Objetivo:
- hacer una primera llamada sobre el gestor de stock
- hacer una segunda llamada encadenada con `previous_response_id`
- imprimir ambas respuestas con titulos

Verificacion:
- `python3 2-main.py`
"""

# Escribi tu solucion aca.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
model = os.getenv("OPENAI_MODEL", "gpt-5-mini")

response1 = client.responses.create(
    model=model,
    input="Estoy construyendo un gestor de stock"
)

print("Respuesta 1: ", response1.output_text)

response2 = client.responses.create(
    model=model,
    previous_response_id=response1.id,
    input="Proponme 3 campos para una venta",
)

print("Respuesta 2: ", response2.output_text)
