# analytics-service

Ingests events and provides analytics capabilities.

## Why this repo exists

Analytics workloads have different performance characteristics than transactional systems, requiring dedicated infrastructure optimized for high-volume event ingestion.

## Core Components

### `ingest_event(event_type: str)`
Ingests an analytics event for processing and storage.

**Logs:**
- `event_ingested` — Logged when an event is successfully received and queued for processing

### `load_config(service_name: str) -> ServiceConfig`
Loads service configuration from environment variables including `APP_ENV` and `SHUTDOWN_TIMEOUT_SECONDS`.

### `AppError`
Base exception class for application errors. Provides `to_log_fields()` for structured error logging.

### `install_signal_handlers(service_logger_name: str)`
Installs SIGINT/SIGTERM handlers for graceful shutdown with logging.

### `init_correlation_id() -> str`
Initializes a correlation ID from the `CORRELATION_ID` environment variable or generates a UUID4.

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/analytics/ingest` | POST | Ingests an analytics event |

### Running the service

```bash
uvicorn src.analytics_service.app:app --host 0.0.0.0 --port 8008
```
