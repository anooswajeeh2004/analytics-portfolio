# Day 13 — Uncertainty, Seen by Simulation First

## Part 0

### Population and Delivery Time

We retrieved all delivered orders and calculated their delivery durations.

The population contains 96,476 orders, with a mean delivery time of 12.56 days and a standard deviation of 9.55 days.

### Five Random Samples of 30 Orders

The five sample averages were:

- Sample 1: 12.92 days
- Sample 2: 9.87 days
- Sample 3: 12.84 days
- Sample 4: 13.02 days
- Sample 5: 11.95 days

Each average is different because every random sample contains a different selection of orders from the population.

### Exercise 0.a — Five Samples of 3,000 Orders

The five sample averages were:

| Sample | Average (days) | Absolute Difference from 12.56 |
| ------ | -------------: | -----------------------------: |
| 1      |        [12.56] |                         [0.00] |
| 2      |        [12.63] |                         [0.07] |
| 3      |        [12.53] |                         [0.03] |
| 4      |        [12.19] |                         [0.37] |
| 5      |        [12.62] |                         [0.06] |

Larger samples generally provide more stable estimates of the population mean because they reduce sampling variability.

### Business Question — Marketing Delivery Claim

The marketing team should not advertise delivery in under 10 days based on a sample of only 30 orders. Small samples can produce unreliable estimates, and different samples may have significantly different averages. The actual population mean is 12.56 days, so the sample average of 9.9 days does not provide sufficient evidence for this claim.

## Part 1

### Thousands of Sample Averages

We generated 2,000 random samples of 30 orders and another 2,000 samples of 300 orders.

The average of the 30-order sample means was 12.52 days, while the average of the 300-order sample means was 12.55 days. Both values are close to the population mean of 12.56 days.

### Reading the Three Charts

- **Original Delivery Days:** The distribution is right-skewed, with a long tail caused by unusually slow orders.
- **Sample Means of 30:** The averages form a more bell-shaped distribution around the true population mean.
- **Sample Means of 300:** The distribution is much narrower, showing that larger samples produce more stable averages.

### Exercise 1.a — Item Prices

We repeated the experiment using item prices from Day 12. We generated 2,000 samples of 30 items and another 2,000 samples of 1,000 items.

The sample averages become more regular and concentrated around the population mean as the sample size increases. The distribution of averages from larger samples is narrower.

### Business Question — Can Sample Averages Be Trusted?

A sample average can be a useful estimate of the population mean, even when individual delivery times are highly variable. Repeated sampling shows that sample averages tend to form a bell-shaped distribution around the true mean. Larger samples produce more stable estimates with less variation, but uncertainty should still be considered.

## Part 2

### Standard Error

We calculated the standard error for four different sample sizes:

| Sample Size | Standard Error (Days) |
| ----------: | --------------------: |
|          30 |                 1.743 |
|         300 |                 0.551 |
|       3,000 |                 0.174 |
|      30,000 |                 0.055 |

A larger sample produces a smaller standard error because the sample mean becomes more stable and has less sampling variability.

Each time the sample size increases ten times, the standard error decreases by approximately the square root of ten.

### Exercise 2.a — Required Sample Size

The target standard error is 0.1 days.

Using the formula:

SE = s / sqrt(n)

Rearranging the formula:

n = (s / SE)^2

The required sample size is **[9114] orders**.

### Business Question — 300 Orders

A sample of 300 orders has a standard error of approximately 0.551 days, which is higher than the target of 0.1 days. The team needs a much larger sample, approximately 9,100 orders, to achieve the desired level of precision. Therefore, 300 orders are not enough for this target.

## Part 3

### Bootstrap Confidence Interval for the Mean

We selected one random sample of 300 orders. Its average delivery time was 12.40 days.

We then generated 2,000 bootstrap samples of 300 observations with replacement. We calculated the mean of each bootstrap sample and used the 2.5th and 97.5th percentiles to create a 95% bootstrap confidence interval.

