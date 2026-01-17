from pydantic import BaseModel


class IngestEventRequest(BaseModel):
    event_type: str


class IngestEventResponse(BaseModel):
    status: str
