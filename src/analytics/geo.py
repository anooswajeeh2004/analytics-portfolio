from analytics.db import execute, get_engine, query
import numpy as np


def build_zip_points(geo):
    inside = geo["geolocation_lat"].between(-34, 6) & geo["geolocation_lng"].between(
        -75, -34
    )

    points = (
        geo[inside]
        .groupby("geolocation_zip_code_prefix")
        .agg(
            lat=("geolocation_lat", "median"),
            lng=("geolocation_lng", "median"),
            state=("geolocation_state", lambda states: states.value_counts().index[0]),
            rows=("geolocation_lat", "size"),
        )
    )

    return points.reset_index().rename(
        columns={"geolocation_zip_code_prefix": "zip_prefix"}
    )


def distance_km(lat1, lng1, lat2, lng2):
    lat1, lng1, lat2, lng2 = (np.radians(value) for value in (lat1, lng1, lat2, lng2))

    a = (
        np.sin((lat2 - lat1) / 2) ** 2
        + np.cos(lat1) * np.cos(lat2) * np.sin((lng2 - lng1) / 2) ** 2
    )

    return 2 * 6371 * np.arcsin(np.sqrt(a))


def main():
    points = build_zip_points(query("SELECT * FROM geolocation"))
    execute("CREATE SCHEMA IF NOT EXISTS clean")
    points.to_sql(
        "zip_points", get_engine(), schema="clean", if_exists="replace", index=False
    )
    print(f"clean.zip_points {len(points):,} zip codes")


if __name__ == "__main__":
    main()
