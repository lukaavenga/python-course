with open('test.txt', 'a+') as file:

    file.write('\n2025-26 FC Barcelona')

    file.seek(0)
    print(file.read())
