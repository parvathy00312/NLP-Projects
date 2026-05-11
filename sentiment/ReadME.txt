# Sentiment_Analyzer
# 💬 Sentiment Analyzer

An open source sentiment analysis tool built using Hugging Face LLMs and Gradio.

## 📌 What it does
Type or paste any English text and instantly detect whether the sentiment is:
- 😊 POSITIVE
- 😞 NEGATIVE  
- 😐 NEUTRAL

With a confidence percentage showing how sure the model is!

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Hugging Face API | RoBERTa sentiment model |
| Gradio | Web UI |
| python-dotenv | Secure token management |

## 🤖 Model Used
**cardiffnlp/twitter-roberta-base-sentiment**
A RoBERTa model fine-tuned on Twitter data for sentiment analysis.
Returns 3 labels: POSITIVE, NEGATIVE, NEUTRAL with confidence scores.

## 🚀 How to Run

### 1. Clone the repository
git clone https://github.com/parvathy00312/sentiment-analyzer.git
cd sentiment-analyzer

### 2. Install dependencies
pip install gradio requests python-dotenv

### 3. Add your Hugging Face token
Create a .env file and add:
HF_TOKEN=your_huggingface_token_here

### 4. Run the app
python app.py

### 5. Open in browser
http://127.0.0.1:7861

## 📂 Project Structure
sentiment-analyzer/
├── app.py          # Main application
├── .gitignore      # Ignores .env file
└── README.md       # This file

## 🔮 Future Plans
- Detect emotions (happy, sad, angry, fear)
- Add batch text analysis
- Support CSV file upload

## 👩‍💻 Author
**Parvathy**
GitHub: https://github.com/parvathy00312

## 📄 License
MIT License - feel free to use and modify!