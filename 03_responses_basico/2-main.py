"""
Pieza 03 - Responses API basico

Objetivo:
- crear un cliente OpenAI
- usar `OPENAI_MODEL`
- preguntar que es stock en lenguaje simple
- imprimir solo el texto final

Verificacion:
- `python3 2-main.py`
"""

# Escribi tu solucion aca.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
client = OpenAI()

response = client.responses.create(
    model=model,
    input="Explica que es stock en lenguaje simple"
)

print(response.output_text)