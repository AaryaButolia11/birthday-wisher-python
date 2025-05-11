# 🎉 Automated Birthday Wisher (Python)

A simple and customizable Python script that automatically sends birthday wishes via email using SMTP. This script runs daily (scheduled on PythonAnywhere) and sends a personalized email to anyone whose birthday matches the current date.

---

## ✨ Features

- 🗓 Automatically checks birthdays daily
- 📬 Sends personalized birthday emails using Gmail SMTP
- 📁 Uses customizable message templates
- 🔒 Keeps your credentials safe using environment variables
- ☁️ Hosted and scheduled to run daily via PythonAnywhere

---

## 🚀 Tech Stack

| Tech              | Purpose                                      |
|-------------------|----------------------------------------------|
| Python 3          | Core programming language                    |
| pandas            | Reading and managing CSV data                |
| smtplib           | Sending emails via Gmail SMTP                |
| datetime          | Working with current date and time           |
| random            | Randomly selecting letter templates          |
| dotenv (optional) | Loading environment variables securely       |
| PythonAnywhere    | Hosting and scheduling the automation        |
| Anaconda          | Environment and package management           |

---
## Screenshot of mail recieved 
![WhatsApp Image 2025-05-12 at 01 36 22_65044fe1](https://github.com/user-attachments/assets/b85020d6-570a-4444-8647-ccf9b6480019)


---
## 🔧 Project Structure
birthday-wisher/<br>
│<br>
├── birthdays.csv # List of birthdays (name, email, date)<br>
├── main.py # Main script that runs daily<br>
├── .env # Stores secure credentials (not committed)<br>
├── letter_templates/<br>
│ ├── letter_1.txt<br>
│ ├── letter_2.txt<br>
│ └── letter_3.txt<br>
├── requirements.txt # Required Python packages<br>
└── README.md # This file<br>


---

## 📁 Sample CSV Format (`birthdays.csv`)

```
name,email,year,month,day
Alex,alex.doe@example.com,1990,05,12
Jamie,jamie.smith@example.com,1985,11,18
Taylor,taylor.jordan@example.com,1977,08,30
Morgan,morgan.lee@example.com,1972,09,21
```

## ⚙️ Setup Instructions (Local)

#### Clone the repository
```
git clone https://github.com/yourusername/birthday-wisher.git
cd birthday-wisher
```
#### Install dependencies
```
pip install pandas
```
#### Add credentials to environment variables

Create a .env file (do not upload it to GitHub):
```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```
#### Run the script manually
```
python main.py
```

## Hosting on PythonAnywhere (Scheduled Daily at 12 PM)
You can host and run this project for free on PythonAnywhere:

Create an account and upload your project.

Navigate to the Tasks tab.

Schedule your script (e.g., main.py) to run at 12:00 PM every day.

Make sure your Python version matches the one used in Anaconda (Python 3.10 or 3.11).

Set up environment variables in the PythonAnywhere dashboard or use .env.

## 🧠 How It Works
Loads today's date and compares it to the birthday entries.

If a match is found, it picks a random letter template.

Replaces [NAME] in the template with the actual name.

Sends the email using Gmail’s SMTP server.
