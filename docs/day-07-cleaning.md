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
- **Review message:** It is of the second kind (another column explains it), because review scores show that 23.5% of 1-star reviews have no message compared to 68.8% of 4-star reviews. _Choice:_ Leave it missing.
- **Product category:** It is a missing catalog entry (the same 610 products miss category, name length, description length, and photo count together). _Choice:_ Fill text with the label `unknown` so they stay in `groupby` operations.

### 3. Exercises 1.a and 1.b answers:

- **1.a:** A total of **160** orders have no approval time. They split into two kinds: for the 141 `canceled` and 5 `created` orders, the status explains it (second kind); for the 14 `delivered` orders, nothing explains it and all have delivery dates (first kind).
- **1.b:** A total of **768** orders have no review, spanning across various statuses (mostly delivered). This is the third kind (missing not at random), where customers choose whether to review based on their experience, which the data cannot directly measure.

## Part 2

- **Step 1 counts:** Checked all seven main tables for exact duplicate rows. Every table printed `0` exact duplicates.
- **Step 2 counts:** Simulating a duplicated load with `pd.concat` on the sellers table resulted in 6,190 rows, 3,095 duplicates, and 3,095 unique rows after `drop_duplicates()`.
- **Step 3 counts:** Found `10,225` look-alike items in `order_items` (excluding `order_item_id`), representing R$ 847,719.70 in sales.
- **Why look-alike items are not copies:** They represent multiple individual units of the same product purchased within the same order (e.g., multiple quantities of a single item), rather than loading errors.
- **Exercise 2.a:** Counting duplicates using the composite keys for `order_items` (`order_id`, `order_item_id`) and `order_payments` (`order_id`, `payment_sequential`) yields `0` duplicates for both, proving their key integrity.
- **Exercise 2.b:** There are **695** products sharing identical attributes and dimensions except for their `product_id`. We cannot call them duplicate copies because distinct products (such as different color variants or different catalog SKUs) often share identical physical measurements, so they remain kept as unique products.

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
- **Payments Log rows:** 5 rows generated (3 removed due to no type/money, 2 changed due to 0 installments):

| table          | key                                | column               | old_value   | new_value     | action  | rule                         |
| :------------- | :--------------------------------- | :------------------- | :---------- | :------------ | :------ | :--------------------------- |
| order_payments | 4637ca194b6387e2d538dc89b124b0ee/1 | payment_type         | not_defined | (row removed) | removed | no payment type and no money |
| order_payments | 00b1cb0320190ca0daa2c88b35206009/1 | payment_type         | not_defined | (row removed) | removed | no payment type and no money |
| order_payments | c8c528189310eaa44a745b8d9d26908b/1 | payment_type         | not_defined | (row removed) | removed | no payment type and no money |
| order_payments | 744bade1fcf9ff3f31d860ace076d422/2 | payment_installments | 0           | (missing)     | changed | 0 installments is impossible |
| order_payments | 1a57108394169c0b47d8f876acc9ba2d/2 | payment_installments | 0           | (missing)     | changed | 0 installments is impossible |

### 3. Answers to Exercises 3.a to 3.f:

- **3.a:** The 4 products weighing 0 g are impossible; their weights were changed to missing (`NaN`) using `.mask()`.
- **3.b:** The 4 items with shipping deadlines exceeding 365 days from purchase were logged and their deadlines successfully made missing (`NaN`) using `.mask()`.
- **3.c:** A total of 166 orders have carrier dates before purchase dates. Exactly 0 of them are outside `carrier_first`, meaning all of these timeline anomalies are fully captured by `carrier_first`.
- **3.d:** Zero-value vouchers are possible (e.g., promotional or 100% discount vouchers); we keep them.
- **3.e:** There are **775** orders with no items with **830** payment rows (totaling 162,591.95 in value). They represent orphaned transactions and are kept.
- **3.f:** The 6 canceled orders with delivery dates are kept as they are as orders might have been processed before cancellation notices.

## Part 4

### The 14 spellings and their counts from Step 1:

- `sao paulo`: 694
- `sp`: 4
- `sao paulo - sp`: 3
- `paulo lopes`: 2
- `sao paulo / sao paulo`: 1
- `são paulo`: 1
- `santo andre/sao paulo`: 1
- `maua/sao paulo`: 1
- `sao paulo sp`: 1
- `sao  paulo`: 1
- `ribeirao preto / sao paulo`: 1
- `carapicuiba / sao paulo`: 1
- `sao paulop`: 1
- `jacarei / sao paulo`: 1

### 2. The five changes in my own words:

1. **Character normalization:** Strips extra spaces, converts text to lowercase, removes accent marks, standardizes apostrophes, and collapses multiple spaces.
2. **Cutting extra parts:** Splits city names at hyphens, slashes, or commas and keeps only the primary name part.
3. **Removing trailing states:** Trims off only the seller's own state suffix, not every state.
4. **Dictionary fixes:** Replaces known explicit typos and abbreviations (like `sbc` or `sao paulop`) with their proper full names.
5. **Filtering non-city entries:** Catches a digit or an `@`, or a city that is only the state, masking them into missing values (`NaN`).

### 3. Counts that changed:

- **Sellers in São Paulo:** Increased from 694 to 702.
- **Unique spellings count:** Dropped from 611 to 578.

### 4. Answers to Exercises 4.a and 4.b:

- **4.a:** Normalizing the `geolocation` table reduces unique city spellings from 8,011 to 5,942 (a reduction of 2,069 variations). This confirms the severe text inconsistency across location records analyzed since Day 1.
- **4.b:** Tracing the seller zip code prefixes (09726, 09861) associated with `sbc` shows that all 46 matching customer records live in São Bernardo do Campo, confirming the abbreviation without ambiguity.

## Part 5

The rule I am least sure about is **"shipping deadline more than a year after purchase"**. While a very long deadline is suspicious, there is a small chance that specialized custom-made products or pre-orders genuinely require extended manufacturing and shipping windows, making our 365-day cutoff a potential oversimplification.

## Errors seen today and lessons learned

--None
