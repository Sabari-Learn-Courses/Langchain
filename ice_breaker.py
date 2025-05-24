from dotenv import load_dotenv
load_dotenv()

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.profile_summarizer_agent import summarize as summarize_linkedin_profile
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile


def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name)
    print("Fetched URL:", linkedin_url)
    summarized_data = summarize_linkedin_profile(linkedin_url)
    print(summarized_data)
    

ice_break_with("Eden Marco")
    
