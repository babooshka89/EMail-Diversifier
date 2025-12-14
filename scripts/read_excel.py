import requests, os
from io import BytesIO
import msoffcrypto
import pandas as pd

def get_email_dict():
    # Nextcloud credentials
    username = os.getenv("USERNAME") 
    password = os.getenv("PASSWORD") 

    # WebDAV URL to your file
    url = os.getenv("URL")
    # Download from Nextcloud
    response = requests.get(url, auth=(username, password))

    if response.status_code != 200:
        raise Exception("Failed to download file:", response.status_code, response.text)

    # Read Excel directly
    df = pd.read_excel(BytesIO(response.content))

    # get columns from index
    all_names = [f"{df.columns[0]} ({df.columns[1]})"]
    all_emails = [df.columns[2]]
    names = [f"{name} ({list(df.iloc[:, 1])[i]})" for i, name in enumerate(list(df.iloc[:, 0]))]
    email = [str(email).strip() for email in list(df.iloc[:, 2])]
    all_names.extend(names)
    all_emails.extend(email)

    email_dict = {all_names[i]: all_emails[i] for i in range(len(names)) if not "AfD" in all_names[i]}

    return email_dict