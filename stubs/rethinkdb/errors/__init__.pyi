from typing import Any, Optional

class ReqlError(Exception):
    def __init__(self, message: str, term: Optional[Any],
                 frames: Optional[Any]) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class ReqlNonExistenceError(ReqlError): ...
