import requests

from utils.logger import log
from config import EXPLORIUM_API_KEY


class OceanService:

    MATCH_URL = "https://api.explorium.ai/v1/businesses/match"

    def get_similar_companies(self, domain):

        log(f"Matching business {domain}")

        headers = {
            "Content-Type": "application/json",
            "api_key": EXPLORIUM_API_KEY
        }

        payload = {
            "businesses_to_match": [
                {
                    "domain": domain
                }
            ]
        }

        response = requests.post(
            self.MATCH_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        print(response.status_code)
        print(response.json())

        return [domain]