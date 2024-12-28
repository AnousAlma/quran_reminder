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
    surahs = 0
    data = {}
    body = ""
    for _, row in df.iterrows():
        days_left = (row["last_date"].date() - present).days + 7
        data[row["surah"]] = days_left
        if days_left >= 4:
            emoji = "🟢"
        elif days_left >= 1:
            emoji = "🟡"
        else:
            emoji = "🚨"
        
        body = f"{body}{emoji} Surah: {row['surah']}, Days left: {days_left}\n\n"
        surahs += 1
    
    most_urgent_surah = min(data, key=data.get)
    send_email(RECEIVER, most_urgent_surah, data[most_urgent_surah], body)

    return surahs

if __name__ == "__main__":
    df = load_df(URL)
    email_counter = query_data_and_send_emails(df)
    print(f"Reminder for {email_counter} surahs sent.")