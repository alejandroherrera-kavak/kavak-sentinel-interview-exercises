from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    id: str
    phone: str
    channel: str  # "whatsapp" | "sms"
