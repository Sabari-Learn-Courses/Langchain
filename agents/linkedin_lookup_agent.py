from langchain_core.tools import Tool
# create_react_agent is agent
# AgentExecutor is the runtime of our agent
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate

from tools.tools import get_linkedin_url_for_name


def lookup(name: str) -> str:
    llm = AzureChatOpenAI(temperature=0, azure_deployment='gpt-4o-mini', api_version='2025-01-01-preview')
    template = """
    Given the full name {name_of_person} I want you to get me a link to their linkedin profile.
    Output should be only URL
"""
    prompt_template = PromptTemplate(template=template, input_variables=['name_of_person'])
    
    # Preparing Tools for agent to invoke if necessary
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin page",
            func=get_linkedin_url_for_name,
            description="useful when you need to get the linkedin Page URL"
        )
    ]

    # Pulling in popular ReAct Agent Prompt created by Langchain Founder
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    url = result["output"]
    return url

