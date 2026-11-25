## Part 0 — One row for each order

### Step 1 — Joining orders and reviews

I joined the orders table with the order_reviews table using order_id and kept only delivered orders.

- Total rows after join: 96,359
- Unique orders: 95,830

The join produced more rows than unique orders because some orders have multiple reviews. This shows that the number of rows is not always equal to the number of unique orders after a JOIN.

### Step 2 — Building one row per order

I created two CTEs:

- The `latest` CTE uses ROW_NUMBER() to identify the latest review for each order.
- The `items` CTE calculates the number of items and total freight for each order.

I then joined these results with the orders and customers tables, keeping only the latest review (`n = 1`) and delivered orders.

- Final rows: 95,830
- Unique orders: 95,830

The final dataset contains exactly one row per order.

### Step 3 — Delivery time and late orders

I calculated delivery duration in days by subtracting the purchase timestamp from the delivery timestamp.

I also created a boolean column called `late` to identify orders delivered after their estimated delivery date.

| Late status              | Number of orders | Average score |
| ------------------------ | ---------------: | ------------: |
| On time or early (False) |           89,448 |          4.29 |
| Late (True)              |            6,382 |          2.27 |

Late orders have a much lower average review score than orders delivered on time or earlier.

### Exercise 0.a — Multiple reviews

I counted orders with more than one review using groupby(), size(), and a condition checking whether the number of reviews was greater than one.

- Orders with more than one review: [525]

I then merged the `late` column from the one-row-per-order dataset into the original joined dataset.

| Late status              | Number of review rows | Average score |
| ------------------------ | --------------------: | ------------: |
| On time or early (False) |                89,949 |          4.29 |
| Late (True)              |                 6,410 |          2.27 |

The average scores remained the same after rounding to two decimal places. However, the number of rows increased because orders with multiple reviews appear more than once in the joined dataset. These orders receive more weight when calculating the average.

### Business question — Do late deliveries really cost stars?

Late deliveries are strongly associated with lower customer ratings. Late orders have an average score of 2.27, compared with 4.29 for orders delivered on time or earlier. However, this comparison shows an association and does not prove that delivery delays are the only cause of low ratings.

## Part 1 — Correlation: What moves with the stars?

### Step 1 — Understanding correlation

I created a small example dataset with delivery days and customer ratings. I used the corr() method to calculate the correlation between the two columns.

The result was -0.95, indicating a strong negative linear relationship: as delivery days increase, customer ratings tend to decrease.

### Step 2 — Correlation with customer ratings

I calculated the correlation between customer ratings and four order-related variables.

| Variable | Correlation with score |
| -------- | ---------------------: |
| score    |                   1.00 |
| days     |                  -0.33 |
| late     |                  -0.39 |
| items    |                  -0.12 |
| freight  |                  -0.09 |

Late deliveries had the strongest negative correlation with review scores (-0.39), followed by delivery days (-0.33). The number of items (-0.12) and freight cost (-0.09) had much weaker negative correlations.

These results show associations, not necessarily causal relationships.

### Step 3 — Interpreting correlations

Late deliveries have the strongest negative correlation with customer ratings among the four variables. However, correlation does not imply causation.

Other factors, such as delivery distance or location, may influence both delivery delays and customer satisfaction. Therefore, we should investigate these relationships further before making business decisions.

### Step 4 — Anscombe's quartet

I loaded Anscombe's quartet dataset and calculated the correlation between x and y for each dataset.

| Dataset | Correlation |
| ------- | ----------: |
| I       |        0.82 |
| II      |        0.82 |
| III     |        0.82 |
| IV      |        0.82 |

All four datasets have approximately the same correlation, despite having very different distributions and patterns.

This demonstrates that correlation alone does not describe the full relationship between two variables. Visualizing data is important to identify nonlinear patterns and outliers.

### Exercise 1.a — Number of items and customer ratings

I calculated the average review score for orders containing one, two, three, and four items.

| Number of items | Orders | Average score |
| --------------- | -----: | ------------: |
| 1               | 86,301 |          4.21 |
| 2               |  7,320 |          3.69 |
| 3               |  1,286 |          3.53 |
| 4               |    487 |          3.38 |

The average review score decreases as the number of items increases.

To investigate possible explanations, I compared delivery days, late delivery rates, and average freight costs across these groups.

| Number of items | Orders | Average score | Average days | Late rate | Average freight |
| --------------- | -----: | ------------: | -----------: | --------: | --------------: |
| 1               | 86,301 |          4.21 |        12.60 |      0.07 |           20.32 |
| 2               |  7,320 |          3.69 |        11.78 |      0.05 |           37.06 |
| 3               |  1,286 |          3.53 |        11.58 |      0.05 |           54.84 |
| 4               |    487 |          3.38 |        12.12 |      0.04 |           74.17 |

