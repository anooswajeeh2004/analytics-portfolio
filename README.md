# Analytics Portfolio

A structured analytics environment and data ingestion pipeline for the Olist E-commerce dataset.

## What you need

- [uv](https://docs.astral.sh/uv/) — Python package and project manager.
- [PostgreSQL](https://www.postgresql.org/download/) — Relational database management system.
- Git.

## Setup

1. Clone the repository and navigate to the project directory.

   ```bash
   git clone https://github.com/anooswajeeh2004/analytics-portfolio.git
   cd analytics-portfolio
   ```

2. Create a PostgreSQL database named `olist`.

   You can create it in pgAdmin or execute the following SQL statement using an account with permission to create databases:

   ```sql
   CREATE DATABASE olist;
   ```

3. Copy `.env.example` to `.env` in the project root and fill in your database credentials.

   Replace `CHANGE_ME` with your PostgreSQL password and check that the database name is `olist`.

   Keep `.env` private and ensure it is excluded from Git through `.gitignore`.

4. Download the Olist dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), extract the files, and place the CSV files inside:

   ```text
   data/raw/olist/
   ```

5. Install the project dependencies and run the data loader from the project root:

   ```bash
   uv sync
   uv run python -m analytics.load_olist
   ```

   The loader is expected to create the required tables and load the nine dataset files.
   Check its output and the database to confirm that all tables loaded successfully and that their row counts match the source files.

## Project layout

| Directory / File | Description                                                                          |
| ---------------- | ------------------------------------------------------------------------------------ |
| `data/`          | Raw datasets in `raw/olist/` and processed data.                                     |
| `notebooks/`     | Jupyter notebooks for analysis and workbenches.                                      |
| `sql/`           | SQL schema creation scripts and queries.                                             |
| `src/`           | Python source code, including `db.py`, `load_olist.py`, `paths.py`, and `checks.py`. |
| `reports/`       | Generated analysis reports and charts.                                               |
| `docs/`          | Documentation and workbench logs.                                                    |
| `pyproject.toml` | Project configuration and dependencies.                                              |
| `.env.example`   | Example environment configuration without private credentials.                       |
| `.env`           | Local database credentials; do not commit this file.                                 |

## Running the notebooks

1. Open a Jupyter notebook from `notebooks/` in VS Code, such as `day-00-workbench.ipynb`.
2. Select the Python kernel associated with the project's `.venv` environment.
3. Restart the kernel and select **Run All** to execute all cells from top to bottom.
4. Review the outputs and resolve any errors before continuing the analysis.
