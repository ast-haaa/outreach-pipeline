from services.ocean import OceanService
from services.prospeo import ProspeoService
from services.eazyreach import EazyreachService
from services.brevo import BrevoService

from utils.validators import validate_domain


domain = input("Enter company domain: ")

if not validate_domain(domain):
    print("Invalid domain")
    exit()


ocean = OceanService()
prospeo = ProspeoService()
eazyreach = EazyreachService()
brevo = BrevoService()


companies = ocean.get_similar_companies(domain)

contacts = prospeo.find_decision_makers(companies)

contacts = eazyreach.resolve_emails(contacts)


print("\nContacts Found\n")

for contact in contacts:

    print(
        contact.name,
        contact.company,
        contact.email
    )


confirm = input(
    "\nSend Emails? (y/n): "
)

if confirm.lower() == "y":
    brevo.send_emails(contacts)