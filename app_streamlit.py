import streamlit as st
import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="MCP AI Assistant", page_icon="🤖", layout="centered")

st.title("🤖 MCP AI Assistant")
st.caption("AI Agent with Tavily MCP Search")


question = st.text_area("Ask Anything",placeholder="Enter your question...")


async def run_agent(user_question):

    # MCP Client
    client = MCPClient("mcp_config_file.json")

    # LLM
    llm = ChatGroq(model="openai/gpt-oss-120b")

    # AI Agent
    agent = MCPAgent(llm=llm,client=client,max_steps=15,system_prompt=(
            "You are an AI assistant with access to web search and browser automation tools. "
            "Use Tavily search for latest information, news, and factual queries. "
            
            "Use Playwright tools when interaction with websites is required, such as "
            "opening websites, clicking buttons, extracting webpage content, filling forms, "
            "or navigating dynamic pages. "
            
            "Always provide concise and clear answers. "
            "Summarize search results in under 300 words."
        )
    )

    # Run Agent
    response = await agent.run(user_question)

    return response


if st.button("Get Answer"):

    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            try:
                response = asyncio.run(run_agent(question))
                st.success("Answer Generated")
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")