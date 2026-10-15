from abc import ABC, abstractmethod


class MessageGateway(ABC):
    @abstractmethod
    def send(self, phone: str, channel: str, text: str) -> None:
        """Envia un mensaje al cliente por el canal indicado."""
