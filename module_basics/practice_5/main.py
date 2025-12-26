
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


def main():
    numbers = [2, 4, 55, 59, 71, 81, 87, 98, 99]
    
    number = int(input("Enter a number: "))
    reverse_number_input = int(input("Enter another number to reverse: "))
    
    print(f"Factorial of {number} is: {factorial(number)}")

    sum_and_average(numbers)

    reversed_num = reverse_number(reverse_number_input)
    print(f"Reversed number: {reversed_num}")

    print_kris_jenner_female_kids()


if __name__ == "__main__":
    main()
