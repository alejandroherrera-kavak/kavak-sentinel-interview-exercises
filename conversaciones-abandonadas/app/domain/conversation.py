from dataclasses import dataclass, field
from typing import List

from app.domain.message import Message


@dataclass(frozen=True)
class Conversation:
    customer_id: str
    messages: List[Message] = field(default_factory=list)
