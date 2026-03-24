# Sentiment Analyzer

An NLP-powered web app that detects sentiment (positive/negative) in any text using DistilBERT.

## Features
- Single text analysis with confidence score
- Batch CSV upload to analyze 100s of reviews at once
- Downloadable results CSV

## Tech Stack
- Python
- HuggingFace Transformers (DistilBERT)
- Streamlit
- Pandas

## How to Run Locally
1. Clone the repo
   git clone https://github.com/iotabhi/sentiment-analyzer.git

2. Install dependencies
   pip install transformers streamlit torch pandas

3. Run
   streamlit run streamlit_app.py

## Model
DistilBERT fine-tuned on SST-2 dataset for binary sentiment classification.

## Author
Abhilasha Manjeet
