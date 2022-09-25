prefixes = "apnum kMGTP"
n = 1000000

if n < 0:
    n *= -1

if n >= 1:
    pow = 0
    while n / (10 ** pow) >= 1:
        print( str(n) + " / " + str(10 ** pow) + " = " + str(n / (10 ** pow)) )
        pow += 3
    pow -= 3

    print(pow)

if n < 1:
    pow = 0
    while n / (10 ** pow) <= 1:
        print( str(n) + " / " + str(10 ** pow) + " = " + str(n / (10 ** pow)) )
        pow -= 3

    print(pow)

new_n = n * (10 ** (pow * -1))
print(str(n) + " -> " + str(new_n) + prefixes[(pow//3) + 5])
