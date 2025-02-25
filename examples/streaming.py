import httpx

url = "http://127.0.0.1:8000/chat/"
data = {"message": "Hello! can you please tell me a story?"}

with httpx.stream("POST", url, json=data) as response:
    for chunk in response.iter_text():
        print(chunk, end="", flush=True)
