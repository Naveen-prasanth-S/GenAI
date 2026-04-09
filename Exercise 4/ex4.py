import os
from typing import Annotated, TypedDict
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition



load_dotenv()


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]



@tool
def get_weather(location: str) -> str:
    """Return current weather for a location."""
    return f"The weather in {location} is currently 72°F and sunny."


@tool
def calculate_sum(a: int, b: int) -> str:
    """Return the sum of two numbers."""
    return str(a + b)

tools = [get_weather, calculate_sum]
tool_node = ToolNode(tools)


llm = ChatGroq(
    model_name=os.getenv("GROQ_MODEL_NAME", "llama-3.1-8b-instant"),
    temperature=0.0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
)

# 🔥 IMPORTANT FIX
llm_with_tools = llm.bind_tools(tools, tool_choice="auto")

SYSTEM_MSG = SystemMessage(
    content="""
You are a helpful AI assistant.

STRICT RULES:
- ALWAYS use tools when needed
- NEVER generate <function=...> format
- ALWAYS return proper JSON tool arguments
- After tool returns result, use it to answer clearly

Examples:
User: weather in Tiruppur
→ call get_weather with {"location": "Tiruppur"}

User: 4 5
→ call calculate_sum with {"a": 4, "b": 5}
"""
)


def chatbot(state: State):
    messages = [SYSTEM_MSG] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


def run_langgraph_tools_demo():
    print("Building LangGraph Pipeline with Tools...")

    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("tools", tool_node)

    graph_builder.add_edge(START, "chatbot")

    graph_builder.add_conditional_edges(
        "chatbot",
        tools_condition,
    )

    graph_builder.add_edge("tools", "chatbot")

    app = graph_builder.compile()

    print("Pipeline built successfully!\n")
    print("Welcome to the LangGraph Groq Chatbot with Tools!")
    print("Try asking for weather or math operations.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            # 🔥 USE INVOKE (NO MULTIPLE OUTPUT)
            result = app.invoke(
                {"messages": [HumanMessage(content=user_input)]}
            )

            messages = result["messages"]

            tool_called = None
            tool_result = None
            final_answer = None

            for msg in messages:
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    tool_called = msg.tool_calls[0]

                elif isinstance(msg, ToolMessage):
                    tool_result = msg.content

                elif msg.type == "ai" and msg.content:
                    final_answer = msg.content

        
            if tool_called:
                print(f"-> [Agent is calling tool '{tool_called['name']}' with args {tool_called['args']}]")

            if tool_result:
                print(f"<- [Tool returned: {tool_result}]")

            if final_answer:
                print(f"Groq Bot: {final_answer}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_langgraph_tools_demo()