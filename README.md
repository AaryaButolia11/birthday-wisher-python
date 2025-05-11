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

## 🔧 Project Structure
birthday-wisher/
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
