from dataclasses import dataclass
from datetime import datetime
from typing import List

from app.domain.conversation_repository import ConversationRepository


@dataclass(frozen=True)
class AbandonedConversation:
    customer_id: str
    waiting_since: datetime
    waiting_hours: float


class DetectAbandonedConversations:
    def __init__(self, repository: ConversationRepository, threshold_hours: int = 24):
        self._repository = repository
        self._threshold_hours = threshold_hours

    def execute(self, now: datetime) -> List[AbandonedConversation]:
        # TODO: implementar
        return []
