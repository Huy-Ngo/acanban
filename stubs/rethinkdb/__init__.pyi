from typing import Any, Optional, Type

from .trio_net.net_trio import TrioConnectionPool

# FIXME: remove all Any
class RethinkDB:
    ConnectionPool: Type[TrioConnectionPool]
    row: Any
    def __init__(self) -> None: ...
    def now(self) -> Any: ...
    def set_loop_type(self, library: Optional[str]) -> None: ...
    def table(self, name: str) -> Any: ...

r: RethinkDB
