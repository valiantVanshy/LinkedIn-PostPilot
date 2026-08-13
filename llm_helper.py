from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

if __name__ == "__main__":
    response = llm.invoke(
        "How is the job market for engineers in India in 2026?"
    )
    print(response.content)