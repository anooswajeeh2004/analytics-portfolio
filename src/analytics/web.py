import json
import time

import pandas as pd
import requests

from analytics.db import execute, get_engine
from analytics.paths import RAW_WEB
from analytics.schemas import holidays_schema, rates_schema

TRY_AGAIN = [429, 500, 502, 503, 504]


def get(url, params=None, tries=3, timeout=30):
    for attempt in range(1, tries + 1):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            if response.status_code not in TRY_AGAIN:
                response.raise_for_status()
                return response
            problem = f"HTTP {response.status_code}"
        except (requests.ConnectionError, requests.Timeout) as error:
            problem = type(error).__name__
        print(f"Try {attempt} of {tries} failed: {problem}")
        if attempt < tries:
            time.sleep(2**attempt)
    raise RuntimeError(f"{url} failed {tries} times. The last problem: {problem}")


HOLIDAYS_URL = "https://brasilapi.com.br/api/feriados/v1/{year}"
PTAX_URL = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
)
PAGE_SIZE = 100


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def download(path, url, params=None):
    if path.exists():
        return
    response = get(url, params)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(response.text, encoding="utf-8")
    print("saved", path.name)
    time.sleep(1)


def download_holidays(years):
    for year in years:
        download(
            RAW_WEB / "brasilapi" / f"holidays-{year}.json",
            HOLIDAYS_URL.format(year=year),
        )


def download_rates(first_day, last_day):
    params = {
        "@dataInicial": f"'{first_day}'",
        "@dataFinalCotacao": f"'{last_day}'",
        "$format": "json",
        "$orderby": "dataHoraCotacao",
        "$top": PAGE_SIZE,
    }
    skip = 0
    while True:
        path = RAW_WEB / "bcb" / f"ptax-{skip:04d}.json"
        download(path, PTAX_URL, params | {"$skip": skip})
        if len(read_json(path)["value"]) < PAGE_SIZE:
            return
        skip += PAGE_SIZE


def build_holidays():
    rows = []
    for path in sorted((RAW_WEB / "brasilapi").glob("holidays-*.json")):
        rows.extend(read_json(path))
    holidays = pd.DataFrame(rows)
    return pd.DataFrame(
        {
            "date": pd.to_datetime(holidays["date"], format="%Y-%m-%d"),
            "name": holidays["name"],
        }
    )


def build_rates():
    pages = [read_json(path) for path in sorted((RAW_WEB / "bcb").glob("ptax-*.json"))]
    rates = pd.concat(
        [pd.json_normalize(page, record_path="value") for page in pages],
        ignore_index=True,
    )
    return pd.DataFrame(
        {
            "date": pd.to_datetime(
                rates["dataHoraCotacao"].str[:10], format="%Y-%m-%d"
            ),
            "buy": rates["cotacaoCompra"],
            "sell": rates["cotacaoVenda"],
        }
    )


def main():
    download_holidays([2016, 2017, 2018])
    download_rates("09-01-2016", "10-31-2018")
    # day 9 - ex:4.a
    tables = {"holidays": build_holidays(), "usd_rates": build_rates()}
    holidays_schema.validate(tables["holidays"], lazy=True)
    rates_schema.validate(tables["usd_rates"], lazy=True)
    # ----------
    execute("CREATE SCHEMA IF NOT EXISTS clean")
    for name, table in tables.items():
        table.to_sql(
            name, get_engine(), schema="clean", if_exists="replace", index=False
        )
        print(
            f"clean.{name:<10} {len(table):>4} rows, {table['date'].min():%Y-%m-%d} to {table['date'].max():%Y-%m-%d}"
        )


if __name__ == "__main__":
    main()
