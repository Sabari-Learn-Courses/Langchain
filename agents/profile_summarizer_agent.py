from langchain_openai import AzureChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate

from tools.tools import scrape_linkedin_profile

def summarize(profile_url: str) -> str:

    llm = AzureChatOpenAI(temperature=0, azure_deployment='gpt-4o-mini', api_version='2025-01-01-preview')

    agent_prompt = hub.pull('hwchase17/react')
    user_prompt_template = """
    Given the Linkedin Profile url {linkedin_url},
    Extract the details and give me
    1. A short summary
    2. two interesting facts about them
"""
    user_prompt = PromptTemplate(template=user_prompt_template, input_variables=['linkedin_url'])

    tools = [
        Tool(
            name="Get Linkedin Profile",
            func=scrape_linkedin_profile,
            description="Given URL of linkedin Profile, it scraps the data from linkedin URL & returns it"
        )
    ]
    agent = create_react_agent(llm=llm, tools=tools, prompt=agent_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    resp = agent_executor.invoke(input={
        "input": user_prompt.format_prompt(linkedin_url=profile_url)
    })

    return resp["output"]
