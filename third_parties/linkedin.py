from dotenv import load_dotenv
load_dotenv()

import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from Linkedin Profiles,
     Manually scraps the information form linkedin profile
    """
    profile_data = requests.get(
        "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
    ).json()

    return profile_data


def clean_linkedin_data(data: dict):
    cleaned_data = {
        k: v
        for k, v in data.items()
        if v and k != 'certifications'
    }
    return cleaned_data
