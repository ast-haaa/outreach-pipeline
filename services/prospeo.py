import requests

from config import PROSPEO_API_KEY
from utils.logger import log
from models.contact import Contact


class ProspeoService:

    SEARCH_URL = "https://api.prospeo.io/search-person"
    ENRICH_URL = "https://api.prospeo.io/enrich-person"

    def find_decision_makers(self, domains):

        log("Finding decision makers")

        contacts = []

        headers = {
            "X-KEY": PROSPEO_API_KEY,
            "Content-Type": "application/json"
        }

        for domain in domains:

            search_payload = {
                "page": 1,
                "filters": {
                    "company": {
                        "websites": {
                            "include": [domain]
                        }
                    }
                }
            }

            try:

                search_response = requests.post(
                    self.SEARCH_URL,
                    headers=headers,
                    json=search_payload,
                    timeout=30
                )

                search_data = search_response.json()

                if search_data.get("error"):
                    continue

                results = search_data.get("results", [])

                if not results:
                    continue

                first = results[0]
                person = first.get("person", {})
                person_id = person.get("person_id")

                email = None

                if person_id:

                    log("Enriching contact emails")

                    enrich_payload = {
                        "only_verified_email": True,
                        "data": {
                            "person_id": person_id
                        }
                    }

                    enrich_response = requests.post(
                        self.ENRICH_URL,
                        headers=headers,
                        json=enrich_payload,
                        timeout=30
                    )

                    enrich_data = enrich_response.json()

                    if not enrich_data.get("error"):

                        enrich_person = enrich_data.get(
                            "person",
                            {}
                        )

                        email_data = enrich_person.get(
                            "email",
                            {}
                        )

                        email = email_data.get("email")

                contacts.append(
                    Contact(
                        name=person.get(
                            "full_name",
                            "Unknown"
                        ),
                        title=person.get(
                            "current_job_title",
                            "Unknown"
                        ),
                        company=domain,
                        linkedin_url=person.get(
                            "linkedin_url",
                            ""
                        ),
                        email=email
                    )
                )

            except Exception as e:
                print(e)

        return contacts