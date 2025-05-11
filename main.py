import datetime as dt
import pandas as pd
import random
import smtplib
import os

# ===================== CONFIGURATION =====================

# Use environment variables or a config file for security
MY_EMAIL = os.getenv("EMAIL_USER")         # e.g., yourname@gmail.com
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")   # app password or OAuth token

# File paths
BIRTHDAYS_CSV_PATH = "birthday_wisher/birthdays.csv"
TEMPLATE_PATH = "birthday_wisher/letter_templates"

# ==========================================================

# Get today's date as (month, day) tuple
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read birthday data
data = pd.read_csv(BIRTHDAYS_CSV_PATH)

# Create a dictionary with (month, day) as keys for fast lookup
birthdays_dict = {
    (row["month"], row["day"]): row
    for (_, row) in data.iterrows()
}

# Check if today matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Select a random letter template and personalize it
    template_file = f"{TEMPLATE_PATH}/letter_{random.randint(1,3)}.txt"
    with open(template_file) as file:
        contents = file.read()
        personalized_letter = contents.replace("[NAME]", birthday_person["name"])

    # Send the email via SMTP
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )

    print(f"Email sent to {birthday_person['name']} at {birthday_person['email']}")

