from abc import ABC, abstractmethod
from typing import List

from app.domain.conversation import Conversation


class ConversationRepository(ABC):
    @abstractmethod
    def find_active(self) -> List[Conversation]:
        """Conversaciones con actividad reciente. El orden de los mensajes NO esta garantizado."""
