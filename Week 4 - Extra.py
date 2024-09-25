# Fibonacci Seq. Generator:

def fibonacci_sequence(n):
# defines function called 'fibonacci_sequence', 'n' is the parameter and represents the total number of terms to generate.
    sequence = []
# initialize empty list called 'sequence' to hold the fibonacci numbers.
    a, b = 0, 1
# initialize a and b as the first two numbers (0 and 1) in the fibonacci sequence.
    for _ in range(n):
# starts loop that will run 'n' times.
        sequence.append(a)
# in every iteration, the next fibonacci number (a) is appended / added to the end of the list.
        a, b = b, a + b
# updates values so that a is set to b while b is set to the sum of (the old values of) a and b.
    return sequence
# after loop ends, all numbers are stored in 'sequence'.

# Example:

num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
# prompts users to input the number of terms they want.
fib_sequence = fibonacci_sequence(num_terms)
# calls the 'fibonnaci_sequence' function so that it uses 'num_terms' to generate the fibonnaci sequence and store it in 'fib_sequence'.
print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence}")
# displays the resulting fibonnaci sequence in a specific format.