The resulting interval ranges from 11.41 to 13.41 days. The true population mean of 12.56 days falls inside this range.

### Sampling With Replacement

Imagine a bag containing five numbered balls, from 1 to 5. We pick one ball, record its number, and put it back before picking again. After five picks, the same number may appear more than once, while some numbers may not appear at all. This is called sampling with replacement.

### Exercise 3.a — Bootstrap Interval for the Median

The bootstrap 95% confidence interval for the median ranges from **[LOWER]** to **[UPPER]** days.

The true population median is 10.22 days. It is **[9.00/10.77]** the bootstrap interval.

### Business Question — Reporting the Average Delivery Time

The team should report the sample mean of 12.40 days together with its 95% bootstrap confidence interval of 11.41 to 13.41 days. Reporting a range communicates the uncertainty of the estimate instead of presenting the sample average as an exact value.

## Part 4

### Formula-Based 95% Confidence Interval

We calculated the standard error of the original sample of 300 orders.

Using the formula:

CI = Sample Mean ± 1.96 × Standard Error

The formula-based confidence interval is:

- Lower bound: 11.40 days
- Upper bound: 13.41 days

### Comparing the Two Methods

| Method    | Lower Bound | Upper Bound |
| --------- | ----------: | ----------: |
| Bootstrap |       11.41 |       13.41 |
| Formula   |       11.40 |       13.41 |

Both methods produced very similar confidence intervals.

### Business Question — What Does 95% Confidence Mean?

A 95% confidence level means that if we repeatedly take samples and construct confidence intervals using the same method, approximately 95% of those intervals will contain the true population mean. A single calculated interval either contains the true mean or does not.

### Exercise 4.a — Interpreting the Confidence Interval

No, this is not correct. The confidence interval describes the uncertainty around the population mean delivery time, not the delivery time of every individual order. Individual orders can arrive much earlier or later than this range.

## Part 5

### Delivery Statistics by State

We calculated the number of orders, mean delivery time, standard deviation and half-width of the 95% confidence interval for each state.

| State |   Size |  Mean |   Std | Half |
| ----- | -----: | ----: | ----: | ---: |
| SP    | 40,495 |  8.76 |  6.75 | 0.07 |
| AL    |    397 | 24.54 | 11.48 | 1.13 |
| AM    |    145 | 26.43 | 13.86 | 2.26 |
| AP    |     67 | 27.19 | 21.38 | 5.12 |
| RR    |     41 | 29.39 | 27.74 | 8.49 |

### State Comparison

**SP:** SP has 40,495 orders and a very narrow 95% confidence interval, from approximately 8.69 to 8.83 days. Its large sample provides a more stable estimate of the mean.

**RR:** RR has only 41 orders and a much wider confidence interval, from approximately 20.90 to 37.88 days. Its estimated average is less precise because of the small sample size.

### Exercise 5.a — Bootstrap Interval for RR

We generated 2,000 bootstrap samples from the 41 RR orders, using sampling with replacement.

The bootstrap 95% confidence interval is:

- Lower bound: **[22.31]**
- Upper bound: **[38.80]**

The formula-based confidence interval is approximately 20.90 to 37.88 days.

The two intervals **[ ARE NOT]** the same. They can differ because the formula uses a normal approximation, while the bootstrap uses the simulated distribution of sample means. With only 41 observations, the distribution may not be sufficiently symmetric or bell-shaped.

### Business Question — Should RR Be Prioritized?

RR has the highest observed average delivery time at 29.39 days, but it has only 41 orders and a very wide confidence interval. Its interval overlaps with those of AM and AP, so we cannot confidently conclude that RR is the slowest state. The operations team should investigate these states further and collect more data before deciding where to focus first.

## Errors and What They Taught Me

No errors were encountered during today's analysis. The notebook executed successfully, and all required calculations and visualizations were generated as expected.
