"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import IngestEventRequest, IngestEventResponse
from .service import ingest_event

router = APIRouter()


@router.post("/analytics/ingest", response_model=IngestEventResponse, status_code=200)
def ingest_event_route(req: IngestEventRequest) -> IngestEventResponse:
    result = ingest_event(
        event_id=req.event_id,
        event_type=req.event_type,
        user_id=req.user_id,
        timestamp=req.timestamp,
        properties=req.properties,
    )
    return IngestEventResponse(
        ingested=result["ingested"],
        event_id=result["event_id"],
        received_at=result["received_at"],
    )
