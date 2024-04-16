s_n = int(input("Introdu start : "))
e_n = int(input("Introdu stop : "))
if s_n < e_n:
    n = s_n
    m = e_n
    while n < m:
        print(n)
        n += 1
if s_n > e_n:
    n = s_n
    m = e_n
    while n > m:
        print(n)
        n -= 1
