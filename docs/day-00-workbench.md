# Day 0 Write-up

## The problems

- Resolved environment path disparities (`PROJECT_ROOT`) to reliably locate configuration and SQL files.
- Adjusted table schemas during database initialization (Part 0) to explicitly handle correct data types instead of default text mapping, overcoming CSV insertion errors.

## The stranger test

- Time taken: ~3 minutes for a fresh clone, setting up environment variables, running `uv sync`, and executing all setup scripts successfully.
- README adjustments made: Ensured explicit path instructions for data directories and setup sequence.

## Types

- Used `numeric(10,2)` for financial prices and payments to ensure precision.
- Used `timestamp` instead of string/text for dates to enable time-based query extraction.
- Stored Brazilian zip codes as `text` rather than integer types to preserve leading zeros (e.g., zip codes starting with '0').
