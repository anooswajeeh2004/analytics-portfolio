## Part 0 — The Same Numbers, Two Charts

The average freight cost in RR is R$ 42.98, while in PI it is R$ 39.15. This means RR pays R$ 3.83 more per item, which is approximately 9.8% higher than PI.

However, in the first chart, RR's bar looks about 27 times taller than PI's bar because the Y-axis starts at 39 instead of 0.

**How could the left chart fool a manager?**

The left chart could make a manager believe that the difference in freight costs between RR and PI is extremely large, even though the actual difference is only about 9.8%. Starting the Y-axis at 39 exaggerates the visual difference between the values.

## Part 1 — Pick the Chart from the Question

In this part, I learned how to choose the appropriate chart based on the question I want to answer.

### 1. Bar Chart — Comparing Values

A bar chart is used to compare values and identify which category has the highest or lowest result. I used it to display the top 10 product categories based on total sales. The health and beauty category had the highest sales.

Important result: Health and beauty was the highest-selling category, with **[insert sales value in thousands of R$]**.

### 2. Line Chart — Changes Over Time

A line chart is used to show how values change over time. I used it to display daily orders from October to December 2017. I also calculated a 7-day rolling average using pandas to make the overall trend easier to understand.

Important result: Black Friday, on November 24, 2017, had 1,176 orders. The 7-day average for that day was 346.4 orders.

### 3. Histogram — Distribution of Values

A histogram shows how numerical values are distributed across different ranges. I used it to analyze the hours of customer purchases throughout the day.

Important result: The busiest hour started at 4 PM, with 6,675 orders, while the quietest hour started at 5 AM, with 188 orders.

### 4. Scatter Plot — Relationship Between Two Values

A scatter plot is used to explore the relationship between two numerical variables. I used it to compare product weight with freight cost. The chart showed that heavier products generally have higher freight costs, although this is not always the case.

Important result: **[insert the number of products weighing exactly 30,000 grams]** products weighed exactly 30,000 grams, while **[insert the number of products weighing more than 30,000 grams]** weighed more.

### 5. Stacked Bar Chart — Share of a Total

A stacked bar chart is used to show how different parts contribute to a total. I used it to compare the percentage of money paid through each payment type.

Important result: Credit cards represented 78.3% of all money paid, followed by boleto at 17.9%, vouchers at 2.4%, and debit cards at 1.4%.

### Exercise 1.a — Weekend Purchase Hours

I filtered the purchase records to include Saturdays and Sundays only, using the dayofweek accessor. Then, I created a histogram to analyze the distribution of purchase hours and compared the busiest hour during weekends with the busiest hour on weekdays.

### Exercise 1.b — Products Weighing 30,000 Grams

I counted the products that weigh exactly 30,000 grams and those that weigh more than 30,000 grams. The scatter plot showed a vertical group of points at 30,000 grams, possibly because this value is used as a maximum or default recorded weight. This explanation needs further investigation.

- Products weighing exactly 30,000 g: **[143]**
- Products weighing more than 30,000 g: **[1]**

### What I Learned

I learned that different charts answer different types of questions. I also practiced using pandas and Matplotlib to create charts, analyze distributions, compare categories, explore relationships between variables, and understand how payment methods contribute to total payments. Choosing the right chart makes data easier to understand and helps avoid misleading conclusions.

## Part 2 — One Chart, One Message

In this part, I learned how to create charts with meaningful titles that communicate the main finding instead of simply describing the displayed data.

I recreated three charts from Part 1 and improved them by adding message titles and clear axis labels.

### 1. Daily Orders Chart

The first chart shows the daily number of orders and the 7-day rolling average from October to December 2017.

**Message title:** Black Friday 2017 sold 1,176 orders in one day.

The chart was saved as `day-10-black-friday.png`.

### 2. Product Category Sales Chart

The second chart displays the top 10 product categories based on total item sales.

**Message title:** Health and beauty sells the most, just ahead of watches and gifts.

