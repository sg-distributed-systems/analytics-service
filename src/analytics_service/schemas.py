"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime
from typing import Dict
from uuid import UUID

from pydantic import BaseModel, Field


class IngestEventRequest(BaseModel):
    event_id: UUID
    event_type: str
    user_id: str
    timestamp: datetime
    properties: Dict = Field(default_factory=dict)


class IngestEventResponse(BaseModel):
    ingested: bool
    event_id: UUID
    received_at: datetime
