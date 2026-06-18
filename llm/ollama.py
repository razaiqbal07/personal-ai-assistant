from ollama import chat

def ask(prompt: str) -> str:
    response = chat(
        model="llama3:latest", messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
