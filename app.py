
import streamlit as st
from scripts.generate_div_version import generate_definition_gemini

st.session_state.page = "main_page"

with open("vorlage.txt", "r") as vl:
    template = vl.read()
st.markdown("""
    # Herzlich Wilkommen!
            
    Du willst eine personalisierte E-Mail schreiben? Dann bist du bei unserem Tool hier richtig!\n\n
    Das hier ist der originale Text:\n\n    
    """
)
st.markdown(f"""
<div style="border:1px solid #ddd; border-radius:5px; padding:10px; background:#f7f7f7; font-family: monospace; white-space: pre-wrap; word-wrap: break-word;">
  <button onclick="navigator.clipboard.writeText(`{template}`)" style="float:right; margin:2px;">Copy</button>
  {template}
</div>
""", unsafe_allow_html=True)
if st.button("Neue Version generieren"):
    
    new_template = generate_definition_gemini(template)
    st.write(new_template)