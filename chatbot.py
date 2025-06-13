import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def es_pregunta_de_comida(mensaje):
    temas_permitidos = [
        "comida", "receta", "nutrición", "almuerzo", "cena",
        "desayuno", "snack", "postre", "vegetariano", "vegano",
        "dieta", "menú", "saludable", "carbohidratos", "proteína", "fruta", "verdura", "bebida", "opción","hola"
    ]
    return any(palabra in mensaje.lower() for palabra in temas_permitidos)

def responder(mensaje):
    if not es_pregunta_de_comida(mensaje):
        return "❌ Solo puedo responder preguntas sobre comida, recetas o nutrición. ¡Pregúntame qué comer! 🍽️"
    try:
        respuesta = model.generate_content(mensaje)
        return respuesta.text.strip()
    except Exception as e:
        return f"Error: {e}"
