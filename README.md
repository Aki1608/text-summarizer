# AI Document & Web-article Summarizer

A full-stack Natural Language Processing (NLP) dashboard designed to ingest raw text or web URLs and compress them into highly accurate, human-readable summaries. This project demonstrates a complete end-to-end NLP pipeline, featuring smart routing, dynamic web scraping, and local machine learning inference with customizable parameters.

## Features
* **Hybrid Input Routing:** Automatically detects whether the user pasted a web link or raw text. URLs are dynamically scraped and cleaned, while raw text is routed directly to the AI.
* **Custom Parameter Control:** Users can fine-tune the AI's output using UI sliders to dictate the minimum and maximum length of the generated summary.
* **Advanced Analytics:** Calculates and displays a "Compression Ratio" metric alongside the original and summarized text, allowing users to instantly evaluate the model's efficiency.
* **Local ML Inference:** Runs entirely locally using Hugging Face's Seq2Seq transformer models, ensuring zero reliance on paid APIs and total data privacy.
* **Custom Dashboard UI:** Built using Gradio Blocks to create a clean, multi-column interface rather than a standard chatbot window.

## Tech Stack
* **Python 3**
* **Hugging Face Transformers** (NLP Summarization Pipeline)
* **BeautifulSoup4 / Requests** (Web Scraping & HTML Parsing)
* **Gradio** (Frontend UI Dashboard)

## Project Structure
* `app.py` - The frontend application. It builds the Gradio Blocks UI, houses the smart-routing logic for inputs, and manages the state between the UI and the backend.
* `summarizer_engine.py` - The core ML backend. It handles loading the pre-trained transformer model, tokenizing the text, and generating the summary based on the user's slider constraints.
* `text_extractor.py` - The data ingestion module. When a URL is detected, it handles the HTTP requests and utilizes BeautifulSoup to strip away HTML boilerplate, returning only clean article text.
* `requirements.txt` - The strict list of dependencies required to run the environment.

## Quick Start Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Set Up the Environment
It is highly recommended to run this inside a Virtual Environment to keep your system dependencies clean.
```bash
python -m venv venv

# Activate on Mac/Linux:
source venv/bin/activate  

# Activate on Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
Install all required libraries for the web UI, scraping tools, and local ML models:
```bash
pip install -r requirements.txt
```
*(Note: Upon your first summarization, the application will download the pre-trained transformer weights to your local machine).*

### 4. Launch the Dashboard
Start the Gradio web server:
```bash
python app.py
```
Click the local URL generated in your terminal (e.g., `http://127.0.0.1:7860`) to open the web interface. Paste an article link or a block of text, adjust your sliders, and start summarizing!

---

## ⚙️ How It Works
1. **Ingestion & Routing:** The user submits input via the UI. The `process_user_input` function evaluates the string. If it begins with `http`, it is sent to the `text_extractor`. Otherwise, it skips extraction.
2. **Web Scraping (Conditional):** The extractor fetches the webpage and uses BeautifulSoup to isolate the core paragraph tags while discarding ads and navigation bars.
3. **Inference:** The clean string of text (capped at 4,000 characters to prevent memory overflow) is passed to the `SummarizerEngine` alongside the user's length parameters.
4. **Analytics & Output:** The engine generates the summary, calculates the compression ratio, and populates the multi-column Gradio dashboard with the results.
