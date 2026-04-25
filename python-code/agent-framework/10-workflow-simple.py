import sys
import asyncio

from agent_framework import (
    Executor,
    WorkflowContext,
    handler, 
    WorkflowBuilder
)

class UpperCaseExecutor(Executor):
    @handler
    async def to_upper_case(self, text: str, ctx: WorkflowContext[str]) -> None:
        """Convert the input inro upper case and forward to the next node."""
        await ctx.send_message(text.upper())


class AddBracketExecutor(Executor):
    @handler
    async def add_bracket(self, text: str, ctx: WorkflowContext[str]) -> None:
        """Wrap it around {}"""
        await ctx.send_message("{ " + text + " }")

upper = UpperCaseExecutor(id="upper")
bracket = AddBracketExecutor(id="bracket")

workflow = WorkflowBuilder(start_executor=upper).add_edge(upper, bracket).build()

if __name__ == "__main__":
    from agent_framework.devui import serve
    serve(entities=[workflow], port=8080, auto_open=True) 