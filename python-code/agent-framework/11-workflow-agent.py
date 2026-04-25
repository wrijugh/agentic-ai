import asyncio
from dataclasses import dataclass
import sys
from typing import Never
import agent_framework as af
from agent_framework import (
    
    Executor,
    WorkflowContext,
    handler,
    WorkflowBuilder,
    AgentExecutorResponse,
)

class Dispatcher(Executor):
    """Send the same text to the downstream so fan-out edges can broadcast it."""
    @handler
    async def dispatch(self, prompt: str, ctx: WorkflowContext[str]) -> None:
        """Send the message to all downstream expert branches"""
        await ctx.send_message(prompt)

@dataclass
class AggregatedInsights:
    """Consolidated output"""

    authorbio: str
    majorworks: str

class AggregateInsights(Executor):
    """Join the outputs"""

    @handler
    async def aggregate(
        self,
        results: list[AgentExecutorResponse],
        ctx: WorkflowContext[Never, str],
    ) -> None:
        """"""
        expert_outputs: dict[str, str] = {"authorbio": "", "majorworks":""}
        for result in results:
            executor_id = result.executor_id.lower()
            text = result.agent_response.text
            if "authorbio" in executor_id:
                expert_outputs["authorbio"] = text
            elif "majorworks" in executor_id:
                expert_outputs["majorworks"] = text

        aggregated = AggregatedInsights(
            authorbio = expert_outputs["authorbio"],
            majorworks = expert_outputs["majorworks"]
        )    

        consolidated = (
            "==== All ==== \n\n"
            f"Author's Biography:\n{aggregated.authorbio}\n\n"
            f"--------------------\n\n"
            f"Major Works:\n{aggregated.majorworks}\n\n"
        )
        await ctx.yield_output(consolidated)

dispatcher = Dispatcher(id="dispatcher")

# Agents
import util
CLIENT = util.client

agent_authorbio = af.Agent(
    client=CLIENT,
    name="authorbio",
    instructions="You are an helpful literary companion. You create a three line bipgraphy of the author."
)

agent_majorworks = af.Agent(
    client=CLIENT,
    name="majorworks",
    instructions="You are an helpful literary companion. You tell three major works by the author."
)

#Aggregator

aggregator = AggregateInsights(id="aggregator")

workflow =( 
    WorkflowBuilder
    (
        name="FanOutInEdges",
        description="Explicit fan-out/fan-in using edge groups.",
        start_executor=dispatcher,
        output_executors=[aggregator]
    )
    .add_fan_out_edges(dispatcher, [agent_authorbio, agent_majorworks])
    .add_fan_in_edges([agent_authorbio, agent_majorworks], aggregator)
    .build()
)

async def main():
    input_text = "I need to make Pasta."
    events = await workflow.run(input_text)
    outputs = events.get_outputs()
    for result in outputs:
        print(result)

if __name__ == "__main__":
    if "--devui" in sys.argv: 
        from agent_framework.devui import serve

        serve(entities=[workflow], port=8070, auto_open=True)
    else:
        asyncio.run(main())