from typing import Any, Optional, Type

from .trio_net.net_trio import TrioConnectionPool

class RethinkDB:
    ConnectionPool: Type[TrioConnectionPool]
    def __init__(self) -> None: ...
    def set_loop_type(self, library: Optional[str]) -> None: ...
    def table(self, name: str) -> Any: ...

r: RethinkDB
