
import smtplib
from email.mime.text import MIMEText
from config import SENDER_EMAIL, PASSWORD

def send_otp_email(recipient_email, subject, otp):
    """
    Sends an email with the OTP to the specified recipient.
    """

    message = MIMEText(f"Your OTP is: {otp}")
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(SENDER_EMAIL, [recipient_email], message.as_string())
        print("OTP email sent successfully!")
    except Exception as e:
        print(f"Error sending OTP email: {e}")

if __name__ == "__main__":
    # Example usage:
    # You will need to create a .env file with your SENDER_EMAIL and PASSWORD
    send_otp_email("recipient@example.com", "Your OTP Code", "123456")
