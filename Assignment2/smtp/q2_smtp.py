# smtp_client.py - Ethereal SMTP
import smtplib
from email.mime.text import MIMEText

# Ethereal credentials
# SENDER_EMAIL = "kaya.ryan62@ethereal.email"
# RECEIVER_EMAIL = "kaya.ryan62@ethereal.email"
# PASSWORD = "AWcs4cN9ENdB9Ey7kj"  # Ethereal account password
SENDER_EMAIL = "sahajasreemeruva@gmail.com"
RECEIVER_EMAIL = "meruvasahajasree@gmail.com"
PASSWORD = "udzu nrjy wpyn lusf"  # Ethereal account password

def send_email(sender, receiver, password):
    """Send a test email via Ethereal SMTP."""
    try:
        # Create email message
        msg = MIMEText("Hello! This is a test email from Python (Ethereal test).")
        msg["Subject"] = "CN Assignment_02 SMTP Email"
        msg["From"] = sender
        msg["To"] = receiver
        # Connect to Ethereal SMTP server
        # server = smtplib.SMTP("smtp.ethereal.email", 587)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.set_debuglevel(1)  # Uncomment to log communication
        server.starttls()  # secure connection
        server.login(sender, password)
        # Send email
        server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully! Check inbox.")

        server.quit()
    except Exception as e:
        print("Error:", e)

def main():
    send_email(SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD)

if __name__ == "__main__":
    main()
