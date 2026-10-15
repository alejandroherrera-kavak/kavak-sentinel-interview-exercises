from typing import Iterable, List, Optional

from app.domain.conversation import Conversation
from app.domain.conversation_repository import ConversationRepository


class InMemoryConversationRepository(ConversationRepository):
    def __init__(self, conversations: Optional[Iterable[Conversation]] = None):
        self._conversations: List[Conversation] = list(conversations or [])

    def find_active(self) -> List[Conversation]:
        return list(self._conversations)
