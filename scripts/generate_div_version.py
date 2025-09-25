import streamlit as st
import argparse, json, time
import google.generativeai as genai


def generate_definition_gemini(orig_text: str) -> dict:

    with open("../../../../.api", 'r') as af:
        api_keys = af.readlines()

    api_key = api_keys[2].split('\t')[-1].strip() 

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-2.0-flash-lite", system_instruction="Du bist ein Assistent, der dabei helfen soll, eine E-Mail umzuschreiben um diverse Versionen desselben Inhalts zu bekommen.",)

    response = model.generate_content(orig_text)

    return response.text