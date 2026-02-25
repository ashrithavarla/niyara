import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings
from app.models.contact_form import ContactFormDTO


class EmailService:
    def send_contact_form_email(self, form_data: ContactFormDTO) -> None:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Contact Form: {form_data.reason}"
        msg["From"] = settings.MAIL_USERNAME
        msg["To"] = form_data.recipient_email

        html_body = f"""
        <html><body>
            <h2>New Contact Form Submission</h2>
            <p><strong>Name:</strong> {form_data.name}</p>
            <p><strong>Email:</strong> {form_data.email}</p>
            <p><strong>Contact Number:</strong> {form_data.contact_number or "N/A"}</p>
            <p><strong>City:</strong> {form_data.city or "N/A"}</p>
            <p><strong>Reason:</strong> {form_data.reason}</p>
            <p><strong>Message:</strong> {form_data.message}</p>
        </body></html>
        """

        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(settings.MAIL_HOST, settings.MAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
            server.sendmail(settings.MAIL_USERNAME, form_data.recipient_email, msg.as_string())


# Singleton instance
email_service = EmailService()
