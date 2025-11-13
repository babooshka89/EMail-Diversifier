import streamlit as st
import urllib.parse as up
from scripts.generate_div_version import generate_definition_gemini

st.session_state.page = "main_page"

with open("vorlage.txt", "r") as vl:
    template = vl.readlines()
subject = template[0].strip()
template_str = "> ".join(template[2:])
new_template = "\n".join(template[2:])

st.markdown("""
    # Herzlich Wilkommen!
            
    Du willst eine personalisierte E-Mail schreiben? Dann bist du bei unserem Tool hier richtig!\n\n
    """)

if st.button("Neue Version generieren"):
    
    subject, new_template = generate_definition_gemini("\n".join(template))
    st.markdown("> " + "\n>".join(new_template.split("\n")))
else:
    st.markdown("> " + template_str)
if st.button("Originalen Text anzeigen"):
    st.markdown("> " + template_str)

placeholder = "erika.mustermann@webmail.de"
text_input = st.text_input(
        "Deine Email-Adresse:",
        placeholder=placeholder,
    )

# encode everything that goes into the URL
mail_content = (
    f"mailto:{text_input}"
    f"?subject={up.quote(subject, safe='')}"
    f"&body={up.quote(new_template, safe='')}"   # encodes quotes and newlines to %0A
)

# mail_content = f"mailto:{text_input}?subject={subject}&body={new_template}"

st.markdown("""
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

st.markdown(f'<a href="{mail_content}" class="btn">Mail öffnen</a>', unsafe_allow_html=True)
