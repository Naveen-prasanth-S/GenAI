GENAI Essentials – Hands-on Exercises
This repository contains a structured set of beginner-to-intermediate exercises designed to understand how Generative AI applications are built using modern tools and frameworks.

Technologies Used
Groq API (OpenAI-compatible)

LangChain

LangGraph

Langfuse (Tracing & Monitoring)

Python

Exercises Overview
🔹 Exercise 1: Basic LLM Integration
Connects to Groq API using OpenAI-compatible client

Sends a prompt and retrieves response

Concepts Covered:

API integration

Environment variables (.env)

Model invocation

🔹 Exercise 2: LangChain Agent with Custom Tool
Builds an AI agent using LangChain

Implements a custom tool (get_word_length)

Agent decides when to call the tool

Concepts Covered:

Agents

Tools

Decision-making with LLMs

🔹 Exercise 3: LangGraph Chatbot (State-Based)
Creates a chatbot using LangGraph

Implements state-driven message handling

Concepts Covered:

Graph-based workflows

State management

Streaming responses

🔹 Exercise 4: LangGraph with Tool Integration
Integrates tools into LangGraph workflow

Enables dynamic tool execution

Features:

Tool execution (e.g., sum, weather)

Conditional routing

Dynamic responses

Concepts Covered:

ToolNode

Conditional edges

Multi-step execution

🔹 Exercise 5: Langfuse Integration (Tracing & Monitoring)
Adds observability to AI workflows

Tracks model inputs, outputs, and performance

Concepts Covered:

Observability in AI systems

Debugging LLM workflows

Monitoring with Langfuse

Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/genai-project.git
cd genai-project
2. Install Dependencies
python -m pip install openai langchain langchain-groq langgraph python-dotenv langfuse
3. Configure Environment Variables
Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here
GROQ_MODEL_NAME=llama3-8b-8192

LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
4. Run the Exercises
Run any exercise file:

python exp1/ex1.py
python exp2/ex2.py
python exp3/ex3.py
python exp4/ex4.py
python exp5/ex5.py
Important Notes
Do not upload the .env file to GitHub

Use .gitignore to protect API keys

Prefer Python 3.10 or 3.11 for better compatibility

Restart the terminal after updating .env

Project Structure
GenAI_Essentials/
│
├── exp1/   # Basic LLM call
├── exp2/   # LangChain agent
├── exp3/   # LangGraph chatbot
├── exp4/   # LangGraph + tools
├── exp5/   # Langfuse integration
├── .gitignore
├── .env.example
└── README.md
Learning Outcome
By completing these exercises, you will understand:

How to interact with LLM APIs

How to build intelligent agents

How to design graph-based AI workflows

How to integrate tools into AI systems

How to monitor and debug AI applications

Conclusion
This repository provides a complete learning path:

LLM Basics → Agents → Graph Workflows → Tool Integration → Observability

It forms a strong foundation for building real-world GenAI applications 🚀

Future Enhancements
Add memory-enabled chatbot

Integrate vector database (FAISS / Pinecone)

Build a RAG-based system

Deploy as a web or mobile app

