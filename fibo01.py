a = 0
print(a)
b = 1
print(b)
for i in range(18):
    c = a + b # next term
    print(c)
    a = b     # update 2 previous terms
    b = c     # update prior term 