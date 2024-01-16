from dotenv import load_dotenv
load_dotenv() #load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get responses
# For text we use - gemini-pro
# For vision we use - gemini_pro_vision

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title = "Q&A Demo")

st.header("Gemini Chatbot")

input=st.text_input("Input: " , key="input")
submit=st.button("Ask the question")


# When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)


