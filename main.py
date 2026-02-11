
import smtplib
from email.mime.text import MIMEText

def send_otp_email(recipient_email, subject, otp):
    """
    Sends an email with the OTP to the specified recipient.
    """
    sender_email = "your_email@example.com"  # Replace with your email
    password = "your_password"  # Replace with your password

    message = MIMEText(f"Your OTP is: {otp}")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, [recipient_email], message.as_string())
        print("OTP email sent successfully!")
    except Exception as e:
        print(f"Error sending OTP email: {e}")

if __name__ == "__main__":
    # Example usage:
    send_otp_email("recipient@example.com", "Your OTP Code", "123456")
