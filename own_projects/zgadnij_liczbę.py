from random import randint
number = randint(1, 100)

print("")
name = input("Jeśli chcesz wejść do gry to podaj swoje imię: ")
print(" ")
print("          $$$ ZGADNIJ LICZBĘ $$$$")
print(" ")
print("Jeśli chcesz zamknąć ten program wpisz 'q'.\n")
while True:
    guess_number = input("\nPodaj swoją liczbę od 1 do 100: ")
    if guess_number == 'q':
        break
    if int(guess_number) == number:
        print(" ")
        print(f"Tak {name.title()}! Udało Ci się!")
        print(f"Twoja liczba to {number}!")
        break
    elif int(guess_number) > number:
        print("Twoja liczba jest zbyt wysoka!")
    else:
        print("Twoja liczba jest zbyt mała!")
