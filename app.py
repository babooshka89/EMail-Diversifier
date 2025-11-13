import streamlit as st
from scripts.generate_div_version import generate_definition_gemini

st.session_state.page = "main_page"

with open("vorlage.txt", "r") as vl:
    template = vl.readlines()
template_str = "> ".join(template)

st.markdown("""
    # Herzlich Wilkommen!
            
    Du willst eine personalisierte E-Mail schreiben? Dann bist du bei unserem Tool hier richtig!\n\n
    """)

if st.button("Neue Version generieren"):
    
    new_template = generate_definition_gemini("\n".join(template))
    st.markdown("> " + "\n>".join(new_template.split("\n")))
elif st.button("Originalen Text anzeigen"):
    st.markdown("> " + template_str)
else:
    st.markdown("> " + template_str)

st.markdown("""
<a href="mailto:fritz.eierschale@example.org?subject=Hallo%20Welt&body=Hallo,%20das%20ist%20ein%20Test!" class="btn">Mail öffnen</a>

<style>
.btn {
  display: inline-block;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-family: sans-serif;
}
.btn:hover {
  background-color: #0056b3;
}
</style>
""", unsafe_allow_html=True)