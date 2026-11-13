## Part 0

- **Holidays in 2017:** The year 2017 has 13 national holidays.
- **API Error for Year 1800:** When querying the API for the year 1800, it returned a JSON error response stating `{"message": "Ano fora do intervalo suportado entre 1900 e 2199.", "type": "feriados_range_error", "name": "NotFoundError"}`, indicating that the requested year is outside the supported range between 1900 and 2199.

## Part 1

- **Status Code & Dataset Shape:** The initial API request returned a status code of `200`, and the aggregated `holidays` DataFrame has a shape of `(39, 4)`.
- **Why save `response.text` first:** Saving the raw response text locally ensures that our data pipeline remains fully independent of web availability, network speed, or potential future API changes.
- **Exercise 1.a (Weekend Holidays):** Out of the 7 holidays.
- **Exercise 1.b (Variable Date Holidays):** Holidays that change dates each year (such as Carnaval, Sexta-feira Santa, Páscoa, and Corpus Christi) were successfully identified by having multiple unique month-day combinations across the 3-year span.

## Part 2

- **Page Keys & Rates Shape:** The response dictionary keys are `dict_keys(['@odata.context', 'value'])`, and the fully aggregated `rates` DataFrame has a shape of `(542, 3)`.
- **Why the JSON is nested:** The JSON is nested because the top-level response is a dictionary containing metadata and a key named `value`, whose value is itself a list of dictionaries containing individual exchange rate records.
- **Exercise 2.a (Highest & Lowest Dollar Rates):**
  - Most expensive (highest sell price): R$ 4.2061 on 22 September 2018.
  - Cheapest (lowest sell price): R$ 3.1191 on 8 September 2017.
- **Exercise 2.b (Spread between Sell and Buy):**
  - The largest absolute difference between `sell` and `buy` is R$ 0.0503 (representing approximately 1.25% to 1.30% of the selling price).
  - For high-level macro sales reporting, this minor spread is negligible and does not alter the general financial narrative.

## Part 3

### 1. Step 5 Printed Output (Timeout & Retries):

Try 1 of 3 failed: ReadTimeout
Try 2 of 3 failed: ReadTimeout
Try 3 of 3 failed: ReadTimeout
https://brasilapi.com.br/api/feriados/v1/2017 failed 3 times. The last problem: ReadTimeout

2. Status Codes Worth a Second Try:
   429 (Too Many Requests): Occurs when sending requests too fast; waiting and retrying usually resolves it.

500, 502, 503, 504 (Server Errors): Indicate temporary server failure or overload; a short wait allows the server to recover.

3. Answers to Exercises (3.a & 3.b):
   3.a: Querying the PTAX API with '31-12-2017' fails because the API strictly expects the US month-day-year format (MM-DD-YYYY). Passing '31-12-2017' put 31 in the month position, causing an invalid month error.

3.b: get does not retry after a 404 because a 404 status code means the requested resource does not exist. Repeating an identical request for a non-existent resource will always fail, so retrying is pointless.

## Part 4

### 1. Program Output (Steps 2 & 3):

- **Initial run (nothing missing):**
  ```text
  clean.holidays     39 rows, 2016-01-01 to 2018-12-25
  clean.usd_rates   542 rows, 2016-09-01 to 2018-10-31
  ```
  fter deleting ptax-0200.json and re-running:Plaintextsaved ptax-0200.json
  clean.holidays 39 rows, 2016-01-01 to 2018-12-25
  clean.usd_rates 542 rows, 2016-09-01 to 2018-10-31

2. Step 4 Output Table

3.Answers to Exercises (4.a & 4.b):
4.a: holidays_schema and rates_schema were successfully created, imported into web.py, and used to validate both tables using lazy=True inside main() before writing to PostgreSQL.
4.b: Out of the 23 weekdays with no price, exactly 2 days correspond to Carnaval.

## Part 5

### 1. Steps 1, 2, and 3 Results:

- **Step 1 (Daily Sales in BRL):** The sales query returned `(602, 2)` with a total of R$ 15,683,706.74 across 602 days.
- **Step 2 (Inner Join Loss):** An inner join with daily exchange rates yielded `(413, 11779628.87)`, losing 189 days and R$ 3,904,077.87 (24.9% of total sales) silently without any error.
- **Step 3 (Using `merge_asof`):** Using `pd.merge_asof` with `direction="backward"` successfully restored all 602 days (0 missing prices), resulting in a total of $4,670,445.60 USD.

### 2. Why Inner Join Lost Sales & How `merge_asof` Fixes It:

- An inner join drops any date that is missing from the right table (such as weekends and national holidays when the Central Bank publishes no rates), resulting in silent data loss.
- `merge_asof` fixes this by matching each sale date to the closest preceding available exchange rate (e.g., assigning Friday's rate to Saturday and Sunday), preserving all sales records.

### 3. Answers to Exercises (5.a, 5.b, & 5.c):

- **5.a:**
  - Highest month in BRL: November 2017.
  - Highest month in USD: November 2017.
- **5.b:** Using the `buy` rate instead of `sell` increases the total USD sales by approximately $140,000, since buying rates are slightly lower than selling rates.
- **5.c:** Comparing January–August 2017 to January–August 2018 shows a growth of **+43.5%** in Brazilian Reais (BRL), but only **+16.2%** in US Dollars (USD) due to currency depreciation.

## Today's Errors and Lessons

1. **PTAX Date Format Error (Day 9, Part 3):**
   - _Error:_ Passing an inverted date format (`31-12-2017`) caused API validation failures.
   - _Lesson:_ Always respect the specific API schema requirements (in this case, US format `MM-DD-YYYY`).

2. **Silent Data Loss via Inner Joins (Day 9, Part 5):**
   - _Error:_ An inner join between sales and daily exchange rates silently omitted 189 days without raising any code exceptions.
   - _Lesson:_ Date-based joins require careful validation (`indicator=True`, `merge_asof`) to prevent silent dropping of weekends and holidays.
