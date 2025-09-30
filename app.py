
import streamlit as st
from scripts.generate_div_version import generate_definition_gemini

st.session_state.page = "main_page"

with open("vorlage.txt", "r") as vl:
    template = vl.read()
st.markdown("""
    # Herzlich Wilkommen!
            
    Du willst eine personalisierte E-Mail schreiben? Dann bist du bei unserem Tool hier richtig!\n\n
    Das hier ist der originale Text:\n\n
    """)

st.markdown("<blockquote>\n" + template + "\n</blockquote>")

if st.button("Neue Version generieren"):
    
    new_template = generate_definition_gemini(template)
    st.write("> " + new_template)