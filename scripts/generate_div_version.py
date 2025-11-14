import streamlit as st
import argparse, json, time
import google.generativeai as genai


def generate_definition_gemini(orig_text: str) -> dict:

    api_key = st.secrets["API_KEY"]

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-2.5-flash-lite", system_instruction="Du bist ein Assistent, der dabei helfen soll, eine E-Mail umzuschreiben um diverse Versionen desselben Inhalts zu bekommen.",)

    prompt = "Formuliere die folgende E-Mail bitte um, sodass der Wortlaut abgeändert ist, aber der Inhalt gleich bleibt. Gebe als Antwort in der ersten Zeile den Betreff und ab der zweiten Zeile die E-Mail, nichts anderes. Das hier ist die originale:\n"
    response = model.generate_content(prompt + orig_text)

    subject, email = response.text.split("\n")[0], "\n".join(response.text.split("\n")[1:])
    return subject, email