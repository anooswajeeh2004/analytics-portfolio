# Day 16 — A/B Testing from Start to Finish

## Part 0 — The plan, before the data

### Test Plan

The goal is to compare the new landing page with the old page using an A/B test.

- **Primary metric:** Conversion rate, which measures the percentage of users who make a purchase.
- **Guardrail metrics:** Page loading time and customer return rate. These metrics should not get worse during the test.
- **Baseline conversion rate:** 12%.
- **Target:** An improvement of 0.5 percentage points, from 12% to 12.5%.
- **MDE:** 0.5 percentage points.
- **Sample size:** 67,584 users in each group.
- **Test duration:** Two full weeks.
- **Randomization unit:** User. Each user should remain in the same group and see the same page on every visit.

### Sample Size and Test Duration

Used the Rule of 16 to calculate the required sample size for each group. The calculation showed that 67,584 users are needed to detect an improvement of 0.5 percentage points.

With approximately 6,400 users per group each day, the required sample size takes 10.6 days. The test should run for two full weeks to include all days of the week equally.

### Understanding the Target

The difference between 12% and 12.5% is 0.5 percentage points. Compared with the original 12% conversion rate, this represents an increase of approximately 4.17%.

### Sample Size Visualization

Created a line chart to show how the required sample size changes with the minimum detectable effect. Smaller improvements require more users. Reducing the MDE by half requires four times as many users.

### Exercise 0.a

For an MDE of 0.3 percentage points, approximately 18,773 users are needed in each group. At 6,400 users per group per day, this takes about 2.9 days, so the test should run for one full week.

### Business Answer

The test should measure the conversion rate while monitoring page loading time and customer return rate. It needs 67,584 users in each group and should run for two full weeks to detect the target improvement of 0.5 percentage points.

## Part 1 — The test's data

### Loading and Inspecting the Data

Loaded the A/B testing dataset from `ab_data.csv` using Pandas. Converted the `timestamp` column to datetime format and inspected the first three rows to understand the dataset structure.

The dataset contains **294,478 rows and 5 columns**.

### Test Duration

Used `min` and `max` to identify the earliest and latest timestamps.

- **Start date:** January 2, 2017
- **End date:** January 24, 2017
- **Duration:** 22 days (3 full weeks and 1 additional day)

The test ran longer than the planned two full weeks.

### Group Sizes

Used `value_counts()` to count the records in each group.

| Group     | Number of rows |
| --------- | -------------: |
| Control   |        147,202 |
| Treatment |        147,276 |

Both groups exceeded the planned sample size of 67,584 users per group.

### Overall Conversion Rate

Calculated the overall conversion rate using the mean of the `converted` column. The result was approximately **11.97%**, which was close to the planned baseline of 12%.

### Exercise 1.a

The overall conversion rate was approximately 11.97%. Therefore, the planned baseline of 12% was a good estimate.

### Business Answer

The test ran for 22 days, exceeding the planned two weeks. Both groups had more than the required number of users, so the test met the planned duration and sample size requirements.

## Part 2 — The result

### Conversion Rates by Group

Grouped the users by their test group and calculated the number of records, total conversions, and conversion rate.

| Group     |   Users | Buyers | Conversion Rate |
| --------- | ------: | -----: | --------------: |
| Control   | 147,202 | 17,723 |          12.04% |
| Treatment | 147,276 | 17,514 |          11.89% |

The treatment group had a slightly lower conversion rate than the control group.

### Regression Analysis

Fitted an OLS regression model using `converted` as the outcome and `group` as the explanatory variable.

- **Intercept:** 0.12040, representing the control group's conversion rate.
- **Treatment coefficient:** -0.00148, representing the difference between the treatment and control groups.

The estimated gap was approximately -0.15 percentage points.

### Confidence Interval

Calculated the 95% confidence interval for the treatment effect:

- **Lower bound:** -0.00382
- **Upper bound:** 0.00086

The interval includes zero, meaning that the results do not rule out the possibility of no real difference between the two pages.

### P-value

The treatment effect had a P-value of 0.22, which is higher than the 0.05 significance level. Therefore, the test does not provide sufficient statistical evidence of a difference between the two pages.

### Exercise 2.a

We cannot conclude that the new page is worse. Although its conversion rate was slightly lower, the confidence interval includes zero and the P-value is higher than 0.05.

### Business Answer

The test does not show that the new landing page increases sales. Its conversion rate was slightly lower, but the difference was not statistically significant. We cannot conclude that the new page performs better or worse based on this test alone.

## Part 3 — The gap in business terms

### 1. Gap and Confidence Interval

I converted the regression coefficient and its 95% confidence interval into percentage points.

- Estimated gap: -0.15 points.
- Lower bound: -0.38 points.
- Upper bound: +0.09 points.

### 2. Buyer Impact

For every 100,000 users:

- Estimated result: 148 fewer buyers.
- Lower bound: 382 fewer buyers.
- Upper bound: 86 additional buyers.
- Business target: 500 additional buyers.

Even the best end of the confidence interval is far below the business target.

### 3. Decision Chart

I created an error-bar chart showing the estimated gap, its confidence interval, the no-change reference line, and the business target of +0.5 percentage points.

The entire confidence interval is below the target. This means the new page does not show a potential improvement large enough to justify its cost.

### 4. Exercise 3.a — Profit Impact

Assuming each buyer generates $10 in profit:

- Best case: approximately $860 in additional profit per 100,000 users.
- Worst case: approximately $3,820 less profit per 100,000 users.
- Estimated result: approximately $1,480 less profit per 100,000 users.

### 5. Business Answer

The new landing page does not meet the business target. Even its best estimated outcome is only 86 additional buyers per 100,000 users, compared with the target of 500. Therefore, the results do not support switching to the new page.

## Part 4 — Was the test big enough?

### 1. MDE Results

I calculated the Minimum Detectable Effect (MDE) for four different sample sizes using the Rule of 16.

| Test size                            | MDE (percentage points) |
| ------------------------------------ | ----------------------: |
| A small test (10,000 users)          |                    1.30 |
| Original plan (67,584 users)         |                    0.50 |
| Current test (147,202 users)         |                    0.34 |
| After two more weeks (236,802 users) |                    0.27 |

A larger sample size allows the test to detect smaller effects.

### 2. Was the Test Big Enough?

Yes. The current MDE was 0.34 points, which is smaller than the business target of 0.5 points.

The upper bound of the confidence interval was also only +0.09 points, which is below the target.

### 3. Exercise 4.a

For an MDE of 0.15 percentage points:

- Required users per group: approximately 750,934.
- Required testing time: approximately 118 days, with 6,400 users arriving in each group per day.

### 4. Business Answer

The current test was large enough to evaluate the business target. Adding two more weeks would reduce the MDE from 0.34 to 0.27 points, but it is not necessary based on the current results because even the upper end of the confidence interval is far below the target.

## Part 5 — The Decision

In this part, I used the A/B test results to make a business decision based on the estimated conversion difference, confidence interval, and business target.

The decision rules were:

1. Switch to the new page if the confidence interval is entirely above zero and the estimated improvement reaches the business target, provided that no guardrail metric worsens.
2. Keep the old page if the entire confidence interval is below the business target.
3. Plan a bigger test if the results are not conclusive.

**Exercise 5.a:**

I applied these rules to three hypothetical tests:

- Test 1: Switch to the new page.
- Test 2: Plan a bigger test.
- Test 3: Keep the old page.

**Business Decision:**

The shop should keep the old landing page because the estimated improvement did not reach the target of 0.5 percentage points. The upper confidence limit was only +0.09 points, which is below the required target.
