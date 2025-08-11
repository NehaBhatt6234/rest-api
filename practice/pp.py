import logging

# Configure logging
logging.basicConfig(
    filename='../sum_program.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def sum_of_two_numbers(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    result = a + b
    logging.info(f"Calculated sum: {a} + {b} = {result}")
    return result


# Main program with logging, type hints, and error handling
try:
    num1: float = float(input("Enter first number: "))
    num2: float = float(input("Enter second number: "))

    result: float = sum_of_two_numbers(num1, num2)
    print("The sum is:", result)

except ValueError as e:
    logging.error(f"Invalid input: {e}")
    print("Invalid input. Please enter numeric values.")
