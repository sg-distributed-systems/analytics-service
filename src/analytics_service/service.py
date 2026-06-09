"""
Core analytics event processing logic.

Handles ingestion, validation, and enrichment of analytics events from various
sources. Validates event types against allowed categories, enriches events with
server-side timestamps, and prepares them for downstream processing and storage.
"""
from datetime import datetime
from uuid import UUID

from core_logger import get_logger

from .errors import ValidationError

logger = get_logger("analytics-service", tier="infrastructure")

VALID_EVENT_TYPES = {"page_view", "click", "purchase", "signup", "logout"}


def ingest_event(
    event_id: UUID, event_type: str, user_id: str, timestamp: datetime, properties: dict
) -> dict:
    logger.info(
        "event_received", event_id=str(event_id), event_type=event_type, user_id=user_id
    )

    if event_type not in VALID_EVENT_TYPES:
        logger.warning(
            "invalid_event_type", event_type=event_type, allowed=list(VALID_EVENT_TYPES)
        )
        raise ValidationError(
            "invalid_event_type", details={"allowed": list(VALID_EVENT_TYPES)}
        )

    if timestamp > datetime.utcnow():
        raise ValidationError("future_timestamp_not_allowed")

    enriched_properties = {**properties, "ingested_at": datetime.utcnow().isoformat()}
    logger.debug(
        "event_enriched", event_id=str(event_id), property_count=len(enriched_properties)
    )

    logger.info("event_ingested", event_id=str(event_id), user_id=user_id)
    return {"ingested": True, "event_id": event_id, "received_at": datetime.utcnow()}


def aggregate_events(event_type: str, window_seconds: int) -> dict:
    logger.info(
        "aggregation_requested", event_type=event_type, window_seconds=window_seconds
    )

    if event_type not in VALID_EVENT_TYPES:
        raise ValidationError(
            "invalid_event_type", details={"allowed": list(VALID_EVENT_TYPES)}
        )

    if window_seconds <= 0:
        raise ValidationError("invalid_window", details={"window_seconds": window_seconds})

    logger.debug("rollup_computed", event_type=event_type, window_seconds=window_seconds)
    return {
        "event_type": event_type,
        "count": 0,
        "window_seconds": window_seconds,
        "computed_at": datetime.utcnow(),
    }
