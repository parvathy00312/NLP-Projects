# ❓ Question Answering System

An open source extractive Question Answering system built using Hugging Face Transformers and Gradio.

## 📌 What it does
Paste any paragraph as context, ask a question about it, and get the exact answer extracted from the text with a confidence score!

### Example:
**Context:** Kerala is a state in southern India. It was formed on November 1, 1956. The capital of Kerala is Thiruvananthapuram.

**Question:** What is the capital of Kerala?

**Answer:** ✅ Thiruvananthapuram (Confidence: 98%)


## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Hugging Face API | DeBERTa-v3 QA model |
| Gradio | Web UI |
| python-dotenv | Secure token management |

## 🤖 Model Used
**deepset/deberta-v3-base-squad2**
A DeBERTa-v3 model fine-tuned on SQuAD2 dataset for extractive question answering.
Chosen over RoBERTa after experimentation showed 40% improvement in confidence scores on complex paragraphs.

## 📊 Confidence Levels
| Confidence | Meaning |
|-----------|---------|
| Above 60% | ✅ Reliable answer |
| 20% - 60% | 💭 Possible answer |
| Below 20% | 🤔 Not sure |

## 🚀 How to Run

### 1. Clone the repository
git clone https://github.com/parvathy00312/question-answering-system.git
cd question-answering-system

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
question-answering-system/
├── app.py          # Main application
├── .gitignore      # Ignores .env file
└── README.md       # This file

## 🔬 Model Comparison
| Model | Confidence on complex text |
|-------|--------------------------|
| roberta-base-squad2 | ~40% |
| deberta-v3-base-squad2 | ~80% |

DeBERTa-v3 was chosen for its superior performance!

## 🔮 Future Plans
- Support PDF file upload as context
- Add multi-paragraph search

## 👩‍💻 Author
**Parvathy**
GitHub: https://github.com/parvathy00312

## 📄 License
MIT License - feel free to use and modify!