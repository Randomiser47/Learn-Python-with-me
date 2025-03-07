# Birthday Wisher Project

## Disclaimer
**Celebrating birthdays is not a part of Islam.** This project was purely made for practicing programming concepts such as working with dates, sending automated emails, and handling CSV files. It is not intended to promote birthday celebrations in any way.

## Project Overview
This Python project is designed to send automated emails to people on their birthdays. It reads a list of names, emails, and birthdates from a CSV file and checks if today's date matches any birthdays in the file. If a match is found, the program selects a random email template, replaces placeholders with the recipient's name, and sends an email.

## Features
- Reads birthday data from a CSV file
- Checks if today matches any stored birthdays
- Selects a random letter template
- Replaces placeholder text with the recipient's name
- Sends an automated email using SMTP

## Technologies Used
- Python
- Pandas (for handling CSV data)
- smtplib (for sending emails)
- datetime (for checking today's date)
- Random (for selecting email templates)

## How It Works
1. Load birthday data from `birthdays.csv`
2. Compare today's date with the stored birthdates
3. If a match is found:
   - Select a random email template
   - Replace `[NAME]` in the template with the recipient's name
   - Send an email to the recipient

## Important Note
This project was created strictly for educational purposes to practice Python programming skills. Any resemblance to an actual birthday wisher service is purely coincidental and unintentional.

