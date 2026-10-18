import asyncio

from dotenv import load_dotenv
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_litellm import ChatLiteLLM
load_dotenv()

MODEL=os.environ['MODEL']
llm=ChatLiteLLM(temperature=1, model=MODEL)

async def main():
    print("hello langchain mcp")

if __name__=="__main__":
    asyncio.run(main())