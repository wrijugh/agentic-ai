import util

client = util.client

import asyncio
import agent_framework


agent = agent_framework.Agent(
    name="Simple Agent",
    client=client,
    instructions="You are a helpful assistant and answer cheerfully.",
)

mysession = agent.create_session()


async def main():
    response = await agent.run("My name is Wriju and I am a professional developer.", session=mysession)
    print(f"Response: {response}\n")

    print("-------------------------------\n")

    response = await agent.run("I occasionally teach Python to school children.", session=mysession)
    print(f"Response: {response}\n")
    print("-------------------------------\n")

    response = await agent.run("What do you know about me?", session=mysession)
    print(f"Response: {response}\n")
    


if __name__ == "__main__":
    asyncio.run(main()) 