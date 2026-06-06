from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    title: str
    company: str
    linkedin_url: str
    email: str = None