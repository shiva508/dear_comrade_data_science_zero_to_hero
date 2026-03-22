import streamlit as st
import PyPDF2
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer
from transformers import pipeline

# -----------------------------
# Load models
# -----------------------------
embedder = SentenceTransformer('all-MiniLM-L6-v2') # all-mpnet-base-v2, all-MiniLM-L6-v2
# qa_pipeline = pipeline(task="text2text-generation", model="google/flan-t5-base")
qa_pipeline = pipeline("text-generation")


# -----------------------------
# Read PDF
# -----------------------------
def read_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# -----------------------------
# Split text
# -----------------------------
def split_text(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


# -----------------------------
# Create FAISS index
# -----------------------------
def create_index(chunks):
    embeddings = embedder.encode(chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index, embeddings


# -----------------------------
# Search relevant chunks
# -----------------------------
def search(query, index, chunks, k=3):
    query_vec = embedder.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    results = [chunks[i] for i in indices[0]]
    return results


# -----------------------------
# Generate answer
# -----------------------------
def get_answer(question, contexts):
    context = " ".join(contexts)

    prompt = f"""
    Context: {context}

    Question: {question}

    Answer:
    """

    result = qa_pipeline(prompt, max_length=200)
    return result[0]['generated_text']


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📄 Chat with your PDF (RAG System)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    text = read_pdf(uploaded_file)
    chunks = split_text(text)

    st.success("PDF processed!")

    index, embeddings = create_index(chunks)

    question = st.text_input("Ask a question:")

    if question:
        contexts = search(question, index, chunks)
        answer = get_answer(question, contexts)

        st.write("### ✅ Answer:")
        st.write(answer)

        st.write("### 🔍 Retrieved Contexts:")
        for c in contexts:
            st.write(c[:300] + "...")