The chart was saved as `day-10-categories.png`.

### 3. Purchase Hours Histogram

The third chart shows the distribution of purchases throughout the 24 hours of the day.

**Message title:** Most purchases happen at 4 PM, with 6,675 orders.

The chart was saved as `day-10-hours.png`.

### What I Learned

I learned that a chart title should communicate its main finding in a short sentence. I also practiced adding clear axis labels, using legends to explain chart lines, and saving charts as PNG images using Matplotlib's `savefig()` function.

This makes charts easier to understand and more suitable for reports and presentations.

## Part 3

### 1. Two Y-Axes

**What was wrong?**

The original chart used two different Y-axes to display monthly orders and average freight costs. The freight axis started at 17.5 and ended at 20.5, making small changes in freight appear as large as changes in thousands of orders. This could mislead the reader into thinking that both values changed in a similar way.

**What I changed:**

I created two separate line charts, one above the other, using `plt.subplots(2, 1, sharex=True)`. Both charts share the same monthly X-axis, but each has its own Y-axis and clear labels. This makes the differences between order volume and freight cost easier to understand.

**Saved file:** `day-10-fix-1.png`

### 2. Area for One Number

**What was wrong?**

The original chart used circles to represent the number of orders in the top five states. The size of each circle was based on the squared order count. This made the visual area grow much faster than the actual difference in orders. For example, SP has 3.25 times as many orders as RJ, but its circle covers approximately 10.6 times the area. This makes it difficult for readers to compare the values accurately.

**What I changed:**

I replaced the circle chart with a horizontal bar chart. The bars make it easier to compare the number of orders between states using their lengths instead of their areas. I also sorted the states in ascending order and added a meaningful title and clear axis labels.

**Saved file:** `day-10-fix-2.png`

### 3. Too Many Colors

**What was wrong?**

The original chart used a pie chart to display the sales of the top 15 product categories. Matplotlib uses a default set of 10 colors, so the colors started repeating for the remaining slices. This made some categories difficult to distinguish. Also, comparing the sizes of pie slices is not as easy as comparing bar lengths.

**What I changed:**

I replaced the pie chart with a horizontal bar chart. This makes it easier to compare the sales of all 15 categories using bar lengths instead of slice sizes. I also sorted the categories in ascending order and added a meaningful title and clear axis labels.

**Saved file:** `day-10-fix-3.png`

### 4. A Month That Is Not There

**What was wrong?**

The original chart did not show November 2016 because there were no recorded orders during that month. SQL GROUP BY returned only months with existing records. As a result, October and December appeared next to each other, which could make the timeline misleading.

**What I changed:**

I used set_index("month") to make the month column the DataFrame index, then applied resample("MS").sum() to create a continuous monthly sequence. This includes missing months with a value of zero. I also added a meaningful title, clear axis labels, and formatted the month labels for better readability.

**Saved file:** `day-10-fix-4.png`

### 5. No Message

**What was wrong?**

The original chart displayed the days of the week in alphabetical order because sort_index() sorts text values alphabetically instead of following the natural order of the week. The title was only "Weekday" and did not communicate any finding. The chart also lacked clear axis labels.

**What I changed:**

I used a custom list containing the days from Monday to Sunday and applied reindex() to arrange them in the correct order. I used idxmax() and max() to identify the busiest day and its number of orders, then created a dynamic title using an f-string. I also added clear axis labels.

**Saved file:** day-10-fix-5.png

## Part 4 — Small Multiples

In this part, I learned how to use small multiples to compare four product categories using separate line charts instead of displaying all lines in a single chart.

### Data Preparation

I used SQL to retrieve the daily number of items sold for four selected product categories between October and December 2017. The query joined the order_items, orders, and products tables and grouped the results by day and category.

### Creating Small Multiples

I used Seaborn's `relplot()` function to create four small line charts, one for each category. The `col` parameter separated the charts by category, while `col_wrap=2` arranged them into two columns.

