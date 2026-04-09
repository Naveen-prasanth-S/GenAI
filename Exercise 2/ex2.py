import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.tools import tool
load_dotenv()
print("MODEL:", os.getenv("GROQ_MODEL_NAME"))
print("API KEY:", os.getenv("GROQ_API_KEY"))
model = ChatGroq(
    model_name=os.getenv("GROQ_MODEL_NAME"),
    temperature=0.1,
    groq_api_key=os.getenv("GROQ_API_KEY"),
)
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]
agent = create_agent(
    model,
    tools=tools,
    system_prompt="You are a helpful assistant."
)
inputs = {
    "messages": [
        {"role": "user", "content": "How many letters are in the word 'langchain'?"}
    ]
}
response = agent.invoke(inputs)
final_message = response["messages"][-1]
print("\nFinal Answer:", final_message.content)