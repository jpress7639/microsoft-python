# Email automation with Python: Sending and receiving emails

# Python's smtplib and imaplib libraries

# The power of smtplib
# Python's built-in library for sending emails, smtplib, 
# provides a straightforward interface to interact with Simple Mail Transfer Protocol (SMTP) servers.
 
# With smtplib, you can craft emails dynamically, including customer names, order details, and even tracking information.
# This powerful library acts as your direct line to SMTP servers, the backbone of email delivery across the internet.

# Sending customized emails
# At the heart of smtplib lies the SMTP class
# the SMTP class is your trusty postal carrier
# Once the connection is established, you utilize methods like sendmail to actually transmit your email.

# Code Example
import smtplib

# Replace with your email provider's SMTP server and your credentials
smtp_server = "smtp.your_email_provider.com"
smtp_port = 587 # Or the appropriate port for your provider
sender_email = "your_email@example.com"
sender_password = "your_password"

receiver_email = "recipient@example.com"
message = f"""\
Subject: Hello from Python

This is a test email sent from Python."""

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() # Secure the connection
    server.login(sender_email, sender_password)  
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except Exception as e: 
    print(f"Error sending email: {e}")
finally:
    server.quit()

# However, smtplib allows you to create more complex emails with HTML formatting, embedded images, and attachments.

# Constructing Email Messages with MIMEText
# When sending emails, especially those that need a structured format (like a subject, sender, and recipient), 
# it's best to use Python's email.mime.text.MIMEText class.

# Code Example

from email.mime.text import MIMEText

# 1. Create the MIMEText object with the email body
message = MIMEText("This is the email body.")

# 2. Set the email headers like a dictionary
# The 'Subject' header defines the email's subject line.
message['Subject'] = "Your Custom Subject Here"

# The 'From' header specifies the sender's email address.
message['From'] = "sender@example.com"

# The 'To' header specifies the recipient's email address.
message['To'] = "recipient@example.com"

# Once configured, this 'message' object can be sent using server.send_message(message)
# from your smtplib.SMTP connection.

# The versatility of imaplib
# imaplib gives you the power to manage and interact with your inbox directly
# It's like having a remote control for your email

# imaplib as your personal email assistant, diligently working behind the scenes to help you stay organized

# Fetching and managing emails
# The IMAP4_SSL class within imaplib is your key to establishing a secure and encrypted connection to your email server.
# ensures that your sensitive information, such as your login credentials and email content, remains protected

# the "select" method allows you to choose a specific mailbox
# "search" method empowers you to find specific emails based on a variety of criteria, 
# including the sender, subject, date, or even keywords within the email body

# Code Example: 

import imaplib

# Replace with your email provider's IMAP server and your credentials
imap_server = "imap.your_email_provider.com"
imap_port = 993 # Or the appropriate port for your provider
email_address = "your_email@example.com"
email_password = "your_password"

try:
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    mail.select("Inbox")

    status, messages = mail.search(None, "UNSEEN")
    if status == "OK":
        for num in messages[0].split():
   # Fetch the complete email data 
   # (including headers and body) for each message
   # The data is fetched in RFC822 format, a text message standard
            status, data = mail.fetch(num, "(RFC822)")
            if status == "OK":
                # Process the email data (data[0][1]) here
                print("Fetched an unread email")
    else:
        print("Error searching for unread emails")

except Exception as e:
    print(f"Error fetching emails: {e}")
finally:
    # Close the connection and log out of the mail server
    mail.close()
    mail.logout()

# Once you have fetched emails, you can parse their content using libraries like email

# Real-life applications
# With email automation, you can
# can collect the necessary data, generate a visually appealing report using a library like matplotlib, 
# and then automatically email it to the relevant recipients

# Customer Support 
# you can employ imaplib to identify urgent messages based on specific keywords or senders, 
# and then trigger automated acknowledgments to let customers know their inquiry has been received

# Social Media
# You can set up a script to periodically check your social media accounts for new mentions or messages

# Best practices and considerations
# Robust error handling should be a top priority. 
# Network hiccups, incorrect login credentials, or unexpected email formats can all disrupt your automation scripts
# By implementing comprehensive error handling, providing informative messages 

# Security is paramount when dealing with email automation

# Be aware of your email provider's rate limits
# NOTE: One effective strategy is to leverage the time.sleep() function before each email loop in your script.
# introduces a deliberate pause, allowing you to control the pace of your email sending and stay well within the rate limits imposed by your provider

# Coding challenge: Send a confirmation email and check for replies

import smtplib
from email.mime.text import MIMEText
import imaplib

smtp_server = "smtp.example.com"
smtp_port = 587
imap_server = "imap.example.com"
imap_port = 993
email_user = "orders@example.com"
email_password = "Coursera1000!"

def send_confirmation_email(client_email, client_name):
    message = MIMEText(f"Thank you for your order, {client_name}!")
    message['Subject'] = "Order Confirmation"
    message['From'] = email_user
    message['To'] = client_email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(message)
            print(f"Sent confirmation email to {client_name}!")  # ✅
    except Exception as e:
        print(f"Error sending email: {e}")

def check_new_messages(client_email, client_name):
    try:
        with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
            mail.login(email_user, email_password)
            mail.select('inbox')

            status, responses = mail.search(None, '(UNSEEN FROM "%s")' % client_email)
            if status == "OK":
                for num in responses:
                    print(f"Fetched unread email from {client_name}")
            else:
                print("No new messages yet.")  # ✅
    except Exception as e:
        print(f"Error: {e}")


client_email = "john.smith@example.com"
client_name = "John Smith"
send_confirmation_email(client_email, client_name)
check_new_messages(client_email, client_name)