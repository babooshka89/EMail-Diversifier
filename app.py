
import streamlit as st
from scripts.generate_div_version import generate_definition_gemini

st.session_state.page = "main_page"

st.markdown("""
    # Herzlich Wilkommen!
            
    Du willst eine personalisierte E-Mail schreiben? Dann bist du bei unserem Tool hier richtig! 
    """
)
if st.button("Neue Version generieren"):
    with open("vorlage.txt", "r") as vl:
        template = vl.read()
    new_template = generate_definition_gemini(template)
    st.write(new_template)