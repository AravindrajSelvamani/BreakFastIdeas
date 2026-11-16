from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = """
Suggest exactly 5 healthy breakfast ideas.
I want south Indian breakfast ideas.
Return only the list of ideas.
Each idea should be 1-2 sentences long.
"""

reply = llm.invoke(prompt)

print(reply.content)