import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬", layout="centered")

st.title("Sentiment Analyzer")
st.caption("Paste any product review or text — AI will detect if it's positive or negative.")

text_input = st.text_area("Enter your text here", height=150, placeholder="e.g. This product is amazing, I love it!")

if st.button("Analyze"):
    if text_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing..."):
            model = load_model()
            result = model(text_input)[0]

        label = result["label"]
        score = round(result["score"] * 100, 1)

        if label == "POSITIVE":
            st.success(f"Positive — {score}% confidence")
        else:
            st.error(f"Negative — {score}% confidence")

        st.progress(result["score"], text=f"{label} — {score}%")

st.divider()

# --- BONUS: CSV batch upload ---
st.subheader("Batch analyze (CSV)")
st.caption("Upload a CSV with a column called 'review' to analyze multiple reviews at once.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:
    import pandas as pd
    df = pd.read_csv(uploaded)

    if "review" not in df.columns:
        st.error("CSV must have a column named 'review'")
    else:
        with st.spinner(f"Analyzing {len(df)} reviews..."):
            model = load_model()
            results = model(df["review"].tolist())

        df["sentiment"] = [r["label"] for r in results]
        df["confidence"] = [round(r["score"] * 100, 1) for r in results]

        st.dataframe(df)

        positive = len(df[df["sentiment"] == "POSITIVE"])
        negative = len(df[df["sentiment"] == "NEGATIVE"])

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Positive reviews", positive)
        with col2:
            st.metric("Negative reviews", negative)

        st.download_button("Download results as CSV", df.to_csv(index=False), "results.csv", "text/csv")