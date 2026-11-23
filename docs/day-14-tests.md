## Part 0

### Observed Difference and Shuffling Experiment

RR had 41 orders, while AM had 145 orders. The average delivery time in RR was **2.96 days longer** than in AM.

To test whether this difference could happen by chance, I combined the orders from both states and randomly shuffled them 5,000 times. Each shuffled dataset was divided into groups of 41 and 145 orders, and the difference between their average delivery times was calculated.

The estimated p-value from the 5,000 shuffles was **0.3742**. This means that about 37.42% of the shuffled experiments produced a difference at least as large as the observed gap, in either direction.

### The Coin Example

A fair coin can produce seven heads in ten flips simply because of random variation. Getting this result does not prove that the coin is unfair. Similarly, observing a delivery-time difference between RR and AM does not automatically prove that their delivery performance is different.

### Exercise 0.a — 20,000 Shuffles

After increasing the number of shuffles from 5,000 to 20,000, the estimated p-value was **[0.3615]**, compared with **0.3742** from the original experiment.

The p-value **[changed only slightly]**. This comparison shows how increasing the number of simulations can help assess the stability of the estimate.

### Business Question

Based on the shuffling experiment, there is not enough evidence to conclude that RR's longer average delivery time is a real difference rather than random variation. I would not recommend changing RR's carrier based on this result alone; we should investigate further before making an operational decision.

## Part 1

### Understanding the p-value

The p-value from the RR versus AM comparison was **0.37**. This means that if both states delivered in the same way, a difference as large as the observed gap could occur in about 37 out of 100 random comparisons.

The result is not statistically significant because the p-value is greater than 0.05. Therefore, the current data does not provide enough evidence to conclude that RR and AM have different delivery performance.

### Five Things a p-value Is Not

1. **It is not the probability that the result is caused by luck.** It measures how often a result this extreme could occur if there were no real difference.
2. **It is not the size of the difference.** The p-value does not tell us whether the difference is large or small.
3. **A large p-value does not prove that no difference exists.** It only means that the available data does not provide enough evidence to detect one.
4. **0.05 is not a magic boundary.** Values such as 0.049 and 0.051 are very close and should not be interpreted as completely different results.
5. **It does not predict the probability of getting the same result again.** New data may produce a different result and a different p-value.

### Exercise 1.a

- **Sentence 1 is wrong.** A p-value of 0.37 does not mean there is a 37% chance that the gap is caused by luck. It means that, assuming no real difference, a gap this large or larger could occur in about 37 out of 100 random comparisons.
- **Sentence 2 is wrong.** A p-value of 0.37 does not prove that RR and AM deliver equally fast. It only means that the current data does not provide enough evidence of a difference.
- **Sentence 3 is correct.** It describes the p-value correctly by explaining how often a gap this large could occur if the two states were actually the same.

### Business Question

If RR and AM were truly alike, a difference this large could still appear in about 37 out of 100 comparisons just by chance. Therefore, I would not conclude that RR is genuinely slower based on this result alone.

## Part 2

### The t-test: RR versus AM

The Welch's t-test returned a p-value of **0.51**. This is greater than 0.05, so there is not enough statistical evidence to conclude that the average delivery times of RR and AM are different.

### The Mann-Whitney Test: RR versus AM

The Mann-Whitney test returned a p-value of **0.49**. The median delivery time was **25.01 days** for RR and **25.88 days** for AM.

This test also found no sufficient evidence that RR orders usually take longer than AM orders.

### Why Is RR's Average Higher?

RR's average is higher because a few extremely late orders pull the mean upward. Its three slowest orders took **172.1, 73.9, and 71.2 days**. This explains why RR has a higher mean even though its median is slightly lower than AM's.

### Compare SP and MG

The Welch's t-test returned an extremely small p-value, displayed as `0.0` by Python. It should be reported as **p < 0.0001**. SP's average delivery time was **8.76 days**, compared with **12.01 days** for MG.

### Exercise 2.a — AL versus AM

The Welch's t-test p-value was **[0.1452]**, while the Mann-Whitney p-value was **[0.0301]**.

The average delivery time was **[24.54]** days for AL and **[26.43]** days for AM. The median was **[22.33]** days for AL and **[25.88]** days for AM.

### Business Question

The RR versus AM comparison does not provide enough evidence that RR customers usually wait longer. A few extremely late RR orders raise its average, so I would investigate those orders before recommending a carrier change.

