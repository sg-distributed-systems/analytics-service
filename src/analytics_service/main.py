"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from analytics_service.config import load_config
from analytics_service.errors import AppError
from analytics_service.lifecycle import install_signal_handlers
from analytics_service.observability import init_correlation_id

logger = get_logger("analytics-service")


def ingest_event(event_type: str) -> None:
    logger.info("event_ingested", event_type=event_type)


def run() -> None:
    cfg = load_config("analytics-service")
    cid = init_correlation_id()
    install_signal_handlers("analytics-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        ingest_event("page_view")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
