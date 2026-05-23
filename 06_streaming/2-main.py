"""
Pieza 06 - Streaming

Objetivo:
- pedir una guia para revisar stock antes de abrir
- mostrar la respuesta en vivo usando streaming

Verificacion:
- al ejecutar, el texto debe aparecer progresivamente
- `python3 2-main.py`
"""

# Escribi tu solucion aca.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
client = OpenAI()
input_text = "Dame una guía de 6 pasos para revisar stock antes de abrir el local."

with client.responses.stream(
    model=model,
    input=input_text,
) as stream:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)

print()