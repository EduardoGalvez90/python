import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

# Lista ampliada de términos relacionados a comida rápida y contextos comunes
palabras_clave = [
    "comida", "receta", "nutrición", "almuerzo", "cena", "desayuno", "snack", "postre",
    "vegetariano", "vegano", "dieta", "menú", "saludable", "carbohidrato", "proteína",
    "fruta", "verdura", "bebida", "presupuesto", "recomendación", "antojito", "delivery",
    # Comidas populares
    "pizza", "hamburguesa", "pollo", "arroz", "pasta", "ensalada", "sopa",
    "sandwich", "wrap", "taco", "burrito", "hot dog", "chifa", "chaufa", "ceviche",
    "pan", "papas", "helado", "jugo", "empanada", "salchipapa"
]

# Expresiones contextuales comunes
expresiones_contextuales = [
    r"(quiero|tengo ganas de|podrías recomendarme|me provoca|qué puedo comer|algo para).*",
    r"(dame una opción|alguna comida|qué hay para comer|sugiere).*",
    r".*(pizza|hamburguesa|pollo|chaufa|ensalada|chifa|desayuno|almuerzo|cena|antojito|postre).*"
]

def es_pregunta_de_comida(mensaje):
    mensaje = mensaje.lower()

    # Detectar por palabra clave
    for palabra in palabras_clave:
        if palabra in mensaje:
            return True

    # Detectar por patrón contextual
    for patron in expresiones_contextuales:
        if re.search(patron, mensaje):
            return True

    return False

def responder(mensaje):
    if not es_pregunta_de_comida(mensaje):
        return "❌ Solo puedo responder preguntas sobre comida, recetas o nutrición. ¡Pregúntame qué comer! 🍽️"
    try:
        respuesta = model.generate_content(mensaje)
        return respuesta.text.strip()
    except Exception as e:
        return f"Error: {e}"
