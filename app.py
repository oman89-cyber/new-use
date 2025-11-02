import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="News Research Assistant", page_icon="📰")

st.title("🤖 My News Research Assistant")
st.write("Hello! I'm your AI research helper for news analysis")

# Sample data for demo
sample_news = [
    {"title": "AI in Education", "sentiment": "positive", "date": "2024-01-15"},
    {"title": "New Tech Gadgets", "sentiment": "positive", "date": "2024-01-14"},
    {"title": "Climate Change News", "sentiment": "neutral", "date": "2024-01-13"}
]

# User input
topic = st.text_input("🔍 What topic do you want to research?", "technology")

if st.button("Research Now!"):
    st.success(f"Researching: {topic}")
    
    # Show sample results
    st.subheader("📊 Research Results")
    
    for news in sample_news:
        st.write(f"- {news['title']} ({news['sentiment']})")
    
    # Simple chart
    chart_data = pd.DataFrame({
        'sentiment': ['positive', 'neutral', 'negative'],
        'count': [2, 1, 0]
    })
    
    fig = px.pie(chart_data, values='count', names='sentiment', title='Sentiment Analysis')
    st.plotly_chart(fig)

st.info("Made by a 15-year-old student! 🎓")
