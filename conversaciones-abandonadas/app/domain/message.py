from dataclasses import dataclass
from datetime import datetime
from typing import Literal

Direction = Literal["inbound", "outbound"]  # inbound = cliente, outbound = agente o bot


@dataclass(frozen=True)
class Message:
    direction: Direction
    timestamp: datetime  # siempre con zona horaria (UTC)
    body: str = ""
