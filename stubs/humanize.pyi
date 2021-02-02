from datetime import datetime
from typing import Optional, Union

def naturalsize(value: Union[float, str], binary: bool = False,
                gnu: bool = False, format: str = '%.1f') -> str: ...
def naturaltime(value: Union[datetime, int], future: bool = False,
                months: bool = True, minimum_unit: str = 'seconds',
                when: Optional[datetime] = None) -> str: ...
