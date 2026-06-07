
from services.exlporium import OceanService
from services.prospeo import ProspeoService
from services.brevo import BrevoService

from utils.validators import validate_domain


domain = input("Enter company domain: ")

if not validate_domain(domain):
    print("Invalid domain")
    exit()


ocean = OceanService()
prospeo = ProspeoService()
brevo = BrevoService()


companies = ocean.get_similar_companies(domain)

contacts = prospeo.find_decision_makers(companies)

print("\n✅ Contacts Found\n")

for contact in contacts:

    print(f"Name:   {contact.name}")
    print(f"Domain: {contact.company}")
    print(f"Email:  {contact.email}")
    print()


confirm = input("\nSend Emails? (y/n): ")

if confirm.lower() == "y":
    brevo.send_emails(contacts)
