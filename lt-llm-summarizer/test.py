import requests

API_TOKEN = "token"  # your real token here

headers = {"Authorization": f"Bearer {API_TOKEN}"}

response = requests.post(
    "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn",
    headers=headers,
    json={"inputs": "The sun is a star at the center of our solar system. It provides light and heat to all planets."}
)

print("Status code:", response.status_code)
print("Response text:", response.text)