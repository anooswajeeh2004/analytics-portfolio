# Day 0 Write-up

## The problems

- Resolved environment path disparities (`PROJECT_ROOT`) to reliably locate configuration and SQL files.
- Adjusted table schemas to explicitly handle correct data types instead of default text mapping.

## The stranger test

- Time taken: ~15 minutes.
- README adjustments made: Ensured explicit path instructions for data directories.

## Types

- Used `numeric(10,2)` for financial prices and payments to ensure precision.
- Used `timestamp` instead of string/text for dates to enable time-based querying.
