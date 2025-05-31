from dotenv import load_dotenv
load_dotenv()

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.profile_summarizer_agent import summarize as summarize_linkedin_profile
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from output_parsers import summary_parser

from third_parties.linkedin import scrape_linkedin_profile


def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name)
    print("Fetched URL:", linkedin_url)
    
    linkedin_profile = scrape_linkedin_profile(linkedin_url)

    llm = AzureChatOpenAI(temperature=0, azure_deployment='gpt-4o-mini', api_version='2025-01-01-preview')
    user_prompt_template = """
    Given the Linkedin Profile information,
    {linkedin_profile}
    Extract the details and give me
    1. A short summary
    2. two interesting facts about them
    \n{format_instructions}
    """

    prompt_template = PromptTemplate(
        template=user_prompt_template,
        input_variables=["linkedin_profile"],
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    chain = prompt_template | llm | summary_parser

    print("invoking chain")
    resp = chain.invoke(
        input={"linkedin_profile": linkedin_profile}
    )

    print(resp)
    

ice_break_with("Eden Marco")
    
