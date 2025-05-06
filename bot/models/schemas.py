from pydantic import BaseModel, Field
from datetime import datetime, timezone

class JournalEntry(BaseModel):
    entry: str  # Required journal message from the user
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


