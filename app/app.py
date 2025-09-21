import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.pipeline import AnimeRecommenderPipeline
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Anime Recommender", page_icon=":books:", layout="wide")
st.title("Anime Recommender System")
st.write("Ask any question about anime and .pyget recommendations!")

@st.cache_resource
def get_pipeline():
    return AnimeRecommenderPipeline()
pipeline = get_pipeline() 
user_question = st.text_area("Enter your question about anime:", height=150)
if user_question:
    with st.spinner("Generating recommendations..."):
        try:
            recommendations = pipeline.recommend(user_question)
            st.subheader("Recommendations:")
            st.write(recommendations)
        except Exception as e:
            st.error(f"An error occurred: {e}")