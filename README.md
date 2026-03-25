# 🎭 Sentiment Analyzer

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-DistilBERT-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

An NLP-powered web application that leverages a fine-tuned **DistilBERT** model to perform high-accuracy sentiment analysis on text data. Perfect for analyzing customer reviews, social media comments, or feedback at scale.

## 🚀 Key Features
* **Real-time Analysis:** Input any text and get instant sentiment classification (Positive/Negative).
* **Confidence Scoring:** View the model's probability score for each prediction to understand its certainty.
* **Batch Processing:** Upload a `.csv` file to analyze hundreds of reviews simultaneously.
* **Data Export:** Download your processed results as a new CSV for further data science workflows.

## 🛠️ Tech Stack
* **Language:** Python
* **Model:** HuggingFace Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)
* **Frontend:** Streamlit
* **Data Handling:** Pandas
* **Backend:** PyTorch

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/iotabhi/sentiment-analyzer.git](https://github.com/iotabhi/sentiment-analyzer.git)
    cd sentiment-analyzer
    ```

2.  **Install dependencies:**
    ```bash
    pip install transformers streamlit torch pandas
    ```

3.  **Launch the App:**
    ```bash
    streamlit run streamlit_app.py
    ```

## 🧠 Model Architecture
This project uses **DistilBERT**, a distilled version of BERT that is 40% smaller and 60% faster while retaining 97% of BERT's performance. It has been specifically fine-tuned on the **SST-2 (Stanford Sentiment Treebank)** dataset for binary classification, making it highly efficient for production-level web apps.

## 📈 Future Roadmap
- [ ] Support for Multi-class classification (Neutral sentiment).
- [ ] Interactive Dashboard using Matplotlib/Seaborn for batch data visualization.
- [ ] Deployment to Hugging Face Spaces or Streamlit Cloud.
- [ ] Integration with Twitter/X API for real-time sentiment tracking.

## ✍️ Author
**Abhilasha Manjeet**
* B.Tech CSE Student @ NIST University
* [GitHub](https://github.com/iotabhi)
* [LinkedIn](https://www.linkedin.com/in/abhilashamanjeet)

---
*Developed as part of my portfolio in AI/ML and Web Development.*
