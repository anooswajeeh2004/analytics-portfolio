# Analytics Portfolio - Day 0: The Analyst's Workbench

## What this is

A structured analytics environment and data ingestion pipeline for the Olist E-commerce dataset using PostgreSQL and Python.

## What you need

- Python & uv
- PostgreSQL
- Git

## Setup

1. Clone the repository and run `uv sync`.
2. Create a PostgreSQL database named `olist`.
3. Copy `.env.example` to `.env` and fill in your database credentials.
4. Download the Olist dataset from Kaggle and place the CSV files inside `data/raw/olist/`.
5. Run the loader script to create tables and ingest data:
   ```bash
   uv run python -m analytics.load_olist
   ```
