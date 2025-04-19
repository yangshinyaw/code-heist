import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

def generate_riddle_hf():
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}"
    }

    prompt = (
        "Create a short hacking-themed riddle that is solvable in one or two words. "
        "Format it like this:\nRiddle: <your riddle>\nAnswer: <correct answer>"
    )

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/bigcode/starcoder",  # or try 'tiiuae/falcon-7b-instruct'
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        output = response.json()[0]["generated_text"]
        lines = output.split("\n")
        riddle_line = next((line for line in lines if line.lower().startswith("riddle:")), None)
        answer_line = next((line for line in lines if line.lower().startswith("answer:")), None)

        if riddle_line and answer_line:
            riddle = riddle_line.replace("Riddle:", "").strip()
            answer = answer_line.replace("Answer:", "").strip().lower()
            return riddle, answer

    print(f"⚠️ Hugging Face API failed: {response.text}")
    return None, None
