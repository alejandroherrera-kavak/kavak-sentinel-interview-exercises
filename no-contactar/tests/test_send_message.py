import pytest

from app.application.send_message import CustomerNotFound, SendMessage, SendMessageResult
from app.domain.customer import Customer
from app.infrastructure.in_memory import FakeMessageGateway, InMemoryCustomerRepository


def test_sends_message_to_existing_customer():
    # Arrange
    customer = Customer(id="c1", phone="+5215512345678", channel="whatsapp")
    gateway = FakeMessageGateway()
    use_case = SendMessage(InMemoryCustomerRepository([customer]), gateway)

    # Act
    result = use_case.execute(customer_id="c1", text="hola")

    # Assert
    assert result == SendMessageResult(customer_id="c1", status="sent")
    assert gateway.sent == [("+5215512345678", "whatsapp", "hola")]


def test_fails_when_customer_does_not_exist():
    # Arrange
    gateway = FakeMessageGateway()
    use_case = SendMessage(InMemoryCustomerRepository(), gateway)

    # Act / Assert
    with pytest.raises(CustomerNotFound):
        use_case.execute(customer_id="missing", text="hola")
    assert gateway.sent == []
