import os
from dotenv import load_dotenv

load_dotenv()

EXPLORIUM_API_KEY = os.getenv("EXPLORIUM_API_KEY")
PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")
EAZYREACH_CLIENT_ID = os.getenv("EAZYREACH_CLIENT_ID")
EAZYREACH_CLIENT_SECRET = os.getenv("EAZYREACH_CLIENT_SECRET")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")