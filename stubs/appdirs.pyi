from typing import Optional

def user_config_dir(appname: Optional[str] = None,
                    appauthor: Optional[str] = None,
                    version: Optional[str] = None,
                    roaming: Optional[bool] = False) -> str: ...
def site_config_dir(appname: Optional[str] = None,
                    appauthor: Optional[str] = None,
                    version: Optional[str] = None,
                    multipath: Optional[bool] = False) -> str: ...
