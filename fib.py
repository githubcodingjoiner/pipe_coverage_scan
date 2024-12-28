def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main():
    n = int(input("Enter the number of terms: "))
    print(f"Fibonacci sequence: {generate_fibonacci(n)}")

if __name__ == "__main__":
    main()
