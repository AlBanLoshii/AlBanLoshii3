import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                print(f"Email sent successfully to {recipient_email}")
        except smtplib.SMTPException as e:
            print(f"An error occurred while sending the email: {e}")

def main():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'sender@example.com'
    sender_password = 'password'
    recipient_email = 'recipient@example.com'
    subject = 'Hello!'
    message = 'This is a test email.'

    sender = EmailSender(smtp_server, smtp_port, sender_email, sender_password)
    sender.send_email(recipient_email, subject, message)

if __name__ == "__main__":
    main()
