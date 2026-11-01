# Analysis log

Every time the data fooled me: what I believed, what was true, and how I found out.

## Entries

| Date       | Day   | What I believed                                                                                  | What was true                                                                                            | How I found out                                                                              |
| :--------- | :---- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| 2026-10-20 | Day 0 | Initial csv load                                                                                 | Schema mapping needed explicit types                                                                     | Checked with head -n 1 and PostgreSQL errors                                                 |
| 2026-10-20 | Day 0 | Believed CSV files would load cleanly with default types                                         | Schema mapping needed explicit types and custom casting                                                  | Checked with head -n 1 and PostgreSQL errors                                                 |
| 2026-10-21 | Day 1 | Assumed `order_item_id` alone is the primary key for `order_items`                               | `order_item_id` restarts per order; uniqueness requires a composite key (`order_id`, `order_item_id`)    | Found duplicate `order_item_id` values when querying count distinct across the table         |
| 2026-10-22 | Day 2 | Believed joining customers and geolocation would yield around 100,000 rows                       | The join generated 15,083,455 rows due to multi-coordinate zip codes                                     | Counted rows and evaluated zip code distributions                                            |
| 2026-10-23 | Day 3 | Expected `LAG()` to get yesterday's sales and `SUM() OVER` to process rows strictly sequentially | `LAG()` accesses the previous physical row, not calendar day; default frame includes ties in dates       | Saw aggregated totals jump on duplicate dates and gaps when days were missing in time series |
| 2026-10-24 | Day 4 | Believed Payment totals (Way 2) and Item totals (Way 1) would match perfectly                    | Way 2 differs due to canceled orders with payments and Way 3 inflates revenue due to join multiplication | Aggregated tables independently inside CTEs before joining and reconciled every cent         |