The results do not support the hypothesis that larger orders receive lower ratings because they take longer to deliver or experience more delays. Average delivery days and late rates do not increase with the number of items.

Freight costs increase with the number of items, but this comparison alone does not prove that higher freight costs cause lower ratings.

### Business question — Which factor should the customer team focus on?

Among the four variables, late deliveries have the strongest negative correlation with customer ratings (-0.39), followed by delivery days (-0.33).

Therefore, delivery delays are the most important factor to investigate first. However, correlation does not prove causation, so we need further analysis before deciding what actions will improve customer satisfaction.

## Part 2 — Regression line: What one day costs

### Step 1 — Building a toy regression model

I fitted a simple Ordinary Least Squares (OLS) regression model using the toy dataset.

The model produced an intercept of 5.50 and a days coefficient of -0.12. This means that each additional delivery day is associated with a decrease of 0.12 stars in the predicted rating.

The regression equation is:

score = 5.50 - (0.12 × days)

### Step 2 — Regression with real data

I fitted an OLS regression model using the real orders dataset, with customer review scores as the dependent variable and delivery days as the predictor.

The model produced an intercept of 4.724 and a days coefficient of -0.045.

This means that each additional delivery day is associated with a decrease of 0.045 stars in the predicted review score.

The regression equation is:

score = 4.724 - (0.045 × days)

### Step 3 — Confidence intervals

I calculated the 95% confidence intervals for the regression coefficients using conf_int().

| Coefficient | Lower bound | Upper bound |
| ----------- | ----------: | ----------: |
| Intercept   |       4.711 |       4.736 |
| days        |      -0.046 |      -0.045 |

The confidence interval for the days coefficient does not include zero, providing statistical evidence of a negative relationship between delivery days and review scores. The narrow interval also indicates that the estimated coefficient is relatively precise.

### Step 4 — P-values

I examined the p-values of the regression coefficients.

The p-value for delivery days is extremely small (p < 0.0001), providing strong statistical evidence of a negative relationship between delivery time and review scores.

Python may display very small values as 0.0 due to numerical formatting, but this does not mean the actual p-value is exactly zero.

Statistical significance does not prove causation.

### Step 5 — R-squared

I calculated the R-squared value of the regression model.

The result was 0.11, meaning that delivery days explain approximately 11% of the variation in customer review scores.

The remaining 89% is not explained by delivery days alone and may be related to other factors, such as product quality, packaging, customer service, and other aspects of the customer experience.

For a simple linear regression with one predictor and an intercept, R-squared equals the squared correlation coefficient. This is consistent with the correlation of approximately -0.33 calculated in Part 1.

### Step 6 — Visualizing the regression line

I grouped orders by rounded delivery days and calculated the average review score for each day. I then plotted these averages as points and added the fitted regression line in red.

The visualization shows that the relationship is not perfectly linear: ratings decrease slowly at first and then fall more quickly after approximately three weeks.

This demonstrates that a simple linear regression line is only a rough summary of the relationship.

The chart was saved as figures/day-15-line.png.

### Exercise 2.a — Comparing predicted and actual ratings

I used the regression equation to predict review scores for orders delivered in 10 and 40 days. I compared these predictions with the actual average scores.

| Delivery days | Predicted score | Actual score |
| ------------- | --------------: | -----------: |
| 10            |            4.27 |         4.31 |
| 40            |            2.91 |         2.13 |

At 10 days, the prediction was very close to the actual average score, with a difference of only 0.04 stars.

At 40 days, the model predicted 2.91 stars, while the actual average was 2.13 stars. The difference was 0.78 stars.

This shows that the linear regression model represents the relationship reasonably well around 10 days but performs poorly at 40 days. The actual ratings fall faster than the straight regression line predicts.

### Business question — How much does each extra delivery day cost?

The regression coefficient suggests that each additional delivery day is associated with a decrease of approximately 0.045 stars in the predicted customer rating.

However, delivery days explain only 11% of the variation in review scores, and the relationship is not perfectly linear. Therefore, delivery time is an important factor to investigate, but it is not the only factor affecting customer satisfaction.

## Part 3 — Hold one thing fixed: Confounders

### Step 1 — Calculating promised delivery days

I created a new column called `promised` by calculating the number of days between the purchase date and the estimated delivery date.

I then fitted a simple OLS regression model to examine the relationship between promised delivery days and customer review scores.

The promised coefficient was -0.0077, suggesting that each additional promised day was associated with a very small decrease in the predicted review score. However, this was only an initial relationship and did not establish causation.

