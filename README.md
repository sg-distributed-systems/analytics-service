# analytics-service

Ingests events and provides analytics capabilities.

## Why this repo exists

Analytics workloads have different performance characteristics than transactional systems, requiring dedicated infrastructure optimized for high-volume event ingestion.

## Core Components

### `ingest_event(event_type: str)`
Ingests an analytics event for processing and storage.

**Logs:**
- `event_ingested` — Logged when an event is successfully received and queued for processing
