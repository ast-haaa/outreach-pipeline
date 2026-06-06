import requests

from config import BREVO_API_KEY
from utils.logger import log


class BrevoService:

    URL = "https://api.brevo.com/v3/smtp/email"

    def send_emails(self, contacts):

        log("Sending emails")

        headers = {
            "accept": "application/json",
            "api-key": BREVO_API_KEY,
            "content-type": "application/json"
        }

        for contact in contacts:

            if not contact.email:
                continue

            payload = {
                "sender": {
                    "name": "Astha",
                    "email": "hello@asthadev.xyz"
                },
                "to": [
                    {
                        "email": contact.email,
                        "name": contact.name
                    }
                ],
                "subject": "Quick Introduction",
                "htmlContent": f"""
                <html>
                    <body>
                        <p>Hi {contact.name},</p>

                        <p>
                        I came across {contact.company}
                        and wanted to connect.
                        </p>

                        <p>
                        Looking forward to hearing from you.
                        </p>

                        <p>
                        Regards,<br>
                        Astha
                        </p>
                    </body>
                </html>
                """
            }

            try:

                response = requests.post(
                    self.URL,
                    headers=headers,
                    json=payload,
                    timeout=30
                )

                print(
                    contact.email,
                    response.status_code
                )

            except Exception as e:

                print(e)