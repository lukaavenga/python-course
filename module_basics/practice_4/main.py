
def second_function():
  numbers = []
  for _ in range(4):
    num = int(input("Enter a number: "))
    numbers.append(num)
  
  even_numbers = [num for num in numbers if num % 2 == 0]
  odd_numbers = [num for num in numbers if num % 2 != 0]
  
  print(f"Even numbers: {even_numbers}")
  print(f"Odd numbers: {odd_numbers}")
  
def third_function():
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  filtered_fruits = [fruit for fruit in fruits if "a" in fruit and len(fruit) <= 5]
  print(f"Filtered fruits: {filtered_fruits}")


def fourth_function():
  authorized_users = ["admin", "root", "john_doe", "jane_doe"]
  admin_users = ["admin", "root"]

  name = input("Enter your username: ")

  if name in authorized_users:
    print(f"Welcome {name}!")
    if name in admin_users:
      print("You have admin rights, don't make career change actions!!!")
  else:
    print("Access denied. You are not an authorized user.")
    
def fifth_function():
  student_scores = {
    "Alice": 85,
    "Jack": 80,
    "Bob": 45,
    "Charlie": 92
  }
    
  name = input("Enter student name: ")
    
  if name in student_scores:
    score = student_scores[name]
    print(f"{name}'s score: {score}")
    if score >= 80:
      print(f"{name} has passed the exam!")
    else:
      print(f"{name} has failed the exam.")
  else:
    print(f"Student '{name}' not found in records.")
    

def sixth_function():
  numbers_list = [5, -2, 3, 4, 4, 5, 9, 7, 8, 10, 5, 0, 8, -2, 3, -1]
  unique_numbers = list(set(numbers_list))
  print(f"\nOriginal list: {numbers_list}")
  print(f"List without duplicates: {unique_numbers}")

def main():
  second_function()
  third_function()
  fourth_function()
  fifth_function()
  sixth_function()
  
if __name__ == "__main__":
    main()