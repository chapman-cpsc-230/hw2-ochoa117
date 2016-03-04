n_str = raw_input("Enter a natural number: ")
n = int(n_str)

b = 2.0
i = 0
s = 0
while i <= n:
    i += 1
    s += b**(i - 1)

print s
print (b**(n + 1) - 1)/(b - 1)
