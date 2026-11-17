## Part 0 — Too Many Points

The geolocation table contains 1,000,163 rows for 19,015 unique zip code prefixes.

- Total geolocation rows: 1,000,163
- Unique zip code prefixes: 19,015
- Median points per zip code: 29.0
- Maximum points for one zip code: 1,146

I also attempted to merge the customers table with the original geolocation table using pandas merge() and validate="many_to_one". The merge raised a MergeError because multiple geolocation records share the same zip code.

Without fixing this problem first, the join would duplicate customer records and increase the resulting number of rows to 15,083,455, approximately 152 rows per customer.

This showed why the geolocation table must be cleaned to contain only one point for each zip code before joining it with customers or sellers.

## Part 1 — One Point for Each Zip Code

### 1. Points Outside Brazil

I checked the geolocation coordinates using Brazil's approximate latitude and longitude boundaries. The result showed that 42 points were outside Brazil.

### 2. Building One Point for Each Zip Code

I created `src/analytics/geo.py` and implemented the `build_zip_points()` function.

The function filters out geographic points outside Brazil, groups the remaining records by zip code, and calculates the median latitude and longitude for each group. It also identifies the most common state using `value_counts()` and counts the remaining points using `size()`.

I used the median instead of the mean because it is less affected by distant or incorrect points.

### 3. Saving the Clean Geographic Table

I executed the module using `uv run python -m analytics.geo`.

The script generated 19,010 zip code points and saved them into the PostgreSQL table `clean.zip_points`. Five zip codes had no points remaining after filtering because all their original points were outside Brazil.

### 4. Visualizing the Zip Code Points

I retrieved the cleaned points from PostgreSQL and created a scatter plot using longitude on the X-axis and latitude on the Y-axis. The 19,010 points formed the approximate geographic shape of Brazil, with most points concentrated in the southeast.

### 5. Customers and Sellers Without Geographic Points

The results showed that 279 customers and 7 sellers had zip codes without a corresponding point in the cleaned table. This means their geographic travel distances cannot be calculated.

### Exercise 1.a — Zip Code with 1,146 Points

- Zip code: **[24220]**
- Most common state: **[RJ]**
- Most common city: **[niteroi]**

### Exercise 1.b — Zip Codes in Two States

I identified the eight zip codes that had geographic points in two different states and counted the points for each state.

**Result:** [MS,SP]

### What I Learned

I learned how to clean geographic data by filtering invalid coordinates, grouping records, and calculating median coordinates. I also practiced using pandas aggregation functions, lambda, value_counts(), and merge validation. Finally, I learned why each zip code needs one representative geographic point before joining it with customer and seller data.

## Part 2 — How far does each item travel?

### Distance Function

Created a `distance_km()` function using the Haversine formula to calculate the straight-line distance between two geographical points. The function converts latitude and longitude values from degrees to radians and returns the distance in kilometers.

Tested the function using São Paulo and Rio de Janeiro. The calculated distance was approximately **360.7 km**, which confirmed that the function was working correctly.

### Item Distance Analysis

Combined order, customer, seller, and product information from PostgreSQL with the ZIP Code coordinates created in Part 1. Added customer and seller coordinates to each item and calculated the distance between them.

Results:

- Total items: 112,650
- Items with missing distances: 555
- Median distance: 431.7 km

The missing distances occurred because some ZIP Codes did not have a corresponding location point.

### Exercises

- **2.a — Longest trip:**
- **2.b — Trips under 100 km:**

## Part 3 — Does distance explain freight and delivery time?

### Delivery Time

Added a `delivery_days` column by calculating the time between the purchase timestamp and the delivery timestamp. The duration was converted from seconds into days.

### Distance Bands

Grouped items into seven distance ranges using `pd.cut()`. For each range, calculated:

- Number of items.
- Average freight cost.
- Average delivery time.

The results showed that longer trips generally had higher freight costs and longer delivery times.

| Distance band |  Items | Average freight (R$) | Average delivery days |
| ------------- | -----: | -------------------: | --------------------: |
| 0–100 km      | 20,986 |                11.75 |                  6.53 |
| 100–300 km    | 15,588 |                16.40 |                  9.90 |
| 300–600 km    | 36,956 |                19.58 |                 12.54 |
| 600–1000 km   | 20,883 |                21.78 |                 14.63 |
| 1000–1500 km  |  7,613 |                26.22 |                 17.16 |
| 1500–2000 km  |  3,644 |                35.44 |                 19.40 |
| 2000–5000 km  |  6,425 |                35.92 |                 21.09 |

### Charts

Created two bar charts to compare average freight cost and delivery time across the distance bands. Both measures generally increased with distance.

The calculated distances are straight-line estimates, not actual road or transportation routes.

### Exercises

- **3.a — Weight and freight:**
- **3.b — Lightweight items:**

## Part 4 — Maps of Brazil

### Geographic Data

Downloaded the Brazil states GeoJSON file and loaded it using GeoPandas. The resulting GeoDataFrame contains the geographic boundaries of Brazil's 27 states and federal district.

### State-Level Metrics

Calculated three metrics for each state:

- Total number of orders.
- Percentage of orders delivered after the estimated delivery date.
- Average freight cost per item.

Merged these metrics with the geographic data using the state codes.

### Maps

Created three maps to compare the results across Brazil:

1. **Orders:** Shows where most customer orders come from. São Paulo has a much higher order count than other states.
2. **Late Orders:** Shows the percentage of orders delivered late. Some states have higher late delivery rates even with fewer orders.
3. **Freight:** Shows the average freight cost per item, which is generally higher in states farther from São Paulo.

The maps demonstrate why comparing rates is important. Order counts mainly show where customers are located, while percentages and averages help compare performance between states.

### Exercises

- **4.a — Promised delivery time:** [Add the average promised days for AM and AL and explain the difference between waiting time and late delivery.]
- **4.b — Average delivery time map:** [Add the state with the highest average delivery time.]

### Errors and Lessons Learned

- **PostgreSQL numeric rounding:** Learned that PostgreSQL may require converting a calculation to `numeric` before using `ROUND()` with a decimal-place argument.
- **Duplicate ZIP Code locations:** Learned that geolocation data can contain multiple points for the same ZIP Code. I used one representative point per ZIP Code to avoid creating duplicate rows during joins.
- **Missing geographic points:** Learned that some customer and seller ZIP Codes do not have a matching point in the cleaned geographic table. These missing values need to be considered when calculating distances.
