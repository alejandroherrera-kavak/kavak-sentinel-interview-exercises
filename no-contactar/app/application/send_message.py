from dataclasses import dataclass

from app.application.message_gateway import MessageGateway
from app.domain.customer_repository import CustomerRepository


class CustomerNotFound(Exception):
    pass


@dataclass(frozen=True)
class SendMessageResult:
    customer_id: str
    status: str  # "sent"


class SendMessage:
    def __init__(self, customers: CustomerRepository, gateway: MessageGateway):
        self._customers = customers
        self._gateway = gateway

    def execute(self, customer_id: str, text: str) -> SendMessageResult:
        customer = self._customers.find_by_id(customer_id)
        if customer is None:
            raise CustomerNotFound(customer_id)
        self._gateway.send(customer.phone, customer.channel, text)
        return SendMessageResult(customer_id=customer_id, status="sent")
