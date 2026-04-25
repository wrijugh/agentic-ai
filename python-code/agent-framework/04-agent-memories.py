import asyncio
import sys
from typing import Any

from agent_framework import AgentSession, ContextProvider, SessionContext

import util


class UserMemoryProvider(ContextProvider):
    """A context provider that remembers user info in session state."""

    DEFAULT_SOURCE_ID = "user_memory"

    def __init__(self):
        super().__init__(self.DEFAULT_SOURCE_ID)

    async def before_run(
        self,
        *,
        agent: Any,
        session: AgentSession | None,
        context: SessionContext,
        state: dict[str, Any],
    ) -> None:
        """Inject personalization instructions based on stored user info."""
        user_name = state.get("user_name")
        if user_name:
            context.extend_instructions(
                self.source_id,
                f"The user's name is {user_name}. Always address them by name.",
            )
        else:
            context.extend_instructions(
                self.source_id,
                "You don't know the user's name yet. Ask for it politely.",
            )

    async def after_run(
        self,
        *,
        agent: Any,
        session: AgentSession | None,
        context: SessionContext,
        state: dict[str, Any],
    ) -> None:
        """Extract and store user info in session state after each call."""
        for msg in context.input_messages:
            text = msg.text if hasattr(msg, "text") else ""
            if isinstance(text, str) and "my name is" in text.lower():
                state["user_name"] = text.lower().split("my name is")[-1].strip().split()[0].capitalize()

#-----------------------------------

CLIENT = util.client
client = CLIENT

agent = client.as_agent(
    name="MemoryAgent",
    instructions="You are a friendly assistant.",
    context_providers=[UserMemoryProvider()],
)

async def main() -> None:
    session = agent.create_session()

    # The provider doesn't know the user yet — it will ask for a name
    result = await agent.run("Hello! What's the square root of 9?", session=session)
    print(f"Agent: {result}\n")

    # Now provide the name — the provider stores it in session state
    result = await agent.run("My name is Alice", session=session)
    print(f"Agent: {result}\n")

    # Subsequent calls are personalized — name persists via session state
    result = await agent.run("What is 2 + 2?", session=session)
    print(f"Agent: {result}\n")

    # Inspect session state to see what the provider stored
    provider_state = session.state.get("user_memory", {})
    print(f"[Session State] Stored user name: {provider_state.get('user_name')}")

if __name__ == "__main__":
    if "--devui" in sys.argv: 
        from agent_framework.devui import serve

        serve(entities=[agent], port=8080, auto_open=True)
    else:
        asyncio.run(main())