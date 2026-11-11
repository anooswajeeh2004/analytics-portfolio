## The question

Does the spreadsheet give the same August 2018 revenue as SQL? And what happens if the delivery fee changes?

## The answer

Our custom revenue definition for August 2018 is R$848,860.10. Yes, the spreadsheet and SQL agree to the cent for the standard revenue calculations (Way 1 and Way 2 both showed exactly 0 difference).

If the delivery fee changes, here is the scenario breakdown:

- Today (Base): R$996,973.51 (Change: R$0.00)
- Fee up 10%: R$1,001,667.00 (Change: +R$4,693.49)
- Fee up 20%: R$985,532.34 (Change: -R$11,441.20)
- Fee down 10%: R$1,001,805.41 (Change: +R$4,831.90)
- Free delivery: R$933,746.11 (Change: -R$63,227.40)

The best scenario is "Fee down 10%", which brings in the most money. The worst scenario is "Free delivery", which brings in the least money.

## How sure I am

I am completely sure about the "Today" revenue numbers because they come directly from the real database data. However, the scenario outcomes (how much orders will change based on fee changes) are just guesses and estimates, not real data.

## What to do next

We should run a real A/B test or experiment on delivery fees instead of guessing. This will give us real data on how customer behavior actually changes when fees go up or down.
