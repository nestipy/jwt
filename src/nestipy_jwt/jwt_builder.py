from dataclasses import dataclass, field
from datetime import datetime
from typing import Union

from nestipy.dynamic_module import ConfigurableModuleBuilder


@dataclass
class JwtOption:
    secret: Union[str, bytes]
    exp: Union[
        datetime,
        int,
    ] = field(default_factory=lambda: datetime.now())
    is_global: bool = False
    algorithms: list[str] = field(default_factory=lambda: ["HS256"])


ConfigurableModuleClass, JWT_OPTION_TOKEN = ConfigurableModuleBuilder[
    JwtOption
]().build()
