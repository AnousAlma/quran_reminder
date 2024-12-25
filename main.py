import pandas as pd
from emailing import send_email
from datetime import date

SHEET_ID = "15yQvQxijxx2P30EYxyPebOLZBKuWArAKkktIs67ND9I"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
RECEIVER = "anaskhaldoun2@gmail.com"

def load_df(url):
    parse_dates= ['last_date']
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        days_left = (row["last_date"].date() - present).days + 7
        send_email(RECEIVER, row["surah"], days_left)
        email_counter += 1

    return email_counter

if __name__ == "__main__":
    df = load_df(URL)
    email_counter = query_data_and_send_emails(df)
    print(f"{email_counter} emails sent successfully.")