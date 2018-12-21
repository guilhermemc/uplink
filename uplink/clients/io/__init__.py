from uplink.clients.io.interfaces import (
    Client,
    Executable,
    ExecutionStrategy,
    RequestTemplate,
)
from uplink.clients.io.context import BasicExecutionContext
from uplink.clients.io.templates import CompositeRequestTemplate
from uplink.clients.io.blocking_strategy import BlockingStrategy
from uplink.clients.io.twisted_strategy import TwistedStrategy

__all__ = [
    "Client",
    "CompositeRequestTemplate",
    "Executable",
    "ExecutionStrategy",
    "RequestTemplate",
    "BlockingStrategy",
    "AsyncioStrategy",
    "TwistedStrategy",
    "execute",
]

try:
    from uplink.clients.io.asyncio_strategy import AsyncioStrategy
except (ImportError, SyntaxError):  # pragma: no cover

    class AsyncioStrategy(ExecutionStrategy):
        def __init__(self, *args, **kwargs):
            raise NotImplementedError(
                "Failed to load `asyncio` execution strategy: you may be using a version "
                "of Python below 3.3. `aiohttp` requires Python 3.4+."
            )


def execute(client, execution, template, request):
    context_ = BasicExecutionContext(client, execution, template, request)
    return execution.execute(context_)
