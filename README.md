# MCP AI Assistant with Tavily Search

## Overview

This project is an AI-powered assistant built using MCP (Model Context Protocol), Groq LLM, Streamlit, Tavily Search, and Playwright. The assistant can perform real-time web searches, retrieve up-to-date information, and interact with websites through browser automation.

## Features

* Real-time web search using Tavily MCP Server
* Browser automation using Playwright MCP
* AI-powered responses using Groq LLM
* Streamlit-based user interface
* Support for dynamic website interaction and content extraction
* Latest news and factual information retrieval

## Tech Stack

* Streamlit
* LangChain
* Groq LLM
* MCP (Model Context Protocol)
* Tavily Search
* Playwright
* Python

## Architecture

1. User enters a query through Streamlit UI.
2. MCP Client connects to configured MCP servers.
3. Tavily MCP provides real-time web search capabilities.
4. Playwright MCP handles browser automation tasks.
5. Groq LLM acts as the reasoning engine.
6. MCP Agent selects the appropriate tool and generates the final response.

## MCP Servers Used

    ### Tavily MCP

    Used for:

    * Latest news retrieval
    * Web search
    * Fact checking
    * Research queries

    ### Playwright MCP

    Used for:

    * Website navigation
    * Content extraction
    * Form interactions
    * Dynamic page handling


## Use Cases

* AI Research Assistant
* News Summarization
* Web Information Retrieval
* Website Data Extraction
* Browser Automation Workflows
