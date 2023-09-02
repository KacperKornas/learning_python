print("Enter 'q' at any time to quit.")

while True:

    print("\n\nGive me two numbers and I will add them to you.\n")

    first_number = input("Enter first number: ")

    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
        print(answer)

    except ValueError:
        print("You must give me number not other sign.")