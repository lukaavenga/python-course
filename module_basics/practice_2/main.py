def first_function():
    r = input("Enter radius: ")
    area = 3.14 * float(r) ** 2
    print("The area of the circle with radius", r, "is:", area)


def second_function():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(last_name, first_name)
    print("Number of characters in first name:", len(first_name))
    print("Number of characters in last name:", len(last_name))


def third_function():
    n = input("Enter an integer: ")
    nn = n + n
    nnn = n + n + n
    result = int(n) + int(nn) + int(nnn)
    print("The value of n + nn + nnn is:", result)


def fourth_function():
    days = int(input("Enter number of days: "))
    seconds = days * 24 * 60 * 60
    print("Total number of seconds:", seconds)


def fifth_function():
    text = "North Macedonia is a member of NATO, the Council of Europe, the World Bank, OSCE, CEFTA, BSEC and the WTO. Since 2005, it has also been a candidate for joining the European Union. North Macedonia is an upper-middle-income country by the World Bank's definitions and has undergone considerable economic reform since its independence in developing an open economy. It is a developing country with a very high Human Development Index and low income inequality; and provides social security, a universal health care system, and free primary and secondary education to its citizens."
    result = text.replace("North Macedonia", "Macedonia")
    print(result)


def sixth_function():
    full_name = input("Enter Name Fathers_Name Surname: ")
    parts = full_name.split()
    fathers_name = parts[1]
    print("Father's name:", fathers_name)


def main():
    first_function()
    second_function()
    third_function()
    fourth_function()
    fifth_function()
    sixth_function()


if __name__ == "__main__":
    main()
