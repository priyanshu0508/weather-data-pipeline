# Weather Data Pipeline System

An end-to-end data engineering project that builds a complete weather data pipeline using the OpenWeatherMap API.  
The system ingests real-time weather data, validates and stores it in a SQL database, automates collection, monitors pipeline health, and generates analytical reports.

This project evolves through four maturity levels:
- Option 1: Core ETL pipeline
- Option 2: Automation and multi-city support
- Option 3: Monitoring and alerting
- Option 4: Enterprise-ready architecture with database abstraction

---

## System Overview

The pipeline performs the following steps:
1. Fetches weather data from OpenWeatherMap API
2. Validates and cleans incoming data
3. Loads data into a normalized SQL database
4. Automates ingestion using a scheduler
5. Monitors pipeline health and data freshness
6. Generates analytical and monitoring reports

---

## Architecture Overview

- API Layer: OpenWeatherMap REST API
- ETL Layer: Python-based extract, transform, load logic
- Storage Layer: SQLite (default), PostgreSQL ready
- Automation: Scheduler-driven ingestion
- Monitoring: Health checks and status reporting
- Reporting: Aggregated weather analytics

---

## Tech Stack

- Python 3.9+
- SQLite (default database)
- PostgreSQL (enterprise-ready)
- OpenWeatherMap API
- python-dotenv
- requests

---

## Project Structure

weather-data-pipeline/
├── config (Configuration file)
├── app/ (Source code modules)
├── database (Database file and schema)
├── docs/ (Technical documentation)
├── logs/(Sample log files)
├── reports/(Sample generated reports)
├── requirements.txt
└── README.md


