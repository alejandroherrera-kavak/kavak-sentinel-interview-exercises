from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.application.send_message import CustomerNotFound, SendMessage
from app.domain.customer import Customer
from app.infrastructure.in_memory import FakeMessageGateway, InMemoryCustomerRepository

app = FastAPI()
customers = InMemoryCustomerRepository(
    [
        Customer(id="c1", phone="+5215512345678", channel="whatsapp"),
        Customer(id="c2", phone="+5491112345678", channel="sms"),
    ]
)
gateway = FakeMessageGateway()


class SendMessageRequest(BaseModel):
    customer_id: str
    text: str


@app.post("/messages", status_code=201)
def send_message(request: SendMessageRequest):
    use_case = SendMessage(customers, gateway)
    try:
        return use_case.execute(request.customer_id, request.text)
    except CustomerNotFound:
        raise HTTPException(status_code=404, detail="customer not found")
