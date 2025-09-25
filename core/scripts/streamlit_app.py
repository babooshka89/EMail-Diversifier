import streamlit as st
import argparse, json, time
import google.generativeai as genai
from openai import OpenAI
from basics import generate_test_targets
# Use a pipeline as a high-level helper
from transformers import pipeline


def generate_definition_gemini(request_list: list, api_file: str, ne: bool=False, omit_example: bool=False) -> dict:

    with open(api_file, 'r') as af:
        api_keys = af.readlines()

    api_key = api_keys[2].split('\t')[-1].strip() 

    genai.configure(api_key=api_key)

    if ne:
        model = genai.GenerativeModel("models/gemini-2.0-flash", system_instruction="You are a trying to provide the reader with additional information about the entity at hand.",)
    else:
        model = genai.GenerativeModel("models/gemini-2.0-flash", system_instruction="You are a lexicographer familiar with providing concise definitions of word meanings in context.",)

    definition_list = []

    for i, request in enumerate(request_list):
        response = model.generate_content(request)
        if ne:
            if omit_example:
                definition_list.append({'target': request.split('?')[0][15:], 'generated_text': response.text})
            else:
                definition_list.append({'target': request.split('?')[0][15:], 'usage_example': request.split('Usage example: ')[1].strip(), 'generated_text': response.text})
        else:
            definition_list.append({'target': request.split('?')[0][26:], 'usage_example': request.split('Usage example: ')[1].strip(), 'generated_text': response.text})
    
        if i % 10 == 0:
            print('Request {} from {}'.format(str(i), len(request_list)))
        
        time.sleep(6)
    return definition_list