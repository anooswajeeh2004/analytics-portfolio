## Part 0

### 1. Explanation of the four numbers in the hardcoded formula:

- **854686.33:** Way 1 item revenue for August 2018 (strict sum of item prices).
- **148622.14:** Total freight value associated with those August orders.
- **19194.21:** Payments linked to orders that have no matching item records in the database.
- **-77.36:** Small reconciliation differences between item totals and payment values.

### 2. Rules broken by the hardcoded formula:

- **No hardcoded numbers inside formulas rule:** The formula embeds business numbers and financial totals directly as plain text rather than referencing input cells.
- **Auditing/Transparency rule:** A coworker or manager checking this sheet cannot trace where these four numbers originated, what orders they filter, or how to update the formula for September 2018. A number that nobody can check is a number that nobody should trust.

## Part 1

## Part 2

## Part 3

## Part 4
