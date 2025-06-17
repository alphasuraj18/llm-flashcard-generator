# llm-flashcard-generator
Generate educational flashcards from PDF, Text content using LLMs and Streamlit.
# 🧠 LLM-Powered Flashcard Generator

This Streamlit-based app converts educational PDFs or raw text into grouped flashcards using OpenAI's GPT-3.5.

## 🚀 Features

- Upload `.pdf` or paste raw educational content
- Automatically generate flashcards in Q&A format
- Topics grouped intelligently
- Export results to `.csv`
- Powered by OpenAI GPT-3.5

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI API
- PyPDF2

## 📦 Setup

How to Create and Use Virtual Environment
Run the following commands in PowerShell:

powershell
# Create a virtual environment
python -m venv .venv

# Activate the environment
.venv\Scripts\Activate.ps1

# Install the dependencies
pip install -r requirements.txt

---

## ▶️ How to Run Locally (Windows PowerShell)

1. **Open Terminal (PowerShell)**
2. 
3. **Activate the virtual environment**
   ```powershell
   .venv\Scripts\Activate.ps1
4. **Navigate to the project directory**
   cd "C:\Users\HP\OneDrive\Desktop\project\flashcard-generator-llm"
   
5. **Run the Streamlit app**
   streamlit run app.py


## 📄 Sample Output

Includes sample input/output in the `/samples` folder.

## 🎯 Future Improvements

- Anki deck export
- Flashcard editing & difficulty levels
- Multilingual support

## 📹 Demo (Optional)
Demo.mp4 available in `/demo`.

## 📝 License
MIT
