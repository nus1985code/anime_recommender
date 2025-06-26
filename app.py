# app.py
import streamlit as st
from recommender import get_tag_recommendations, df

st.set_page_config(page_title="🎌 Anime Recommender App", layout="centered")

# UI Styling
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to top left, #ffecd2, #fcb69f);
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }
    .title-style {
        font-size: 2.8em;
        font-weight: bold;
        color: #4B0082;
        text-shadow: 1px 1px 2px #999;
    }
    .sub-style {
        font-size: 1.2em;
        color: #333;
        margin-bottom: 2em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-style'>🎌 Anime Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-style'>Enter the name of your favorite anime to discover 10 similar ones!</p>", unsafe_allow_html=True)

# Input
anime_name = st.text_input("🔎 Search for an anime:")

if anime_name:
    recommendations, _ = get_tag_recommendations(anime_name)
    if isinstance(recommendations, str):
        st.error(f"🚫 {recommendations}")
    else:
        st.balloons()
        st.success(f"🎉 Top 10 Recommendations similar to '{anime_name}':")
        for i, name in enumerate(recommendations, 1):
            genre = df[df['name'] == name]['genre'].values
            genre_display = ', '.join(genre) if len(genre) > 0 else 'N/A'
            st.markdown(f"**{i}. {name}** ✨  \
*Genres:* _{genre_display}_")
