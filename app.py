import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="News Research Assistant", page_icon="📰")

st.title("🤖 My News Research Assistant")
st.write("Hello! I'm your AI research helper for news analysis")

# Sample data
sample_data = {
    'Topic': ['AI in Education', 'Climate Change', 'Space Exploration'],
    'Sentiment': ['Positive', 'Neutral', 'Positive'],
    'Date': ['2024-01-15', '2024-01-14', '2024-01-13']
}

df = pd.DataFrame(sample_data)

# User input
topic = st.text_input("🔍 What topic do you want to research?", "technology")

if st.button("Research Now!"):
    st.success(f"Researching: {topic}")
    
    # Show results
    st.subheader("📊 Research Results")
    st.dataframe(df)
    
    # Simple bar chart
    st.subheader("📈 Sentiment Distribution")
    sentiment_count = df['Sentiment'].value_counts()
    st.bar_chart(sentiment_count)

st.info("Made by a 15-year-old student! 🎓")
