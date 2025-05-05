# Fibonacci sequence

# Get the Fibonacci term position from the user
n = int(input("Enter the position of the Fibonacci term you want: "))

# Initial values
a = 0
b = 1

# Calculate the nth Fibonacci term
for i in range(2, n + 1):
    c = a + b
    a = b
    b = c

# Print the nth Fibonacci term
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    print(c)