All four charts shared the same axes, making it easier to compare the number of items sold. The chart showed a sharp increase in all four categories during Black Friday.

**Message title:** All four categories saw a sharp rise in items sold on Black Friday.

The final chart was saved as `day-10-categories-black-friday.png`.

### Exercise 4.a — Independent Y-Axes

I repeated the small multiples chart using `facet_kws={"sharey": False}`. This gave each chart its own Y-axis scale.

I learned that independent Y-axes make it easier to observe changes within categories that have different value ranges. However, they make direct comparison of actual values across categories more difficult because each chart uses a different scale.

### What I Learned

I learned how to use Seaborn's `relplot()` to create multiple charts from grouped data. I also learned how shared and independent axes affect data comparison. Small multiples help organize complex data and make patterns across different groups easier to understand.

## Part 5 — Charts You Can Explore

In this part, I learned how to create interactive charts using Plotly Express.

### Creating an Interactive Line Chart

I used `px.line()` to recreate the daily orders chart from Part 1. The chart displays the actual daily orders and the 7-day rolling average from October to December 2017.

I used `reset_index()` to convert the day index back into a regular column so that Plotly could use it on the X-axis.

The interactive chart allows users to hover over the lines to see exact values and zoom into specific periods.

### Exercise 5.a — Black Friday Week

I zoomed into the week of Black Friday and inspected the values for November 24, 2017.

- Actual daily orders: **1,176**
- 7-day rolling average: **346.4**

### What I Learned

I learned that Plotly is useful for interactive data exploration because it allows users to inspect exact values and zoom into specific periods.

Matplotlib is more suitable for reports when a consistent, static image is needed, while Plotly is useful when exploring data and examining detailed values interactively.

## Errors and Lessons

During Day 10, I learned that charts can be misleading even when the underlying data is correct. I identified several charting problems and learned how to avoid them.

### 1. Truncated Y-Axis

**What was wrong?**

The first bar chart started its Y-axis at 39 instead of 0. This made RR's bar look about 27 times taller than PI's bar, even though the actual difference in average freight cost was only about 9.8%.

**What I learned:**

Bar charts should start at zero because the length of each bar represents its value. Starting the axis above zero can exaggerate differences and mislead the reader.

### 2. Two Y-Axes

**What was wrong?**

The chart used two different Y-axes for monthly orders and average freight costs. The different scales made small changes in freight appear as large as changes in thousands of orders.

**What I learned:**

Using separate charts with a shared X-axis makes it easier to compare different measurements without creating misleading visual relationships.

### 3. Area for One Number

**What was wrong?**

The chart used circles to represent the number of orders for different states. Comparing circle areas was difficult and made the differences look larger than they really were.

**What I learned:**

Horizontal bar charts are easier to read when comparing numerical values because people can compare bar lengths more accurately than circle areas.

### 4. Too Many Colors

**What was wrong?**

The pie chart displayed 15 product categories, but some colors were repeated because the default color palette had only 10 colors. This made some categories difficult to distinguish. Comparing slice sizes was also difficult.

**What I learned:**

Charts should use clear and distinguishable visual elements. Horizontal bar charts are often more suitable when comparing many categories.

### 5. A Month That Is Not There

**What was wrong?**

November 2016 was missing from the original chart because there were no recorded orders for that month. This made October and December appear next to each other.

**What I learned:**

Missing time periods should be included when they represent zero activity. The pandas resample("MS").sum() method can create a continuous monthly sequence and include missing months with zero values.

### 6. No Message

**What was wrong?**

The weekday chart displayed days in alphabetical order instead of their correct weekly order. It also had a generic title and missing axis labels.

**What I learned:**

Charts should use a logical order, meaningful message titles, and clear axis labels. The reindex() function can arrange weekdays in their correct order.

### Overall Lesson

A chart should communicate the actual meaning of the data without exaggerating differences, hiding information, or confusing the reader. Choosing the right chart type, using appropriate scales, organizing data correctly, and adding meaningful titles are essential for honest data visualization.
