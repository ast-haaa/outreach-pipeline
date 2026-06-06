import requests

from config import PROSPEO_API_KEY
from utils.logger import log
from models.contact import Contact


class ProspeoService:

    SEARCH_URL = "https://api.prospeo.io/search-person"

    def find_decision_makers(self, domains):

        log("Finding decision makers")

        contacts = []

        headers = {
            "X-KEY": PROSPEO_API_KEY,
            "Content-Type": "application/json"
        }

        for domain in domains:

            payload = {
                "page": 1,
                "filters": {
                    "company": {
                        "websites": {
                            "include": [
                                domain
                            ]
                        }
                    }
                }
            }

            try:

                response = requests.post(
                    self.SEARCH_URL,
                    headers=headers,
                    json=payload,
                    timeout=30
                )

                print("\nSEARCH STATUS:", response.status_code)
                print(response.text)

                data = response.json()

                if data.get("error"):
                    continue

                results = data.get("results", [])

                if not results:
                    continue

                first = results[0]

                person = first.get("person", {})

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
                        )
                    )
                )

            except Exception as e:

                print(e)

        return contacts