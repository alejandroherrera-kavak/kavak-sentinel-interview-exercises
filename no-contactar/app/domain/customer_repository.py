from abc import ABC, abstractmethod
from typing import Optional

from app.domain.customer import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def find_by_id(self, customer_id: str) -> Optional[Customer]:
        """Devuelve el cliente o None si no existe."""

    @abstractmethod
    def save(self, customer: Customer) -> None:
        """Crea o reemplaza el cliente."""
