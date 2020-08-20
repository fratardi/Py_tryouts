from decimal import *

def pi():
    getcontext().prec = 400 #here is fine, and probably better
    mod = 1
    ret = Decimal(0)
    start = 0
    while start < 400:
    #tab here ok ? 
        ret = Decimal(ret) + (Decimal(1.0 / (mod)) * \
        ( \
            (Decimal(4.0) / (Decimal(8.0 * start) + Decimal(1.0))) \
            - (Decimal(2.0) / (Decimal(8.0 * start) + Decimal(4.0)))\
            - (Decimal(1.0) / (Decimal(8.0 * start) + Decimal(5.0)))\
            - (Decimal(1.0) / (Decimal(8.0 * start) + Decimal(6.0)))))
        mod *= 16.0
        start += 1   
    return (ret)

print(pi())
