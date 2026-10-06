def print_right_angled_triangle(rows):
    """
    Prints a right-angled triangle pattern of stars (*).
    """
    for i in range(1, rows + 1):
        print("*" * i)


def print_pyramid(rows):
    """
    Prints a centered pyramid pattern of stars (*).
    """
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def print_left_angled_triangle(rows):
    """
    Prints a left-aligned/right-justified right-angled triangle pattern.
    """
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * i
        print(spaces + stars)


def analyze_numbers(start, end):
    """
    Iterates through a specified range of numbers and displays whether each is odd or even,
    followed by the count and sum of all prime numbers within that range.
    """
    prime_count = 0
    prime_sum = 0

    print(f"\nAnalyzing numbers from {start} to {end}:")

    for num in range(start, end + 1):
        # Determine Odd / Even
        parity = "even" if num % 2 == 0 else "odd"
        print(f"Number {num} is {parity}")

        # Check for Prime status
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_count += 1
                prime_sum += num

    print(
        f"Found {prime_count} prime numbers with a total sum of {prime_sum}."
    )


def main():
    """
    Main function providing an interactive console menu for pattern generation and range analysis.
    """
    while True:
        print("\nWelcome to the Pattern Generator and Number Analysis!")
        print("Select an option:")
        print("1. Right-angled Triangle")
        print("2. Pyramid")
        print("3. Left-angled Triangle")
        print("4. Analyze a range of numbers")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid number (1-5).")
            continue

        if choice == 5:
            print("Exiting program. Goodbye!")
            break

        if choice in [1, 2, 3]:
            try:
                rows = int(input("Enter the number of rows for the pattern: "))
                if rows <= 0:
                    print("Please enter a positive integer for rows.")
                    continue

                if choice == 1:
                    print_right_angled_triangle(rows)
                elif choice == 2:
                    print_pyramid(rows)
                elif choice == 3:
                    print_left_angled_triangle(rows)
            except ValueError:
                print("Invalid input! Please enter a valid integer for rows.")

        elif choice == 4:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))

                if start > end:
                    print(
                        "Start of range must be less than or equal to the end of range."
                    )
                    continue

                analyze_numbers(start, end)
            except ValueError:
                print("Invalid input! Please enter valid integers for range.")

        else:
            print("Invalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()