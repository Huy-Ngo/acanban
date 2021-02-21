from typing import Any, Dict, Union

from .trio_net.net_trio import Connection

class RqlQuery:
    def __getitem__(self, index: Any) -> RqlQuery: ...

    def count(self) -> RqlQuery: ...
    def filter(self, predicate: dict) -> RqlQuery: ...
    def pluck(self, *selectors: Union[str, Dict[str, Any]]) -> RqlQuery: ...
    def order_by(self, key: str) -> RqlQuery: ...
    def update(self, obj: dict) -> RqlQuery: ...

    # Loaded JSON or TrioCursor of loaded JSON,
    # static typing has no power here.
    async def run(self, c: Connection) -> Any: ...

class Table(RqlQuery):
    def get(self, key: str) -> RqlQuery: ...
    def get_all(self, *keys: str, index: str = 'id') -> RqlQuery: ...
    def insert(self, *objects: dict) -> RqlQuery: ...
