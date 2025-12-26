def sum_three_numbers():
    print("Sum three numbers (returns 0 if any two are equal)\n")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a == b or b == c or a == c:
        print(0)
    else:
        print(a + b + c)


def get_grade():
    points = int(input("\nEnter points (0-100) to determine grade: "))
    if points < 0 or points > 100:
        print("Invalid score")
    elif points >= 90:
        print("A")
    elif points >= 80:
        print("B")
    elif points >= 70:
        print("C")
    elif points >= 60:
        print("D")
    else:
        print("F")


def check_divisibility():
    num = int(input("\nEnter a number to check if it is divisible by 7 or 5: "))

    div_by_7 = num % 7 == 0
    div_by_5 = num % 5 == 0

    if div_by_7 and div_by_5:
        print(f"{num} is divisible by both 7 and 5")
    elif div_by_7:
        print(f"{num} is divisible by 7 only")
    elif div_by_5:
        print(f"{num} is divisible by 5 only")
    else:
        print(f"{num} is not divisible by 7 or 5")


def check_positive():
    num = float(
        input("\nEnter a number to check if it is positive or negative: "))

    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")


def check_letters():
    full_name = input(
        "\nEnter full name (name surname) to determine vowels/consonants: ")

    parts = full_name.split()
    if len(parts) < 2:
        print("Please enter both name and surname")
        return

    name = parts[0]
    surname = parts[1]

    if len(name) < 3:
        print("Name must have at least 3 letters")
        return
    if len(surname) < 4:
        print("Surname must have at least 4 letters")
        return

    vowels = "aeiouAEIOU"

    third_letter = name[2]
    fourth_letter = surname[3]

    third_is_vowel = third_letter in vowels
    fourth_is_vowel = fourth_letter in vowels

    if third_is_vowel and fourth_is_vowel:
        print(f"Both '{third_letter}' and '{fourth_letter}' are vowels")
    elif not third_is_vowel and not fourth_is_vowel:
        print(f"Both '{third_letter}' and '{fourth_letter}' are consonants")
    else:
        print(
            f"'{third_letter}' and '{fourth_letter}' are a mix (one vowel, one consonant)")


def check_leap_year():
    year = int(input("\nEnter a year to check if it is a leap year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


def calculator():
    print("\nSimple Calculator\n")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("\nEnter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print(
            f"Warning: '{operator}' is not a valid operator. Please use +, -, *, or /")


def main():
    sum_three_numbers()
    get_grade()
    check_divisibility()
    check_positive()
    check_letters()
    check_leap_year()
    calculator()


if __name__ == "__main__":
    main()
