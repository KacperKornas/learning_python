print("\n\nGive me two numbers and I will add them to you.\n")

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

try:
    answer = int(first_number) + int(second_number)
    print(answer)

except ValueError:
    print("You must give me number not another sign.")
