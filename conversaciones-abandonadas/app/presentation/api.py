from datetime import datetime, timezone

from fastapi import FastAPI

from app.application.detect_abandoned_conversations import DetectAbandonedConversations
from app.infrastructure.in_memory_conversation_repository import InMemoryConversationRepository

app = FastAPI()
repository = InMemoryConversationRepository()


@app.get("/conversations/abandoned")
def abandoned_conversations(hours: int = 24):
    use_case = DetectAbandonedConversations(repository, threshold_hours=hours)
    return use_case.execute(now=datetime.now(timezone.utc))
