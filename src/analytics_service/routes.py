"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import ingest_event
from .schemas import IngestEventRequest, IngestEventResponse

router = APIRouter()


@router.post("/analytics/ingest", response_model=IngestEventResponse)
def ingest_event_route(req: IngestEventRequest) -> IngestEventResponse:
    ingest_event(req.event_type)
    return IngestEventResponse(status="ok")
