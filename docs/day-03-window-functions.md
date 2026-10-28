# Day 3: Window Functions — Learnings & PostgreSQL Errors

## Key Takeaways

1. **Window vs Group By:** `GROUP BY` collapses rows into a single summary row, whereas window functions append aggregated values to every individual row without losing original details.
2. **Execution Order:** PostgreSQL evaluates `WHERE` before window functions. Filtering window functions directly in a `WHERE` clause causes an error and requires a CTE wrapper.
3. **Tie-Breakers:** Truncations and row rankings (`ROW_NUMBER`) require explicit tie-breakers to produce deterministic and reproducible results across query runs.

## PostgreSQL Errors Encountered & Lessons Learned

1. `ERROR: window functions are not allowed in WHERE`
   - _Lesson Learned:_ Window functions are computed at stage 4 of query execution (after `GROUP BY` and `WHERE`). To filter based on a window function result (such as `RANK() <= 3`), calculate the window in a CTE first, then apply the `WHERE` condition in the outer query.

2. `ERROR: column "x" must appear in the GROUP BY clause or be used in an aggregate function`
   - _Lesson Learned:_ When combining regular `GROUP BY` with window functions, any non-window column must be explicitly included in the `GROUP BY` list.
