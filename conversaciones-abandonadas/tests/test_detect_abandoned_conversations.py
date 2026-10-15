from datetime import datetime, timedelta, timezone

from app.application.detect_abandoned_conversations import DetectAbandonedConversations
from app.domain.conversation import Conversation
from app.domain.message import Message
from app.infrastructure.in_memory_conversation_repository import InMemoryConversationRepository

NOW = datetime(2026, 10, 15, 12, 0, tzinfo=timezone.utc)


def hours_ago(hours: float) -> datetime:
    return NOW - timedelta(hours=hours)


def test_conversation_answered_by_agent_is_not_abandoned():
    # Arrange
    conversation = Conversation(
        customer_id="c1",
        messages=[
            Message("inbound", hours_ago(30), "hola, tengo un problema con mi pago"),
            Message("outbound", hours_ago(29), "hola, te ayudo con eso"),
        ],
    )
    use_case = DetectAbandonedConversations(InMemoryConversationRepository([conversation]))

    # Act
    result = use_case.execute(now=NOW)

    # Assert
    assert result == []
