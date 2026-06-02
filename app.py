import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
from utlis.guardrail import input_guardrail, output_guardrail


async def main():

    # Load environment variables from .env file
    load_dotenv()

    # Get GROQ API key
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    # Load MCP configuration
    client = MCPClient("mcp_config_file.json")

    # Create LLM model
    llm = ChatGroq(model="openai/gpt-oss-120b")

    # Create AI agent
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        system_prompt=(
            "You are an AI assistant with access to web search and browser automation tools. "
            "Use Tavily search for latest information, news, and factual queries. "
            
            "Use Playwright tools when interaction with websites is required, such as "
            "opening websites, clicking buttons, extracting webpage content, filling forms, "
            "or navigating dynamic pages. "
            
            "Always provide concise and clear answers. "
            "Summarize search results in under 300 words."
        )
    )

    while True:

        # Take user input
        question = input("You: ")

        # Exit condition
        if question.lower() == "exit":
            break
        
        # Input guardrail
        is_valid, error_message = input_guardrail(question)
        if not is_valid:
            print("\nGuardrail:", error_message)
            continue

        # Run AI agent
        response = await agent.run(question)

        # Output guardrail
        response = output_guardrail(response)
        # Print response
        print("\nAssistant:", response)


# Start program
asyncio.run(main())