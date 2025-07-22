import streamlit as st
from model import recommend_talks

st.set_page_config(page_title="TED Talk Recommender", layout="wide")

st.markdown("<h1><span style='color:red'>TED Talk</span> Recommender</h1>", unsafe_allow_html=True)
user_input = st.text_area("Enter a TED Talk topic idea:", height=100)

if st.button("Get Recommendations") and user_input.strip():
    with st.spinner("Finding similar talks..."):
        results = recommend_talks([user_input])
        st.subheader("Top 5 Similar TED Talks:")
        for rec in results:
            st.markdown(f"**{rec['main_speaker']}** — {rec['details']}")
else:
    st.info("Enter a topic idea and click the button to get recommendations.")
