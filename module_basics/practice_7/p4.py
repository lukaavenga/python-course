with open('text2.txt', 'r') as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print(f"\n{longest_word}\n")
