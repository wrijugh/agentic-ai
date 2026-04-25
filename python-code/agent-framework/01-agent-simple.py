import util

client = util.client

import asyncio
import agent_framework


agent = agent_framework.Agent(
    name="Simple Agent",
    client=client,
    instructions="You are a helpful assistant and answer cheerfully.",
)

async def main():
    response = await agent.run("What is the day today?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main()) 