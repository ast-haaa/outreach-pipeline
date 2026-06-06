from utils.logger import log


class EazyreachService:

    def resolve_emails(self, contacts):

        log("Resolving emails")

        for contact in contacts:

            contact.email = (
                f"{contact.name.lower().replace(' ', '')}"
                f"@{contact.company}"
            )

        return contacts