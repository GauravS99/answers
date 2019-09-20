# Time Complexity: O(n)
# Space Complexity: O(1)


def estimate_e(n):
    """
    In 2004, using series compression, Brothers proposed 

    $$ e=\sum_{n=0}^{\infty} \frac{2n+2}{(2n+1)!} $$    (use latex to visualize)

    to calculate the value of *e*.  Implement a function that performs this estimation given an positive integer *n*, where *n* is a provided parameter, and returns the result as a double.
    
    """
    
    e = 0.0
    fact = 1 # accumulate fact so you don't need to calculate factorial each time

    for i in range(n):
        doublei = 2 * i
        if i != 0:
            fact = (doublei + 1) * (doublei) * fact
        e += ((2 * i + 2) / fact)

    return e
