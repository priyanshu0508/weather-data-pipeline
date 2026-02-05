# 📚 `docs/` (Technical Documentation)

### `docs/architecture.md`
```markdown
## System Architecture

The Weather Data Pipeline follows a layered architecture:

1. Ingestion Layer
   - API client fetches weather data

2. Processing Layer
   - ETL pipeline validates and transforms data

3. Storage Layer
   - Normalized relational database

4. Automation Layer
   - Scheduler triggers periodic ingestion

5. Monitoring Layer
   - Health checks and freshness detection

6. Reporting Layer
   - Aggregated analytics and system status
