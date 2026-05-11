import gradio as gr
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

API_URL = "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment"

def analyze_sentiment(text):
    if not text.strip():
        return "⚠️ Please enter some text."
    
    if len(text.split()) < 3:
        return "⚠️ Please enter at least 3 words."

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text},
            timeout=30
        )

        if response.status_code == 503:
            return "⏳ Model is loading, please wait 20 seconds and try again."
        if response.status_code == 401:
            return "❌ Invalid API token."
        if response.status_code != 200:
            return f"❌ Error {response.status_code}: {response.text}"

        result = response.json()
        labels = result[0]

        # Sort by score
        labels.sort(key=lambda x: x["score"], reverse=True)
        top = labels[0]

        label = top["label"]
        score = round(top["score"] * 100, 2)

        if label == "LABEL_2":
            emoji = "😊"
            label = "POSITIVE"
        elif label == "LABEL_0":
            emoji = "😞"
            label = "NEGATIVE"
        else:
            emoji = "😐"
            label = "NEUTRAL"

        return f"{emoji} {label}\nConfidence: {score}%"

    except requests.exceptions.Timeout:
        return "⏳ Request timed out. Please try again."
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks(title="Sentiment Analyzer") as demo:
    gr.Markdown("""
    # 💬 Sentiment Analyzer
    ### Detect Positive / Negative / Neutral sentiment
    """)

    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                lines=8,
                placeholder="Type or paste your text here...",
                label="📝 Input Text"
            )
            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear", variant="secondary")
                submit_btn = gr.Button("🔍 Analyze", variant="primary")

        with gr.Column(scale=1):
            output_text = gr.Textbox(
                lines=8,
                label="📊 Result"
            )
            word_count = gr.Markdown("**Word count:** 0 words")

    def update_word_count(text):
        count = len(text.split()) if text.strip() else 0
        return f"**Word count:** {count} words"

    def clear():
        return "", "", "**Word count:** 0 words"

    input_text.change(update_word_count, inputs=input_text, outputs=word_count)
    submit_btn.click(analyze_sentiment, inputs=input_text, outputs=output_text)
    clear_btn.click(clear, outputs=[input_text, output_text, word_count])

    gr.Markdown("""
    ---
    Built with ❤️ using Hugging Face & Gradio |
    [GitHub](https://github.com/parvathy00312)
    """)

demo.launch()