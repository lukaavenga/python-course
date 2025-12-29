import random


def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_and_average(numbers):

    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}")
    print(f"Average: {average}")


def reverse_number(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return -reversed_num if negative else reversed_num


def print_kris_jenner_female_kids():
    kids = ["Kourtney", "Kim", "Khloé", "Rob", "Kendall", "Kylie"]
    female_kids = ["Kourtney", "Kim", "Khloé", "Kendall", "Kylie"]

    last_names = {
        "Kourtney": "Kardashian",
        "Kim": "Kardashian",
        "Khloé": "Kardashian",
        "Rob": "Kardashian",
        "Kendall": "Jenner",
        "Kylie": "Jenner"
    }

    print("Kris Jenner's female kids:")
    for kid in kids:
        for female in female_kids:
            if kid == female:
                print(f"{kid} {last_names[kid]}")
                break


def count_divisible(a, b, c):
    if c == 0:
        return None
    count = 0
    start = min(a, b)
    end = max(a, b)
    for num in range(start, end + 1):
        if num % c == 0:
            count += 1
    return count


def count_digits_and_letters(s):
    digits = sum(1 for char in s if char.isdigit())
    letters = sum(1 for char in s if char.isalpha())
    return {"Letters": letters, "Digits": digits}


def guess_number_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome! Guess the secret number between 1 and 10.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(
                f"Congratulations! You guessed the number {secret_number} in {attempts} attempt(s)!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


def even_digit_numbers():
    result = []
    for num in range(100, 401):
        num_str = str(num)
        if all(int(digit) % 2 == 0 for digit in num_str):
            result.append(num_str)
    print("Numbers with all even digits between 100 and 400:")
    print(",".join(result))


def count_fruit_occurrences():
    fruits = ["apple", "tomato", "apple", "kiwi", "apple", "orange",
              "banana", "apple", "kiwi", "kiwi", "kiwi", "mango"]
    occurrences = {}
    for fruit in fruits:
        occurrences[fruit] = occurrences.get(fruit, 0) + 1
    print("Fruit occurrences:")
    for fruit, count in occurrences.items():
        print(f"{fruit}: {count}")


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def decimal_to_binary(n):
    if n == 0:
        return "0"
    negative = n < 0
    n = abs(n)
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return "-" + binary if negative else binary


def main():
    numbers = [2, 4, 55, 59, 71, 81, 87, 98, 99]

    number = int(input("Enter a number: "))
    reverse_number_input = int(input("Enter another number to reverse: "))

    print(f"Factorial of {number} is: {factorial(number)}")

    sum_and_average(numbers)

    reversed_num = reverse_number(reverse_number_input)
    print(f"Reversed number: {reversed_num}")

    print_kris_jenner_female_kids()

    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    c = int(input("Enter the divisor (c): "))
    count = count_divisible(a, b, c)
    print(f"Count of numbers divisible by {c} between {a} and {b}: {count}")

    count_digits_and_letters_input = input(
        "Enter a string to count digits and letters: ")
    result = count_digits_and_letters(count_digits_and_letters_input)
    print(f"Letters: {result['Letters']}, Digits: {result['Digits']}")

    guess_number_game()

    even_digit_numbers()

    count_fruit_occurrences()

    palindrome_input = input("Enter a word to check if it's a palindrome: ")
    if is_palindrome(palindrome_input):
        print(f"{palindrome_input} is a palindrome.")
    else:
        print(f"{palindrome_input} is not a palindrome.")

    decimal_input = int(input("Enter a decimal number to convert to binary: "))
    binary_output = decimal_to_binary(decimal_input)
    print(f"Binary representation of {decimal_input} is: {binary_output}")


if __name__ == "__main__":
    main()
