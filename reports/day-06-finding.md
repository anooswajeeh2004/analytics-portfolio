# Day 6 — Category Growth

## The question

Which product categories grew the most from October to November 2017,
the month of Black Friday?

## The answer

Among categories with at least 100 items in October, furniture_decor
had the highest growth ratio at 2.07, followed by garden_tools at 1.96
and fashion_bags_accessories at 1.82.

Across all categories, item counts increased from 5,322 in October to
8,665 in November: a growth ratio of approximately 1.63 .
Ten of the 18 qualifying categories grew faster than the
overall item count.

The table counts item rows ordered in each purchase month, including
orders of any status. It includes only categories with at least
100 items in October.

Growth ratio = November item count / October item count.

| Category                 | October items | November items | Growth ratio |
| ------------------------ | ------------: | -------------: | -----------: |
| furniture_decor          |           379 |            783 |         2.07 |
| garden_tools             |           281 |            550 |         1.96 |
| fashion_bags_accessories |           110 |            200 |         1.82 |
| housewares               |           235 |            423 |         1.80 |
| bed_bath_table           |           545 |            975 |         1.79 |
| auto                     |           150 |            263 |         1.75 |
| toys                     |           290 |            495 |         1.71 |
| computers_accessories    |           322 |            532 |         1.65 |
| perfumery                |           189 |            311 |         1.65 |
| stationery               |           101 |            166 |         1.64 |
| health_beauty            |           361 |            584 |         1.62 |
| telephony                |           253 |            383 |         1.51 |
| watches_gifts            |           314 |            469 |         1.49 |
| baby                     |           138 |            203 |         1.47 |
| sports_leisure           |           471 |            612 |         1.30 |
| consoles_games           |           109 |            134 |         1.23 |
| cool_stuff               |           258 |            302 |         1.17 |
| office_furniture         |           102 |            102 |         1.00 |

## How sure I am

Pandas and Polars returned matching category names, ordering, and rounded
growth ratios, and the joins used relationship validation. The results
describe item-count changes, not revenue or completed sales, and do not
prove that Black Friday caused the growth.

## What to do next

Complete the comparison with a minimum October count of 50 to assess
how the threshold affects the ranking. Compare delivered-only results
and item counts per day to assess sensitivity to order status and
different month lengths.
