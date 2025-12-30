with open("test2.txt", "r", encoding="utf-8") as file:
    content = file.read()

content = content.replace("Seavus", "Avenga")

with open("test2_replaced.txt", "w", encoding="utf-8") as file:
    file.write(content)
