import asyncio
import os
import sys
import warnings

from pathlib import Path
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.server.fastmcp import FastMCP
from mcp.client.stdio import stdio_client

from langchain_litellm import ChatLiteLLM
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

load_dotenv()

llm=ChatLiteLLM(model=os.environ["MODEL"])
stdio_server_params = StdioServerParameters(
   command=sys.executable,
   args=[str(Path(__file__).resolve().parent / "servers" / "math_server.py")],
)


async def main():
    async with stdio_client(stdio_server_params) as (read, write):
      async with ClientSession(read, write) as session:
        # Initialize the connection
          await session.initialize()

        # Get tools
          tools = await load_mcp_tools(session)

        # Create and run the agent
          agent = create_agent(
              llm,
              tools,
              system_prompt=(
                  "Answer in plain text. Do not use LaTeX or Markdown math formatting. "
                  "Use * for multiplication, for example: (3 + 5) * 12 = 96."
              ),
          )
          agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
          print(agent_response["messages"][-1].content)



if __name__ == "__main__":
  warnings.filterwarnings(
    "ignore",
    message=r"(?s)Pydantic serializer warnings:.*Expected `BaseMessage`",
    category=UserWarning,
    module=r"pydantic\.main",
)
  asyncio.run(main())
