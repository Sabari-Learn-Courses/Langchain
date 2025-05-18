from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. A short Summary
        2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    # Temperature sets the creativity of model. 0 -> not creative, 1 -> more creative. it accepts decimal value as well,
    # but within range 0 - 1.
    # llm = AzureChatOpenAI(temperature=0, azure_deployment='gpt-4o-mini', api_version='2025-01-01-preview')
    llm = ChatOllama(model='deepseek-r1:1.5b')

    # chaining all the components together using pipe symbol, which comes from Langchain Expression Language.
    chain = summary_prompt_template | llm | StrOutputParser()

    # Run chain
    res = chain.invoke(
        input={
            "information": "Ravi is a software engineer with 2 years of exp in AI & ML"
        }
    )

    print(res)
