if len(str) >= n:
    l = []
    for i in str:
        l.append(i)
    l.pop(n)
    a = ""
    for k in l:
        a = a + k

    return a