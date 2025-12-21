import streamlit as st
import urllib.parse as up
from scripts.generate_div_version import generate_definition_gemini
from scripts.read_excel import get_email_dict

st.session_state.page = "main_page"
st.session_state.text = "original"
if 'addressee' not in st.session_state:
    st.session_state.addressee = False

def click_button_circus():
    st.session_state.addressee = "circus"

def click_button_politics():
    st.session_state.addressee = "politics"

st.markdown("""
    # E-Mails gegen Tierzirkusse
    
    In Nürnberg gastiert derzeit erneut der Circus Barnum. Viele Menschen möchten ihre Haltung zu Tierauftritten und der vermeidbaren Nutzung fühlender Lebewesen zur bloßen Unterhaltung äußern oder die lokale Politik darauf aufmerksam machen, dass zeitgemäße Formen des Zirkus längst ohne Tiere auskommen.

    Lasst uns gemeinsam ein Zeichen setzen und dafür sorgen, dass solche veralteten Praktiken in unserer Stadt keinen Platz mehr haben! Zeigen wir, dass dieses Thema vielen Bürger:innen am Herzen liegt.
    Mithilfe dieser Seite kannst du ganz einfach eine E-Mail an den Zirkus selbst oder an Politiker:innen im Stadtrat Nürnberg verfassen und abschicken. 

    Damit du nicht selber lange überlegen musst, was du schreiben möchtest, haben wir Vorlagen erstellt, die du nutzen kannst. Du kannst den Text außerdem mithilfe des KI-gestützten Generators ein wenig umschreiben lassen. So bekommen die Empfänger:innen viele individuelle Nachrichten und nicht immer denselben Text zugeschickt. Du kannst den Text in deinem E-Mail-Programm natürlich auch noch weiter anpassen, bevor du die Mail abschickst.
    Achte bitte darauf, Kritik stets respektvoll und sachlich zu äußern. Höflich formulierte Nachrichten werden eher gelesen, ernst genommen und können mehr bewirken als scharfe Töne.\n\n
            
    Danke für dein Engagement! 
    ### Wem möchtest du schreiben?
    """)

col = st.columns([0.3, 0.4, 0.3],gap="small")

with col[0]:
    st.button("Mail an Circus Barnum", on_click=click_button_circus)

with col[1]:
    st.button("Mail an Nürnbergs Politiker:innen", on_click=click_button_politics)


if st.session_state.addressee == "circus":
    with open("vorlage_zirkus.txt", "r") as vl:
        template = vl.readlines()

    subject = template[0].strip()
    template_str = "> ".join(template[2:])
    original_str = "\n".join(template[2:])
    new_template = "\n".join(template[2:])


    circus_col = st.columns([0.3, 0.3, 0.4],gap="small")

    with circus_col[0]:
        if st.button("Neue Version generieren"):
            subject, new_template = generate_definition_gemini("\n".join(template))
            st.session_state.text = "changed"
    with circus_col[1]:
        if st.button("Originalen Text anzeigen"):
            st.session_state.text = "original"
            new_template = original_str

    if st.session_state.text == "changed":
        st.markdown("> " + "\n>".join(new_template.split("\n")))
    else:
        st.markdown("> " + template_str)

    
    mail_content = (
            "mailto:circus.barnum@gmail.com"
            f"?subject={up.quote(subject, safe='')}"
            "&amp;bcc=info@veganvernetzt.de"
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


elif st.session_state.addressee == "politics":

    with open("vorlage_politik.txt", "r") as vl:
        template = vl.readlines()

    email_dict = get_email_dict()

    subject = template[0].strip()
    template_str = "> ".join(template[2:])
    original_str = "\n".join(template[2:])
    new_template = "\n".join(template[2:])

    politics_col = st.columns([0.3, 0.3, 0.4],gap="small")
    
    with politics_col[0]:
        if st.button("Neue Version generieren"):
            subject, new_template = generate_definition_gemini("\n".join(template))
            st.session_state.text = "changed"
    with politics_col[1]:
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
            "&amp;cc=circus.barnum@gmail.com"
            "&amp;bcc=info@veganvernetzt.de"
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