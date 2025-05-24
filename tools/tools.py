from langchain_community.tools.tavily_search import TavilySearchResults
import requests

def get_linkedin_url_for_name(name: str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/32f3c85b9513994c572613f2c8b376b633bfc43f/eden-marco-scrapin.json"
    response = requests.get(
        linkedin_profile_url,
        timeout=10,
    )

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data