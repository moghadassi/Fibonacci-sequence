# Fibonacci sequence

# Get the Fibonacci term position from the user
n = int(input("Enter the position of the Fibonacci term you want: "))

# Check for invalid input
if n <= 0:
    print("Please enter a positive integer greater than 0.")
elif n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    # Initial values
    a = 0
    b = 1

    # Calculate the nth Fibonacci term
    for i in range(2, n):
        c = a + b
        a = b
        b = c

    # Print the nth Fibonacci term
    print(b)