### Step 2 — Comparing orders with similar actual delivery times

I selected orders that took approximately 20 days to arrive and grouped them by promised delivery time.

| Promised delivery time | Orders | Average score |
| ---------------------- | -----: | ------------: |
| [0, 20)                |    100 |          3.02 |
| [20, 30)               |    931 |          4.14 |
| [30, 200)              |    733 |          4.15 |

Orders promised in less than 20 days had an average review score of 3.02, while orders promised between 20 and 30 days had an average score of 4.14. Orders promised between 30 and 200 days had an average score of 4.15.

This suggests that among orders with similar actual delivery times, customers gave higher ratings when the promised delivery time was longer. Orders that arrived later than promised may receive lower ratings because they did not meet customer expectations.

### Step 3 — Interpreting the relationship

The initial regression showed a small negative relationship between promised delivery days and review scores. However, when I compared orders with similar actual delivery times, the pattern changed.

Orders with longer promised delivery times received higher average ratings. This suggests that customer satisfaction may depend not only on how long delivery takes, but also on whether the order arrives within the promised time.

Setting realistic delivery expectations may be more important than simply promising faster delivery.

### Step 4 — Including promised and actual delivery days

I fitted a multiple regression model using both promised delivery days and actual delivery days as predictors of review scores.

The promised coefficient changed from -0.0077 in the simple model to +0.0131 in the multiple regression model.

Holding actual delivery days fixed, each additional promised day was associated with an increase of 0.0131 stars.

The actual delivery days coefficient was -0.0501. Holding promised delivery days fixed, each additional actual delivery day was associated with a decrease of 0.0501 stars.

This demonstrates how including an important variable can change the interpretation of a relationship.

### Step 5 — Understanding the confounder

A confounder is a variable that can affect the relationship between two other variables.

In this example, distance could be a potential confounder because distant orders may take longer to deliver and may receive longer estimated delivery times.

The multiple regression model showed that the promised coefficient changed from negative to positive after including actual delivery days. This demonstrates how controlling for another variable can change the relationship we observe.

Distance is only a possible unobserved confounder in this analysis because it is not directly included in our dataset.

### Exercise 3.a — Including late status in the regression

I fitted a multiple regression model using actual delivery days and late delivery status to explain customer review scores.

The coefficient for `days` was -0.0209, meaning that each additional actual delivery day was associated with a decrease of 0.0209 stars, holding late status constant.

The coefficient for `late[T.True]` was -1.5411, meaning that late orders were associated with 1.5411 fewer stars than orders that were not late, holding actual delivery days constant.

This suggests that arriving later than the estimated delivery date has a strong negative association with customer satisfaction.

### Part 3 — Business takeaway

Customer satisfaction depends not only on actual delivery time but also on whether the order arrives within the promised delivery date. Setting realistic delivery expectations and meeting those expectations may be more important than simply promising the fastest delivery.

## Part 4 — Simpson's Paradox

### Step 1 — Comparing Northeast and Southeast

I selected orders from the Northeast and Southeast regions and created a new column called `region` to identify each order's region.

I then calculated the average review score for each region.

| Region    | Average score |
| --------- | ------------: |
| Northeast |          3.97 |
| Southeast |          4.18 |

At first, this suggests that customers in the Southeast gave higher ratings. However, this overall comparison does not account for differences in delivery times between the two regions.

### Step 2 — Comparing regions within delivery-time groups

I divided orders into five groups based on their actual delivery times and calculated the average review score for each region within each group.

| Delivery time | Northeast | Southeast |
| ------------- | --------: | --------: |
| [0, 7)        |      4.44 |      4.41 |
| [7, 14)       |      4.34 |      4.29 |
| [14, 21)      |      4.23 |      4.06 |
| [21, 30)      |      3.94 |      3.26 |
| [30, 300)     |      2.45 |      1.97 |

The Northeast had a higher average score than the Southeast in all five delivery-time groups, even though its overall average score was lower.

This reveals that the overall comparison can be misleading. We need to examine how orders are distributed across delivery-time groups to understand why the regional averages differ.

### Step 3 — Comparing the distribution of delivery times

I used a cross-tabulation with column normalization to compare the distribution of delivery times in each region.

| Delivery time | Northeast | Southeast |
| ------------- | --------: | --------: |
| [0, 7)        |      0.03 |      0.36 |
| [7, 14)       |      0.29 |      0.42 |
| [14, 21)      |      0.33 |      0.14 |
| [21, 30)      |      0.21 |      0.05 |
| [30, 300)     |      0.13 |      0.03 |

