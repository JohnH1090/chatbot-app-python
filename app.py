import streamlit as st
from groq import Groq


# creates groq client

client = Groq(api_key=st.secrets.get("GROQ_API_KEY"))

# page header
st.title("Chatbot")
st.write("Chatbot powered by Groq")
st.divider()
