from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from schema import ExtractedData


def LLMagent(user_input: str):
    try:
        llm = ChatGoogleGenerativeAI(
            model="models/gemini-2.5-flash",
            temperature=0.0
        )

        prompt_message = [
            HumanMessage(
                # Instruct the model clearly on what to do.
                content=f"Extract the requested data from the following text and conform to the provided schema:\n\nTEXT: {user_input}"
            )
        ]

        pydantic_output = llm.with_structured_output(ExtractedData).invoke(prompt_message)
        
        return pydantic_output.model_dump_json(indent=2)
        
    except Exception as e:
        return f"\n LangChain Agent Failed! Error: {e}"

