import streamlit as st
import urllib.parse as up
from scripts.generate_div_version import generate_definition_gemini
from scripts.read_excel import get_email_dict

st.session_state.page = "main_page"
st.session_state.text = "original"

email_dict = get_email_dict()

with open("vorlage.txt", "r") as vl:
    template = vl.readlines()
subject = template[0].strip()
template_str = "> ".join(template[2:])
original_str = "\n".join(template[2:])
new_template = "\n".join(template[2:])

st.markdown("""
    # Herzlich Wilkommen!

    Du willst eine personalisierte E-Mail schreiben? Dann bist du bei unserem Tool hier richtig!\n\n
    """)

col = st.columns([0.3, 0.3, 0.4],gap="small")

with col[0]:
    if st.button("Neue Version generieren"):
        subject, new_template = generate_definition_gemini("\n".join(template))
        st.session_state.text = "changed"
with col[1]:
    if st.button("Originalen Text anzeigen"):
        st.session_state.text = "original"
        new_template = original_str

if st.session_state.text == "changed":
    st.markdown("> " + "\n>".join(new_template.split("\n")))
else:
    st.markdown("> " + template_str)


option = st.selectbox(
    "Wem möchtest du eine E-Mail schreiben?",
    list(email_dict.keys()),
    index=None,
    placeholder="Ausklappen zum Auswählen",
)


if option:
    new_template = new_template.replace("[NAME]", option.split(" (")[0])

    # encode everything that goes into the URL
    mail_content = (
        f"mailto:{email_dict[option]}"
        f"?subject={up.quote(subject, safe='')}"
        f"&body={up.quote(new_template, safe='')}"   # encodes quotes and newlines to %0A
    )

    st.markdown("""
    <style>
    .btn {
      display: inline-block;
      padding: 8px 16px;
      background-color: #007bff;
      color: #ffffff !important;
      text-decoration: none;
      border-radius: 4px;
      font-family: sans-serif;
      opacity: 1 !important;
    }
    .btn:hover {
      background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'<a href="{mail_content}" class="btn">Mail öffnen</a>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .btn {
      display: inline-block;
      padding: 8px 16px;
      background-color: #007bff;
      color: #ffffff !important;
      text-decoration: none;
      border-radius: 4px;
      font-family: sans-serif;
      opacity: 0.5 !important;
    }
    .btn:hover {
      background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'<a class="btn">Mail öffnen</a>', unsafe_allow_html=True)