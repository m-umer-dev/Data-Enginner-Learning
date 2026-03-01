Because WHERE filters individual rows before aggregation, while HAVING filters grouped results after aggregation. Since we needed to filter based on COUNT(), which is an aggregate function, HAVING was required.

LAG() is used to access a previous row’s value based on a defined ordering, while LEAD() is used to access the next row’s value within the same partition.

✅ LAG()

Detect salary increase

Detect drop in sales

Compare with previous event

Find change over time

✅ LEAD()

Calculate time difference between events

Find churn date

Detect future status change

Identify gaps in sequence
