import gradio as gr
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

MODELS = {
    "English": "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn",
}

def summarize(text, language):
    if not text.strip():
        return "⚠️ Please enter some text to summarize."
    
    if len(text.split()) < 30:
        return "⚠️ Please enter at least 30 words for a good summary."

    # Trim text to max 1024 words to avoid model limits
    words = text.split()
    if len(words) > 1024:
        text = " ".join(words[:1024])

    API_URL = MODELS[language]

    try:
        payload = {"inputs": text}
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

        if response.status_code == 503:
            return "⏳ Model is loading, please wait 20 seconds and try again."
        
        if response.status_code == 401:
            return "❌ Invalid API token. Please check your .env file."

        if response.status_code != 200:
            return f"❌ Error {response.status_code}: {response.text}"

        result = response.json()

        if isinstance(result, list):
            summary = result[0].get("summary_text", "No summary returned.")
            if language == "Malayalam / Multilingual":
                return f"📝 Note: Malayalam summarization uses multilingual model.\n\n{summary}"
            return summary
        else:
            return f"❌ Unexpected response: {result}"

    except requests.exceptions.Timeout:
        return "⏳ Request timed out. Please try again."
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks(title="LT-LLM Text Summarizer") as demo:
    gr.Markdown("""
    # 🌐 LT-LLM Text Summarizer
    ### Multilingual Text Summarization | ICFOSS LT-LLM Project
    """)

    with gr.Row():
        with gr.Column(scale=1):
            language = gr.Dropdown(
                choices=["English"],
                value="English",
                label="🌍 Select Language"
            )
            input_text = gr.Textbox(
                lines=12,
                placeholder="Paste your text here (minimum 30 words)...",
                label="📝 Input Text"
            )
            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear", variant="secondary")
                submit_btn = gr.Button("✨ Summarize", variant="primary")

        with gr.Column(scale=1):
            output_text = gr.Textbox(
                lines=12,
                label="📋 Summary"
            )
            word_count = gr.Markdown("**Word count:** 0 words")

    def update_word_count(text):
        count = len(text.split()) if text.strip() else 0
        return f"**Word count:** {count} words"

    def clear():
        return "", "", "**Word count:** 0 words"

    input_text.change(update_word_count, inputs=input_text, outputs=word_count)
    submit_btn.click(summarize, inputs=[input_text, language], outputs=output_text)
    clear_btn.click(clear, outputs=[input_text, output_text, word_count])

    gr.Markdown("""
    ---
   Built with ❤️ using Hugging Face & Gradio | 
    [GitHub](https://github.com/parvathy00312/lt-llm-summarizer)
    """)

demo.launch()