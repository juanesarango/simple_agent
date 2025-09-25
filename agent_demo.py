import asyncio
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient


async def run_example():
    """Run an example using multiple MCP servers."""
    
    # Create a configuration with multiple servers
    config = {
        "mcpServers": {
            "airbnb": {
                "command": "npx",
                "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
            },
            "playwright": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"],
                "env": {"DISPLAY": ":1"},
            },
            "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "./",
                ],
            }
        }
    }
    client = MCPClient.from_dict(config)
    

    # Create LLM
    llm = ChatOpenAI(model="gpt-5-mini")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    query = (
        "Choose a nice place on Airbnb, under $600 usd/night, to stay in NYC "
        "on the upper east side close to Rockefeller University and Central Park, "
        "then use Google to find nearby restaurants and attractions. "
        "Write the results in current directory in retreat_plan.md in a nice markdown format, "
        "with image links and with a summary at the end."
    )
    print(f"Query: {query}")
    result = await agent.run(query)
    print(result)

if __name__ == "__main__":
    asyncio.run(run_example())