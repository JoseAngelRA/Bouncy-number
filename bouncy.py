"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def bouncy(n):
    d = str(n)
    increasing = decreasing = True
    for i in range(1, len(d)):
        if d[i] < d[i-1]:
            increasing = False
        elif d[i] > d[i-1]:
            decreasing = False
    return not (increasing or decreasing)

def number(p):
    nbouncy = 0
    n = 0
    while True:
        n += 1
        if(bouncy(n)):
            nbouncy += 1
        total = (nbouncy / n) * 100
        if total >= p:
            return n

print(number(99))