import smtplib
from email.mime.text import MIMEText

# Email credentials
sender_email = "example@gmail.com"
password = "app_password"

def send_mail(i,email):
    receiver_email = email

    # Email content
    subject = "Incomplete Task Reminder"
    body = f"This email is from task manager regarding an incomplete task.\nTask details:\nTitle:{i[1]}, Category:{i[2]}, Priority:{i[3]}, Deadline:{i[4]}"

    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    try:
        # Connect to the email server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP server
        server.starttls()  # Start TLS for security
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")