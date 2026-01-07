from core_logger import get_logger

logger = get_logger("analytics-service")


def ingest_event(event_type: str) -> None:
    logger.info("event_ingested", event_type=event_type)


def main() -> None:
    ingest_event("page_view")


if __name__ == "__main__":
    main()
