## Part 0

- **Row counts:** Before cleaning, there were `99,441` rows. After using `dropna()`, the row count dropped to `96,461` (removing 2,980 orders, or 3.0% of the total dataset).
- **Statuses that disappeared completely:** `shipped`, `unavailable`, `invoiced`, `processing`, `created`, and `approved` orders are completely gone because they contain missing values in delivery or approval date columns.
- **Why `dropna()` kept the 6 canceled orders:** The 6 canceled orders kept by `dropna()` are the exact same canceled orders found in Warm-up 7 that somehow managed to receive a customer delivery date despite being canceled. Because they had no missing values in those specific checked columns, `dropna()` retained them.
- **Metric distortion:** The `cleaned` table gets the share of canceled orders wrong by reporting it as 0.01% instead of the true 0.63%, heavily distorting the cancellation rate.

## Part 1

### 1. The three kinds of missing values:

- **By accident (Missing Completely at Random):** Nothing in the data explains it. _Example:_ 8 orders have the status `delivered`, but have no customer delivery date.
- **Because of something you can see (Missing at Random):** Another column explains the gap. _Example:_ Orders that were never delivered (like `shipped` or `canceled`) have no delivery date because their status explains why.
- **Because of something you cannot see (Missing Not at Random):** It is missing because of what the value would be. _Example:_ Unhappy customers may choose not to write a review.

### 2. Analysis of the three data points:

- **Delivery date:** It is of the second kind ("because of something you can see"). _Choice:_ Leave it missing in the main table and handle it per specific delivery analysis.
- **Review message:** It is of the third kind ("because of something you cannot see"). _Choice:_ Leave it missing.
- **Product category:** It is of the first/second kind. _Choice:_ Fill text with the label `unknown` so they stay in `groupby` operations.

### 3. Exercises 1.a and 1.b answers:

- **1.a:** Orders with no approval time are mostly `canceled` or `created`. This is the second kind of missingness, explained by their early or canceled status.
- **1.b:** Orders with no review span across various statuses (mostly delivered). This is the third kind (missing not at random), where customers choose whether to review based on their experience, which the data cannot directly measure.

## Part 2

- **Step 1 counts:** Checked all seven main tables for exact duplicate rows. Every table printed `0` exact duplicates.
- **Step 2 counts:** Simulating a duplicated load with `pd.concat` on the sellers table resulted in 6,190 rows, 3,095 duplicates, and 3,095 unique rows after `drop_duplicates()`.
- **Step 3 counts:** Found `10,225` look-alike items in `order_items` (excluding `order_item_id`), representing R$ 847,719.70 in sales.
- **Why look-alike items are not copies:** They represent multiple individual units of the same product purchased within the same order (e.g., multiple quantities of a single item), rather than loading errors.
- **Exercise 2.a:** Counting duplicates using the composite keys for `order_items` (`order_id`, `order_item_id`) and `order_payments` (`order_id`, `payment_sequential`) yields `0` duplicates for both, proving their key integrity.
- **Exercise 2.b:** There are a few products sharing identical dimensions and weights except for their `product_id`. To be completely sure whether they are true duplicate entries or distinct products, we would need additional data such as supplier logs or catalog creation metadata.

## Part 3

### 1. Step 1 and Step 2 Value Evaluations:

- **Item price (min 0.85, max 6,735.0):** Possible.
- **Freight value (383 items with 0.00):** Possible (free shipping).
- **Product weight (4 products of 0 g):** Impossible.
- **Product weight (lightest at 2 g / heaviest at 40,425 g):** Not sure / possible extremes.

### 2. Step 4 Counts and Payments Log:

- **Carrier date before approval date:** 1,359 orders.
- **Customer delivery date before carrier date:** 23 orders.
- **Total orders flagged:** 1,382 orders.
- **Payments Log rows:** 5 rows generated (3 removed due to no type/money, 2 changed due to 0 installments).

### 3. Answers to Exercises 3.a to 3.f:

- **3.a:** The 4 products weighing 0 g are impossible; their weights were changed to missing (`NaN`) using `.mask()`.
- **3.b:** Items with shipping deadlines exceeding 365 days from purchase were logged and their deadlines made missing.
- **3.c:** Orders reaching the carrier before purchase are captured by or closely related to the chronological checks in `carrier_first`.
- **3.d:** Zero-value vouchers are possible (e.g., promotional or 100% discount vouchers); we keep them.
- **3.e:** Payments for orders without items represent orphaned transactions; we choose to flag or leave them out of item-level analysis.
- **3.f:** The 6 canceled orders with delivery dates are kept as flagged anomalies (either delivered before cancellation notice or status update error).

## Part 4

### 1. The 14 spellings of São Paulo found in Step 1:

Includes variations such as `sao paulo`, `sao paulo - sp`, `sao.paulo`, `sao paulo/sp`, `sao paulo sp`, `sao. paulo`, `s. paulo`, and other mixed formats combining city and state or punctuation differences.

### 2. The five changes in my own words:

1. **Character normalization:** Strips extra spaces, converts text to lowercase, removes accent marks, standardizes apostrophes, and collapses multiple spaces.
2. **Cutting extra parts:** Splits city names at hyphens, slashes, or commas and keeps only the primary name part.
3. **Removing trailing states:** Trims off state abbreviations if they appear at the end of the city string.
4. **Dictionary fixes:** Replaces known explicit typos and abbreviations (like `sbc` or `sao paulop`) with their proper full names.
5. **Filtering non-city entries:** Masks values containing digits, symbols like `@`, or matching state names into missing values (`NaN`).

### 3. Counts that changed:

- **Sellers in São Paulo:** Increased from 694 to 702.
- **Unique spellings count:** Dropped from 611 to 578.

### 4. Answers to Exercises 4.a and 4.b:

- **4.a:** Normalizing the `geolocation` table significantly reduces the number of unique city spellings, demonstrating massive text inconsistency across location records.
- **4.b:** By tracing the zip code prefix of sellers writing `sbc`, customer records with the same prefix confirm the city is predominantly São Bernardo do Campo.

## Part 5

The rule I am least sure about is **"shipping deadline more than a year after purchase"**. While a very long deadline is suspicious, there is a small chance that specialized custom-made products or pre-orders genuinely require extended manufacturing and shipping windows, making our 365-day cutoff a potential oversimplification.

## Errors seen today and lessons learned

1. **Error / Trap:** Attempting to use `dropna()` as a quick shortcut for dataset cleaning.
   - **Lesson:** `dropna()` silently destroys data integrity by removing entire categories of orders, altering fundamental business metrics like cancellation rates.
2. **Error / Trap:** Assuming look-alike item rows with duplicate product details are database errors.
   - **Lesson:** Always verify primary keys first; items with identical parameters are distinct units sold within the same order.
3. **Error / Trap:** Replacing impossible values (like 0 g weight) with calculated numbers like mean or zero.
   - **Lesson:** Never fabricate values in a clean table. An impossible value must become missing (`NaN`) rather than a guess.
