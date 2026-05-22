"""
Pieza 04 - Modelos, instrucciones y tokens

Objetivo:
- hacer dos llamadas con el mismo input
- una respuesta como tutor principiante
- otra respuesta como tecnico de backend
- comparar como cambian instrucciones y salida

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
input_text = "Explica que significa descontar stock."
response = client.responses.create(
    model = model,
    instructions = "Sos un tutor principiante. Frases cortas. Ejemplo simple.",
    input = input_text,
    max_output_tokens=180
)
print(("=" * 20))
print("Respuesta como tutor principiante: ", response.output_text)
print(("=" * 20))
response = client.responses.create(
    model = model,
    instructions = "Sos un tecnico de backend. Menciona validacion, stock disponible y movimiento/log.",
    input = input_text,
    max_output_tokens=280
)
print(("=" * 20))
print("Respuesta como tecnico de backend: ", response.output_text)
print(("=" * 20))
