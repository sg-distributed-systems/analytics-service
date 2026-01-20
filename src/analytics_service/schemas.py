"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from pydantic import BaseModel


class IngestEventRequest(BaseModel):
    event_type: str


class IngestEventResponse(BaseModel):
    status: str
