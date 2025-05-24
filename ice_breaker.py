from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import clean_linkedin_data, scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
        Given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    # Temperature sets the creativity of model. 0 -> not creative, 1 -> more creative. it accepts decimal value as well,
    # but within range 0 - 1.
    llm = AzureChatOpenAI(temperature=0, azure_deployment='gpt-4o-mini', api_version='2025-01-01-preview')
    # llm = ChatOllama(model='deepseek-r1:1.5b')

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile("safcf")
    cleaned_linkedin_data = clean_linkedin_data(linkedin_data)
    res = chain.invoke(input={"information": cleaned_linkedin_data})

    print(res)
