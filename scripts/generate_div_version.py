import streamlit as st
import argparse, json, time
import google.generativeai as genai


def generate_definition_gemini(orig_text: str, modifier: str) -> dict:

    api_key = st.secrets["API_KEY"]

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-2.0-flash-lite", system_instruction="Du bist ein Assistent, der dabei helfen soll, eine E-Mail umzuschreiben um diverse Versionen desselben Inhalts zu bekommen.",)

    prompt = "Formuliere die folgende E-Mail bitte um, sodass der Wortlaut abgeändert ist, aber der Inhalt gleich bleibt. Gebe als Antwort nur die geänderte E-Mail. Das hier ist die originale:\n"
    response = model.generate_content(prompt + orig_text)

    return response.text