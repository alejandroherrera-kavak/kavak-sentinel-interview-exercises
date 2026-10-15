from typing import Dict, Iterable, List, Optional, Tuple

from app.application.message_gateway import MessageGateway
from app.domain.customer import Customer
from app.domain.customer_repository import CustomerRepository


class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self, customers: Optional[Iterable[Customer]] = None):
        self._customers: Dict[str, Customer] = {c.id: c for c in (customers or [])}

    def find_by_id(self, customer_id: str) -> Optional[Customer]:
        return self._customers.get(customer_id)

    def save(self, customer: Customer) -> None:
        self._customers[customer.id] = customer


class FakeMessageGateway(MessageGateway):
    """Guarda los mensajes enviados en lugar de mandarlos."""

    def __init__(self):
        self.sent: List[Tuple[str, str, str]] = []

    def send(self, phone: str, channel: str, text: str) -> None:
        self.sent.append((phone, channel, text))
