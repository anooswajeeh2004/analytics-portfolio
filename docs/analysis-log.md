# Analysis log

Every time the data fooled me: what I believed, what was true, and how I found out.

## Entries

| Date       | Day   | What I believed  | What was true                        | How I found out                              |
| ---------- | ----- | ---------------- | ------------------------------------ | -------------------------------------------- |
| 2026-10-20 | Day 0 | Initial csv load | Schema mapping needed explicit types | Checked with head -n 1 and PostgreSQL errors |

## Day 3 Analysis Log

- **Window Frame Defaults:** Observed how `SUM(...) OVER (ORDER BY date)` includes all peer rows with identical dates by default. To track true running totals without tie-averaging, a tie-breaker column (like `order_id` or timestamp) is essential in the `ORDER BY` clause.
- **`LAG` vs Missing Dates:** Noticed that `LAG()` accesses the previous physical row in the partition rather than the actual previous calendar day. Always verify daily continuity before evaluating lags on time series.

## Log Entry — Day 04 (Three Revenue Numbers)

- **Initial Belief:** I believed Way 2 (customer payments) would equal Way 1 (item prices) plus freight, and that Way 3 would equal Way 1.
- **Reality:** Way 2 differs due to canceled orders with payments and small installment rounding differences. Way 3 significantly inflates total revenue due to join multiplication when orders have multiple payment methods.
- **How I Found Out:** By aggregating tables independently inside CTEs before joining, and reconciling every cent between the numbers.
