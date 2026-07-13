# API Data Pipeline

## Overview

A modular Python ETL pipeline that extracts user data from a REST API, transforms it using Pandas, and stores both raw and processed datasets.

## Architecture

REST API
↓
Extract
↓
Transform
↓
Raw JSON
+
Processed Parquet

## Technologies

- Python
- Requests
- Pandas
- PyArrow

## Project Structure

(api-data-pipeline tree)

## How to Run

1. Clone the repository
2. Create a virtual environment
3. Install dependencies

pip install -r requirements.txt

4. Run

python main.py

## Output

The pipeline generates:

- data/raw/users.json
- data/processed/users.parquet

Sample output files are included in this repository for demonstration purposes.

## Roadmap

Version 1.0
- Local ETL Pipeline ✅

Planned Enhancements

- Google Cloud Storage
- Airflow Orchestration
- Incremental Loads
- Logging
- Docker
- BigQuery