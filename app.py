import streamlit as st
import PyPDF2
import openai
import json
import csv
from prompt_templates import FLASHCARD_PROMPT
from utils import extract_text_from_pdf

st.title("🧠 LLM-Powered Flashcard Generator")

openai.api_key = "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"




def generate_flashcards(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert educator helping students learn efficiently."},
            {"role": "user", "content": FLASHCARD_PROMPT.format(content=content)}
        ],
        temperature=0.7
    )
    return json.loads(response['choices'][0]['message']['content'])

def export_to_csv(flashcards, filename="flashcards.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Topic", "Question", "Answer"])
        for topic in flashcards:
            for card in topic["cards"]:
                writer.writerow([topic["topic"], card["question"], card["answer"]])
    return filename

content = None

input_method = st.radio("Select Input Method:", ["Upload PDF", "Paste Text"])

if input_method == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        content = extract_text_from_pdf(uploaded_file)
else:
    content = st.text_area("Paste Educational Content Here")

if content and st.button("Generate Flashcards"):
    with st.spinner("Generating flashcards..."):
        try:
            flashcards = generate_flashcards(content)
            for topic in flashcards:
                st.subheader(topic["topic"])
                for i, card in enumerate(topic["cards"], 1):
                    st.markdown(f"**Q{i}: {card['question']}**")
                    st.markdown(f"A{i}: {card['answer']}")
            if st.button("Export to CSV"):
                export_to_csv(flashcards)
                st.success("Flashcards exported to flashcards.csv")
        except Exception as e:
            st.error(f"Error: {e}")

