# Day 12 — Distributions and Why the Average Can Be Wrong

## Part 0

### Mean, Median and Slow Orders

The mean delivery time is 12.56 days, while the median is 10.22 days. The maximum delivery time is 209.63 days.

There were 4,553 orders that took more than 30 days and 306 orders that took more than 60 days.

For a typical order, I would report the median of 10.22 days rather than the mean. The median better represents a typical delivery time because a small number of extremely slow orders pull the mean upward.

### Exercise 0.a

The share of orders taking longer than the mean is **[37.71]%**.

This share is below 50% because the delivery-time distribution is right-skewed. A small number of unusually long delivery times increase the mean, making it higher than the median.

## Part 1

### Delivery Days Distribution

The linear histogram shows that most orders are delivered within a relatively short period, while a small number take much longer. The logarithmic y-axis makes the low-frequency values in the long tail easier to see. The distribution is right-skewed and extends up to approximately 209.6 days.

### Item Price Distribution

The linear histogram shows that 84,833 out of 112,650 items fall into the first price range, which extends up to R$ 135.53. The logarithmic histogram reveals the price distribution more clearly. Approximately 80% of items cost between R$ 24 and R$ 230.

### Exercise 1.a — Freight Value Distribution

The freight values were plotted using both a linear histogram and a logarithmic x-axis. The logarithmic scale helps show the distribution across different shipping costs.

## Part 2

### Delivery Time Percentiles

The delivery time percentiles are:

| Percentile | Delivery Days |
| ---------- | ------------: |
| P50        |          10.2 |
| P90        |          23.1 |
| P99        |          46.0 |

P50 means that 50% of orders arrive within 10.2 days. P90 means that 90% arrive within 23.1 days, while P99 means that 99% arrive within 46 days.

### Item Price Percentiles

The item price percentiles are:

| Percentile | Item Price (R$) |
| ---------- | --------------: |
| P50        |           74.99 |
| P90        |          229.80 |
| P99        |          890.00 |

The median item price is R$ 74.99, while 90% of items cost R$ 229.80 or less.

### State Comparison

The median delivery times of MG and RJ are relatively close: 10.3 and 12.0 days. However, RJ has a higher P90 of 29.1 days compared with 20.2 days in MG, indicating that its slow orders take considerably longer.

### Exercise 2.a

The state with the highest P90-to-median ratio is **[RJ]**, with a ratio of **[2.43]**.

### Exercise 2.b

The mean promised delivery time is longer than the actual P90 in **[15] states**.

## Part 3

### Standard Deviation and Variance

The standard deviation of delivery times is 9.55 days, and the variance is 91.14 days squared.

The standard deviation measures how spread out the delivery times are around their mean. The variance is harder to interpret because it uses squared units.

### The Two-Standard-Deviation Window

The lower limit is -6.53 days, and the upper limit is 31.65 days. There are 0 orders below the lower limit and 3,878 orders above the upper limit.

The window fails for delivery times because the distribution is right-skewed. All observations outside the window are on the upper side, showing that the data is not symmetric around the mean.

### Exercise 3.a — Item Price Distribution

The lower limit of the item price window is **[-246.61]**, and the upper limit is **[487.92]**.

There are **[0]** items below the lower limit and **[3494]** items above the upper limit.

The results show that the item price distribution is not necessarily symmetric around its mean.

## Part 4

### Understanding Box Plots

A box plot summarizes the distribution of numerical data.

- The line inside the box represents the median (P50).
- The box extends from P25 to P75 and contains the middle 50% of observations.
- The whiskers extend to the most extreme observations within 1.5 times the interquartile range (IQR) from the quartiles.
- The dots represent outliers, which are values outside the whiskers.

### Comparing Six States

- **SP:** Its box is low and short, indicating that orders arrive relatively quickly and their delivery times are close together.
- **RJ:** Its upper whisker reaches much higher than MG's, indicating that some of its slower deliveries take longer.
- **AM:** Its box is high and tall, indicating longer delivery times and a wider middle 50% spread.

### Exercise 4.a — Item Prices by Category

We selected the five product categories with the highest item counts and created a box plot of their item prices using a logarithmic y-axis.

This category has the largest visual box height on the logarithmic scale, indicating the widest relative spread between P25 and P75.

## Part 5

### Anscombe's Four Datasets

We downloaded Anscombe's dataset and calculated the mean and standard deviation for each of the four datasets.

All four datasets have the same summary statistics:

| Dataset | X Mean | Y Mean | X Std | Y Std |
| ------- | -----: | -----: | ----: | ----: |
| I       |    9.0 |    7.5 |  3.32 |  2.03 |
| II      |    9.0 |    7.5 |  3.32 |  2.03 |
| III     |    9.0 |    7.5 |  3.32 |  2.03 |
| IV      |    9.0 |    7.5 |  3.32 |  2.03 |

### Visual Differences

Although all four datasets have the same means and standard deviations, their visual patterns are very different:

- **Dataset I:** The points are scattered around a straight-line pattern.
- **Dataset II:** The points form a curved pattern.
- **Dataset III:** The points follow a roughly straight line, but one point is far from the others.
- **Dataset IV:** Almost all points have an x-value of 8, except for one point.

These differences show that summary statistics alone cannot fully describe a dataset. Visualizing the data is essential.

### Exercise 5.a — Effect of One Extreme Point

After removing the observation with the largest y-value from Dataset III:

- The mean of y decreased from 7.50 to 6.98.
- The standard deviation of y decreased from 2.03 to 1.11.

This demonstrates that a single extreme point can significantly affect both the mean and standard deviation.

## Errors and What They Taught Me

No errors were encountered during today's analysis. The notebook executed successfully, and all required visualizations and analysis outputs were generated.
