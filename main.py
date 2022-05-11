"""
DIRECTIONS
A soldier wants to buy some bananas.
The first banana costs k dollars, the second 2k, third 3k, and so on.

Given k - the cost of the first banana, n - the amount of money the soldier has on him,
and w - the amount of bananas the soldier desires, print how much money he is short by.

If the soldier can pay for the bananas with his money on hand, print 0.
"""


"""
Math Time:

The total cost of all bananas can be expressed as k + 2k + 3k + ... + (w - 1)k + wk.
We can factor k out of all of these terms, leaving k(1 + 2 + 3 + ... + (w - 1) + w)

The inside sum is simply just the sum of all integers up to w.
Fortunately, we don't need to iterate as the sum of integers to an integer n is equal to n(n + 1) / 2.
This simplifies the equation to (kw)(w + 1) / 2.

This is only the total amount of money all the bananas cost however.
To get the amount the soldier is short by, we must subtract the previous equation by n.

This leaves us with the equation debt = (kw)(w + 1) / 2 - n.
"""

asArr = input().split(' ')
k = int(asArr[0])
n = int(asArr[1])
w = int(asArr[2])

debt = int(k * (w * (w + 1) / 2) - n)

print(debt if debt > 0 else 0)
