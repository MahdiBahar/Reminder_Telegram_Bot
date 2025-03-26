def fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
        if num_terms < 1:
            print("Please enter a positive integer.")
        else:
            fib_seq = fibonacci(num_terms)
            print("Fibonacci sequence:", fib_seq)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
