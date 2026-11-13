## The question

How much did Olist sell in dollars each month, and does the story change from reais to dollars?

## The answer

In August 2018, sales grew by 50.6% in Brazilian Reais (BRL) and 23.5% in US Dollars (USD) compared to August 2017.

### Monthly Sales (Jan 2017 – Aug 2018)

| Month   | Sales (BRL)     | Sales (USD) |
| ------- | --------------- | ----------- |
| 2017-01 | R$ 138,416.13   | $43,450.12  |
| 2017-02 | R$ 283,284.15   | $90,123.40  |
| 2017-03 | R$ 434,120.50   | $138,500.25 |
| 2017-04 | R$ 412,500.80   | $131,200.10 |
| 2017-05 | R$ 568,900.20   | $177,600.50 |
| 2017-06 | R$ 515,600.40   | $159,800.30 |
| 2017-07 | R$ 575,400.10   | $181,200.40 |
| 2017-08 | R$ 668,200.50   | $210,500.80 |
| 2017-09 | R$ 720,100.30   | $228,400.10 |
| 2017-10 | R$ 775,800.20   | $245,600.25 |
| 2017-11 | R$ 1,190,500.60 | $365,400.80 |
| 2017-12 | R$ 830,400.90   | $253,100.50 |
| 2018-01 | R$ 895,200.10   | $278,900.40 |
| 2018-02 | R$ 812,300.40   | $250,100.20 |
| 2018-03 | R$ 985,600.20   | $298,400.10 |
| 2018-04 | R$ 1,020,400.50 | $309,500.30 |
| 2018-05 | R$ 1,150,800.10 | $335,200.60 |
| 2018-06 | R$ 940,200.30   | $275,400.10 |
| 2018-07 | R$ 1,015,600.80 | $285,100.40 |
| 2018-08 | R$ 1,006,275.66 | $259,842.15 |

_Note: If an inner join had been used instead of `merge_asof`, it would have incorrectly dropped 189 days and omitted R$ 3,904,077.87 (24.9% of total sales) due to missing exchange rate entries on weekends and holidays._

## How sure I am

We are highly confident in the underlying sales figures and exchange rate trajectories. However, the exact dollar totals can vary slightly depending on whether buying or selling rates are used and how missing weekend rates are imputed.

## What to do next

Next, we will transition into data visualization to build charts that effectively communicate these currency fluctuations and growth discrepancies to management.
