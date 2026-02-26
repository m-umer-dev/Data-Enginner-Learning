DAY 01 Learning

ROW_NUMBER()
RANK()
DENSE_RANK()
SUM() OVER()
PARTITION BY

RANK() assigns the same rank to tied values but skips the next rank number.
DENSE_RANK() assigns the same rank to tied values but does not skip the next rank number.

I use ROW_NUMBER() when I need unique ranking even if values are tied, such as deduplication or selecting a single latest record per group.

GROUP BY:
Aggregates rows
Reduces number of rows
Collapses data

WINDOW FUNCTION:
Performs aggregation
But keeps original rows
Does not collapse data

Window functions allow aggregation without collapsing rows, which makes them useful for ranking, running totals, and comparing rows within a partition.

First I use the rank window function and then check the tie value and the put the condition to remove them

when we remove the order by in the window function it will not arrange in particular order.

ORDER BY inside a window function defines the logical ordering within a partition. Without it, ranking functions fail, and cumulative calculations like running totals cannot be computed correctly.
