import os
from dotenv import load_dotenv
import requests


load_dotenv()


API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# URL de la API de Hugging Face
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {API_KEY}"}  # Usar el token cargado

# Función para hacer la solicitud a la API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "I love cats",
})


print("Respuesta de la API:", output)
