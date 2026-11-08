# Day 0 Write-up

## The problems

During the initial setup and running of notebook B9, several technical issues were encountered and resolved across Day 0 steps:

1. **Missing Dependencies & Virtual Environment Issues:**
   - **Problem:** Running the setup notebook failed due to missing Python libraries and unconfigured local environment paths.
   - **Fix (Part 0 Setup):** Created and activated a dedicated Python virtual environment using `uv` and ran `uv sync` to automatically install all required packages cleanly.

2. **Database Path & Connection Failures (`PROJECT_ROOT`):**
   - **Problem:** Relative database paths caused connection errors when trying to create or query the SQLite database from different cell contexts.
   - **Fix (Part 0 Database Setup):** Configured standard environment paths (`analytics.db` module) to dynamically compute `PROJECT_ROOT`, ensuring reliable database access across all notebooks.

3. **Schema Data Type & CSV Insertion Mismatches:**
   - **Problem:** Default text data types for all columns led to precision loss in financial fields and prevented date-based SQL queries.
   - **Fix (Part 0 Schema Definition):** Defined custom table schemas explicitly using `numeric(10,2)` for financial fields (`price`, `payment_value`), `timestamp` for order dates, and `text` for zip code prefixes to preserve leading zeros.

---

## The stranger test

- **Time taken:** ~3 minutes for a fresh clone, setting up environment variables, running `uv sync`, and executing all setup scripts successfully.
- **README adjustments made:** Ensured explicit path instructions for data directories and setup sequence.

---

## Types

- **Financial Precision:** Used `numeric(10,2)` for prices and payment values to eliminate floating-point rounding errors.
- **Temporal Analysis:** Used `timestamp` instead of string types for all order timestamps to enable native SQL date functions and interval calculations.
- **Leading Zeros:** Stored Brazilian zip codes as `text` rather than integers to preserve leading zeros (e.g., prefixes starting with '0').
