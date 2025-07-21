import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.9,          
    "top_p": 0.95,               
    "max_output_tokens": 100     
}

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_restaurant_name(cuisine):
    cuisine = "Mexican"
    prompt_name = f"Suggest a unique and creative name for a high-end Mexican restaurant. Only return one name, no explanation."

    step1_response = model.generate_content(prompt_name, generation_config=generation_config)
    restaurant_name = step1_response.text.strip()

    prompt_menu = f"Suggest 5 popular {cuisine} dishes for the restaurant named {restaurant_name}. Return them as a plain comma-separated list, no explanations."

    step2_response = model.generate_content(prompt_menu, generation_config=generation_config)
    menu_items = [item.strip() for item in step2_response.text.strip().split(",")]

    structured_output = {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
    
    return structured_output


