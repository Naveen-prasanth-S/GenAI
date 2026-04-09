import os
from typing import Annotated, TypedDict
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from dotenv import load_dotenv
import os

load_dotenv()
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

llm = ChatGroq(
    model_name=os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-versatile"),
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY"),
)

def chatbot(state: State):
   
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def run_langgraph_demo():
    print("Building simple LangGraph Pipeline with ChatGroq...")
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    app = graph_builder.compile()

    print("Pipeline built successfully!\n")
    print("Welcome to the LangGraph Groq Chatbot!")
    print("Type 'quit' or 'exit' to exit.\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break
            if not user_input.strip():
                continue

            events = app.stream(
                {"messages": [HumanMessage(content=user_input)]},
                stream_mode="values"
            )
            
            for event in events:
              
                latest_message = event["messages"][-1]
                

                if latest_message.type == "ai":
                    print(f"Groq Bot: {latest_message.content}")
                    
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_langgraph_demo()