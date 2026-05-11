import gradio as gr
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

API_URL = "https://router.huggingface.co/hf-inference/models/deepset/deberta-v3-base-squad2" #DeBERTa Model

import re

def clean_text(text):
   
    text = re.sub(r'\s+', ' ', text)
   
    text = re.sub(r'[—–]', '-', text)
    return text.strip()

def answer_question(context, question):
    context = clean_text(context)
    question = clean_text(question)

def answer_question(context, question):
    if not context.strip():
        return "⚠️ Please enter a context paragraph."
    
    if not question.strip():
        return "⚠️ Please enter a question."

    if len(context.split()) < 10:
        return "⚠️ Please enter a longer context (at least 10 words)."

    try:
        payload = {
            "inputs": {
                "question": question,
                "context": context
            }
        }
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 503:
            return "⏳ Model is loading, please wait 20 seconds and try again."
        if response.status_code == 401:
            return "❌ Invalid API token."
        if response.status_code != 200:
            return f"❌ Error {response.status_code}: {response.text}"

        result = response.json()
        answer = result.get("answer", "No answer found.")
        score = round(result.get("score", 0) * 100, 2)

        if score < 20:
            return f"🤔 Not sure...\nAnswer: {answer}\nConfidence: {score}%"
        elif score < 60:
            return f"💭 Possible Answer: {answer}\nConfidence: {score}%"
        else:
            return f"✅ Answer: {answer}\nConfidence: {score}%"

    except requests.exceptions.Timeout:
        return "⏳ Request timed out. Please try again."
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks(title="Question Answering System") as demo:
    gr.Markdown("""
    # ❓ Question Answering System
    ### Extract answers from any text 
    """)

    with gr.Row():
        with gr.Column(scale=1):
            context = gr.Textbox(
                lines=10,
                placeholder="Paste your paragraph or context here...",
                label="📄 Context"
            )
            question = gr.Textbox(
                lines=2,
                placeholder="Type your question here...",
                label="❓ Question"
            )
            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear", variant="secondary")
                submit_btn = gr.Button("🔍 Get Answer", variant="primary")

        with gr.Column(scale=1):
            output_text = gr.Textbox(
                lines=5,
                label="💡 Answer"
            )
            gr.Markdown("""
            ### 💡 How to use:
            1. Paste any paragraph in the Context box
            2. Type a question about it
            3. Click Get Answer!
            """)

    def clear():
        return "", "", ""

    submit_btn.click(answer_question, inputs=[context, question], outputs=output_text)
    clear_btn.click(clear, outputs=[context, question, output_text])

    gr.Markdown("""
    ---
    Built with ❤️ using Hugging Face & Gradio |
    [GitHub](https://github.com/parvathy00312)
    """)

demo.launch()