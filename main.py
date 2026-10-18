import asyncio
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.server.fastmcp import FastMCP
from mcp.client.stdio import stdio_client

from langchain_litellm import ChatLiteLLM
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

load_dotenv()

llm=ChatLiteLLM()
stdio_server_params = StdioServerParameters(
   command="python",
   args=["C:\\MyGit\\UdemyLangchainCourse\\mcp-crash-course\\servers\\math_server.py"],
)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
  asyncio.run(main())