## Part 3 — Two Percentages: The Chi-square Test

### AL vs MA

- AL late-order rate: 21.4% (85 out of 397 orders).
- MA late-order rate: 17.4% (125 out of 717 orders).
- Chi-square p-value: 0.12.

The difference between AL and MA is not statistically significant because the p-value is above 0.05. We do not have enough evidence to conclude that AL is genuinely worse than MA.

### Expected Counts

AL and MA have 1,114 orders combined, with 210 late orders. If both states had the same late-order rate, the expected rate would be about 18.9%. We would expect approximately 75 late orders in AL and 135 in MA, compared with the actual counts of 85 and 125.

### Exercise 3.a — RJ vs SP

- RJ late-order count:
- RJ late-order rate:
- SP late-order count:
- SP late-order rate:
- Chi-square p-value:
- Is the difference statistically significant?

**RJ vs AL operational comparison:**

- RJ late orders:
- AL late orders: 85.
- State to fix first:
- Reason:

### Business Answer

The observed late-order rate is higher in AL than in MA, but the difference is not statistically significant. We should not conclude that AL is genuinely worse based on these percentages alone.

## Part 4 — Significant Is Not the Same as Big

### Tuesday vs Wednesday

- Average delivery-time gap: 0.37 days.
- P-value: 0.0011.
- Effect size: approximately 9 hours.
- Percentage difference: approximately 3%.

The difference is statistically significant, but its practical size is relatively small. Tuesday and Wednesday each have around 15,000 orders, allowing the test to detect a small difference.

### Exercise 4.a — Monday vs Friday

- Average delivery-time gap: [1.57] days.
- P-value: [0.0].
- Difference in hours: [38].
- Percentage difference: [13]%.

### Business Answer

Wednesday orders arrive about 9 hours later than Tuesday orders on average. Although the difference is statistically significant, it represents only about 3% of the average delivery time, so the business should consider its practical impact before changing promised delivery dates.

## Part 5 — The p-hacking experiment

### Step 1 — Twenty random comparisons

I randomly divided the orders into two groups and performed a Welch's t-test 20 times.

- Significant results (p < 0.05): 1
- Smallest p-value: 0.0473

Although the groups were created randomly, one test produced a significant result by chance.

### Step 2 — One thousand random comparisons

I repeated the experiment 1,000 times.

- Results below 0.05: 49
- Results below 0.0025: 4

Approximately 5% of random tests produced a significant result using the 0.05 threshold. Applying the Bonferroni correction reduced the number of results passing the stricter threshold.

### What is p-hacking?

P-hacking is trying many statistical comparisons and reporting only the one that produces a significant result, without accounting for the number of tests performed.

### Exercise 5.a — Seed 31

- Significant results (p < 0.05): [3]
- Smallest p-value: [0.012]

Changing the random seed produces a different sequence of random groups, so the number of significant results can change. This is expected and not surprising.

### Business answer

We should not change the promised delivery date based on one significant result found after examining 20 different comparisons. We should account for multiple comparisons and confirm the finding with a properly planned test or new data.

## Part 6 — Power: how many orders does a test need?

### Step 1 — Power at different sample sizes

I tested different sample sizes using 1,000 repeated samples from SP and MG.

| Orders per group | Power |
| ---------------: | ----: |
|               10 | 19.1% |
|               30 | 53.1% |
|              100 | 91.3% |

The results show that larger samples increase the probability of detecting a real difference.

### Step 2 — Power chart

I plotted power against the number of orders in each group. The chart shows that power increases as the sample size grows.

The figure is saved as `day-14-power.png`.

### Why does Part 0's big p-value say little?

RR had only 41 orders, and their delivery times varied widely. A small sample may not have enough statistical power to detect a real difference, so a big p-value does not prove that there is no difference.

### Exercise 6.a — Finding 80% power

- Closest sample size: [65] orders per group.
- Estimated power: [0.81].

I tested sample sizes between 50 and 100 to find the value closest to 80% power.

### Business answer

To test a new carrier against the old one, Olist should use a sufficiently large sample in each group. The experiment suggests that larger samples make it much more likely to detect a real delivery-time difference of about three days.

## Errors and Lessons Learned

No execution errors occurred during this day's analysis. However, I learned several important lessons:

- A large p-value does not prove that two groups are equal.
- Statistical significance does not necessarily mean that a difference is practically important.
- A small sample size can make a test miss a real difference.
- Running many tests increases the chance of finding a significant result by chance.
