import streamlit as st
import google.generativeai as genai
import re
import pandas as pd

# Configuration for Google's generative AI
API_KEY = 'AIzaSyBrX0GtL5TqwCaVKQEldpQnlH2DVdFVX4I'  # Be sure to replace with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def remove_asterisks(text):
    """Remove all asterisks from the text."""
    return re.sub(r'\*', '', text)

def analyze_symptoms(symptoms):
    """Analyze symptoms using Gemini Pro model."""
    system_prompt = """
    Prompt for Medical Practitioners: Analyzing Disease Symptoms

    Objective: Evaluate patient symptoms to identify possible diseases or health issues.

    Tasks:

    Detailed Analysis: Thoroughly examine each symptom to detect any abnormalities or signs indicative of disease.
    Findings Report: Clearly document all abnormalities and disease signs identified during the analysis.
    Recommendations and Next Steps: Propose necessary further tests or medical evaluations to confirm the diagnosis or expand understanding of the symptoms.
    Treatment Suggestions: Based on the symptoms and findings, suggest potential treatment options or interventions.
    Guidelines:

    Scope: Ensure the analysis pertains only to human health issues.
    Clarity: If symptom details are insufficient for a definitive analysis, indicate this as a limitation in the findings.
   
    Purpose: This structured analysis supports clinical decision-making by providing a systematic approach to symptom evaluation.
    """
    chat = model.start_chat(history=[])
    response = chat.send_message(system_prompt + symptoms)
    return remove_asterisks(response.text)

# Streamlit UI
st.title("Symptom Analyzer")
symptoms = st.text_area("Enter your symptoms here:", height=150)
if st.button("Analyze Symptoms"):
    if symptoms:
        result = analyze_symptoms(symptoms)
        st.subheader("Analysis Results")
        st.write(result)
    else:
        st.error("Please enter some symptoms to analyze.")

# Disclaimer
# st.markdown("### Disclaimer")
# st.markdown("**Consult with a Doctor before making any decisions based on this analysis.**")



















# system_prompt="""
# Prompt for Medical Practitioners: Analyzing Disease Symptoms

# Objective: Evaluate patient symptoms to identify possible diseases or health issues.

# Tasks:

# Detailed Analysis: Thoroughly examine each symptom to detect any abnormalities or signs indicative of disease.
# Findings Report: Clearly document all abnormalities and disease signs identified during the analysis.
# Recommendations and Next Steps: Propose necessary further tests or medical evaluations to confirm the diagnosis or expand understanding of the symptoms.
# Treatment Suggestions: Based on the symptoms and findings, suggest potential treatment options or interventions.
# Guidelines:

# Scope: Ensure the analysis pertains only to human health issues.
# Clarity: If symptom details are insufficient for a definitive analysis, indicate this as a limitation in the findings.
# Disclaimer: Include a disclaimer advising patients to "Consult with a Doctor before making any decisions" when applicable.
# Purpose: This structured analysis supports clinical decision-making by providing a systematic approach to symptom evaluation.

# do not include * in the response
# """



# from fastapi import FastAPI
# from pydantic import BaseModel
# import os
# import google.generativeai as genai
# import re

# # from dotenv import load_dotenv

# def remove_asterisks(text):
#     # Use the regex sub() function to replace all asterisks with an empty string
#     cleaned_text = re.sub(r'\*', '', text)
#     return cleaned_text

# app= FastAPI()
# symptoms=input("Enter the symptoms")
# API_KEY = 'AIzaSyBU1BhybBEaYGRKM45KWvomihSXgYvV22U'

# genai.configure(
# api_key = API_KEY
# )

# model= genai.GenerativeModel('gemini-pro')
# chat=model.start_chat(history=[])



# response=chat.send_message(system_prompt+symptoms)

# print(remove_asterisks(response.text))




