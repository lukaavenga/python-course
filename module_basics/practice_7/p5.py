with open('test2.txt', 'r') as f:
    text = f.read().lower()
    words = []
    word = ''
    for char in text:
        if char.isalnum() or char == '_':
            word += char
        else:
            if word:
                words.append(word)
                word = ''
    if word:
        words.append(word)
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1
    if not counter:
        print([])
    max_count = max(counter.values())
    most_common = [word for word, count in counter.items()
                   if count == max_count]
    print("Most common word:", ", ".join(most_common),
          f"(appeared {max_count} times)")
