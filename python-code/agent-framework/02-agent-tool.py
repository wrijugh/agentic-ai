import util
client = util.client

import asyncio
from agent_framework import Agent, tool 

@tool
def get_date() -> str:
    """Get the current date."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")



agent = Agent(
    name="Agent-tool",
    client=client,
    instructions="You are a helpful assistant and answer cheerfully.",
    tools=[get_date],
)

async def main():
    response = await agent.run("What is the day today?")
    print(response)

if __name__ == "__main__":
    from agent_framework.devui import serve

    serve(entities=[agent], auto_open=True)

    # asyncio.run(main()) 