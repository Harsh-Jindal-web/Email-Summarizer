from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

MAX_CHARS = 12000  # Adjust this number based on token limit (rough approx)

def truncate_text(text, max_chars=MAX_CHARS):
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[Text truncated due to length]"
    return text

def summarizeEmail(body):
    body = truncate_text(body)
    prompt = PromptTemplate(
        template="""Acting like a Good Reader and Writer, summarize the body of the email in 3 sentences. 

        NOTE: SUMMARIZE IN EXACTLY 3 SENTENCES AND RETURN ONLY THE SUMMARY. 
        Body: {body}

        SUMMARY:
        """,
        input_variables=["body"]
    )   
    parser = StrOutputParser()

    model = ChatGroq(
        model="gemma2-9b-it"
    )
    chain = prompt | model | parser

    result = chain.invoke({"body": body})
    return result

if __name__ =="__main__":
    ans = summarizeEmail("Hii i am Satyam Singh")
    print(ans)
