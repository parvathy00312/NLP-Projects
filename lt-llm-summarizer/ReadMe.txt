# 🌐 LT-LLM Text Summarizer

An open source text summarization tool built using Hugging Face LLMs and Gradio.

## 📌 What it does
Paste any long English text and get a clean, concise summary instantly using Facebook's BART model.

## 🖼️ Screenshot
front end.png

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Hugging Face API | BART summarization model |
| Gradio | Web UI |
| python-dotenv | Secure token management |

## 🚀 How to Run

### 1. Clone the repository
git clone https://github.com/parvathy00312/lt-llm-summarizer.git
cd lt-llm-summarizer

### 2. Install dependencies
pip install gradio requests python-dotenv

### 3. Add your Hugging Face token
Create a .env file and add:
HF_TOKEN=your_huggingface_token_here

### 4. Run the app
python app.py

### 5. Open in browser
http://127.0.0.1:7860

## 📂 Project Structure
lt-llm-summarizer/
├── app.py          # Main application
├── test.py         # API test script
├── .env            # Your HF token (not pushed to GitHub)
├── .gitignore      # Ignores .env file
└── README.md       # This file

## 🔮 Future Plans
- Add Malayalam language support
- Add translation layer for Indian languages
- Deploy on Hugging Face Spaces

## 👩‍💻 Author
**Parvathy**
GitHub: https://github.com/parvathy00312

## 📄 License
MIT License - feel free to use and modify!