Only 32% of Northeast orders were delivered in less than 14 days, compared with 78% of Southeast orders. In addition, 34% of Northeast orders took 21 days or more, compared with only 8% of Southeast orders.

This explains why the Northeast had a lower overall average score. It had a much larger share of slow deliveries, which generally received lower ratings.

The difference in overall regional averages is therefore strongly influenced by the distribution of delivery times, rather than showing that Northeast customers are harder to satisfy.

### Step 4 — Visualizing the regional comparison

I created a grouped bar chart to compare the average review scores of the Northeast and Southeast across delivery-time groups.

The chart shows that the Northeast had an equal or higher average score in every delivery-time group. However, its overall average was lower because a larger proportion of its orders took longer to deliver.

I saved the chart as `day-15-regions.png` for use in the final report.

### Exercise 4.a — Comparing North with Southeast

I compared the average review scores of the North and Southeast regions within the same delivery-time groups.

| Delivery time | North | Southeast | North orders |
| ------------- | ----: | --------: | -----------: |
| [0, 7)        |  4.22 |      4.41 |           23 |
| [7, 14)       |  4.42 |      4.29 |          360 |
| [14, 21)      |  4.30 |      4.06 |          569 |
| [21, 30)      |  4.05 |      3.26 |          488 |
| [30, 300)     |  3.13 |      1.97 |          339 |

The North had a higher average score in four out of five groups. The Southeast had a higher score only in the shortest delivery-time group, where the North had just 23 orders.

The number of North orders varied across groups, ranging from 23 to 569 orders. This is important because averages based on small groups may be less reliable.

The results show that the regional comparison does not reverse in every delivery-time group. Therefore, the pattern observed in the Northeast comparison does not apply identically to every regional comparison.

### Part 4 — Business takeaway

The overall difference in regional ratings can be misleading when regions have different delivery-time distributions. Olist should compare customer ratings within similar delivery-time groups before concluding that customers in one region are less satisfied than customers in another region.

## Part 5 — Regression to the Mean

### Step 1 — Prepare seller review data

I joined the order items, order reviews, and orders tables to create a dataset containing seller reviews from 2017.

I grouped the data by seller and review ID to avoid duplicate rows and used `MIN(review_score)` to keep one review score for each seller-review combination.

I also divided the year into two periods:

- `first`: January through June 2017.
- `second`: July through December 2017.

The resulting dataset contained **44,903 rows**.

### Step 2 — Keep sellers with enough reviews

I created two pivot tables:

- `stars`: the average review score for each seller in each half of the year.
- `counts`: the number of reviews for each seller in each half.

I kept only sellers with at least 20 reviews in both periods to make the comparison more reliable.

The final dataset contained **143 sellers**.

### Step 3 — Pick worst and best sellers

I selected the 20 sellers with the lowest average score in the first half of 2017 and the 20 sellers with the highest average score.

The results were:

| Period | Worst 20 | Best 20 |  All |
| ------ | -------: | ------: | ---: |
| First  |     3.71 |    4.57 | 4.18 |
| Second |     3.93 |    4.27 | 4.15 |

The worst 20 sellers improved by 0.22 points, while the best 20 sellers declined by 0.30 points. The overall average remained almost unchanged.

### Step 4 — Interpret the results

Both extreme groups moved closer to the overall average. This is consistent with regression to the mean: unusually low or high results tend to become less extreme when measured again.

We cannot conclude that the fictional warning letter caused the improvement. Natural variation and regression to the mean may explain part of the observed change.

### Step 5 — Why regression to the mean happens

An observed score consists of real performance and random variation.

When sellers are selected because of unusually low or high scores, their results may partly reflect temporary factors. When measured again, those temporary factors may not repeat, causing their average scores to move closer to the overall average.

This does not necessarily mean that their actual performance changed.

### Exercise 5.a — Using a minimum of 10 reviews

I repeated the analysis using sellers with at least 10 reviews in each half instead of 20.

The results were:

| Period | Worst 20 | Best 20 |  All |
| ------ | -------: | ------: | ---: |
| First  |     3.42 |    4.68 | 4.15 |
| Second |     3.97 |    4.25 | 4.12 |

The worst 20 sellers improved by 0.55 points, while the best 20 sellers declined by 0.43 points.

Compared with the 20-review requirement, both extreme groups moved further toward the overall average.

Sellers with fewer reviews may have averages that are more affected by random variation, making regression to the mean more noticeable. However, changing the minimum review requirement also changes the eligible seller groups, so we cannot attribute the entire difference to review count alone.

### Part 5 — Key takeaway

Regression to the mean explains why unusually high or low results often become less extreme when measured again. It is important not to confuse this natural statistical pattern with the effect of a business intervention.
