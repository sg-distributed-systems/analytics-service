from core_logger import get_logger

logger = get_logger("analytics-service")


def ingest_event(event_type: str) -> None:
    logger.info("event_ingested", event_type=event_type)


if __name__ == "__main__":
    ingest_event("page_view")
