def is_palindrome(word):
    word = word.replace(" ", "").lower()
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def max_of_three(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num


def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result


def count_letter_occurrences(full_name):
    occurrences = {}
    for char in full_name.lower():
        if char.isalpha():
            occurrences[char] = occurrences.get(char, 0) + 1
    return occurrences


def get_card_priority(card):
    rank, suit = card

    ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
             "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    suits = {"Clubs": 1, "Diamonds": 2, "Hearts": 3, "Spades": 4}

    return ranks[rank] * 10 + suits[suit]


def compare_cards(card1, card2):
    priority1 = get_card_priority(card1)
    priority2 = get_card_priority(card2)

    if priority1 > priority2:
        return card1
    else:
        return card2


def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence_lower = sentence.lower()

    for letter in alphabet:
        if letter not in sentence_lower:
            return False
    return True


def aggregate_dictionaries(*dicts):
    result = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            result[key] = result.get(key, 0) + value
    return result


def main():
    print("=" * 50)
    print("Practice 1: Palindrome Checker")
    print("=" * 50)
    words = ["abba", "mama", "mom", "kayak", "peeps", "bird rib"]
    for word in words:
        if is_palindrome(word):
            print(f"'{word}' is a palindrome")
        else:
            print(f"'{word}' is not a palindrome")

    user_word = input("Enter a word to check if it's a palindrome: ")
    if is_palindrome(user_word):
        print(f"'{user_word}' is a palindrome")
    else:
        print(f"'{user_word}' is not a palindrome")

    print("\n" + "=" * 50)
    print("Practice 2: Prime Numbers from 1 to 1001")
    print("=" * 50)
    primes = []
    for num in range(1, 1002):
        if is_prime(num):
            primes.append(num)
    print(f"Found {len(primes)} prime numbers")
    print(f"First 10 primes: {primes[:10]}")
    print(f"Last 10 primes: {primes[-10:]}")

    print("\n" + "=" * 50)
    print("Practice 3: Max of Three Numbers")
    print("=" * 50)
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    print(f"Max of ({num1}, {num2}, {num3}): {max_of_three(num1, num2, num3)}")

    print("\n" + "=" * 50)
    print("Practice 4: Remove Duplicates")
    print("=" * 50)
    test_list_1 = [1, 2, 3, 2, 4, 1, 5, 6, 5]
    test_list_2 = ["apple", "banana", "apple", "orange", "banana"]
    print(f"Original: {test_list_1}")
    print(f"After removing duplicates: {remove_duplicates(test_list_1)}")
    print(f"Original: {test_list_2}")
    print(f"After removing duplicates: {remove_duplicates(test_list_2)}")

    print("\n" + "=" * 50)
    print("Practice 5: Letter Occurrences Counter")
    print("=" * 50)
    full_name = input("Enter a full name: ")
    result = count_letter_occurrences(full_name)
    print(f"Letter occurrences in '{full_name}':")
    print(result)

    print("\n" + "=" * 50)
    print("Homework 1: Playing Card Priority")
    print("=" * 50)
    print("Available ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace")
    print("Available suits: Clubs, Diamonds, Hearts, Spades")
    rank1 = input("Enter rank of first card: ")
    suit1 = input("Enter suit of first card: ")
    rank2 = input("Enter rank of second card: ")
    suit2 = input("Enter suit of second card: ")

    card1 = (rank1, suit1)
    card2 = (rank2, suit2)
    winner = compare_cards(card1, card2)
    print(f"{card1} vs {card2}: {winner}")

    print("\n" + "=" * 50)
    print("Homework 2: Pangram Checker")
    print("=" * 50)
    sentence = input("Enter a sentence to check if it's a pangram: ")
    if is_pangram(sentence):
        print(f"'{sentence}' is a pangram")
    else:
        print(f"'{sentence}' is not a pangram")

    print("\n" + "=" * 50)
    print("Homework 3: Dictionary Aggregation")
    print("=" * 50)
    dic1 = {"apple": 3, "banana": 2, "kiwi": 6}
    dic2 = {"banana": 7}
    dic3 = {"mango": 4}
    result = aggregate_dictionaries(dic1, dic2, dic3)
    print(f"dic1 = {dic1}")
    print(f"dic2 = {dic2}")
    print(f"dic3 = {dic3}")
    print(f"Aggregated result: {result}")


if __name__ == "__main__":
    main()
