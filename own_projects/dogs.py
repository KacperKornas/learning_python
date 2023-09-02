# a = 0
# b = 0
# c = 0
#
# def quesion(a_quest, b_quest, c_quest):
#     """Print the question and add points."""
#
#     points_a = a
#     points_b = b
#     points_c = c
#
#     print("\n" * 5)
#     print(f"a) {a_quest}")
#     print(f"b) {b_quest}")
#     print(f"c) {c_quest}")
#     answer = input("\nChose your answer: ")
#
#     if answer == "a":
#         points_a += 1
#     elif answer == "b":
#         points_b += 1
#     elif answer == "c":
#         points_c += 1
#
#     print(points_a)
#
# quesion('a', 'b', 'c')
# quesion('a', 'b', 'c')
# quesion('a', 'b', 'c')

# a = 0
# b = 0
# c = 0
#
#
# class Questions:
#     """Class represents questions."""
#     a = 0
#
#     def __init__(self, a_quest, b_quest, c_quest):
#         """Initialize the questions."""
#         self.a_quest = a_quest
#         self.b_quest = b_quest
#         self.c_quest = c_quest
#
#     def quesion(self):
#         """Print the question and add points."""
#
#         points_a = a
#         points_b = b
#         points_c = c
#
#         print("\n" * 5)
#         print(f"a) {self.a_quest}")
#         print(f"b) {self.b_quest}")
#         print(f"c) {self.c_quest}")
#         answer = input("\nChose your answer: ")
#
#         if answer == "a":
#             points_a += 1
#         elif answer == "b":
#             points_b += 1
#         elif answer == "c":
#             points_c += 1
#
#         print(points_a)
#
#
# first_question = Questions('a', 'b', 'c')
# print(first_question.quesion())
# first_question = Questions('a', 'b', 'c')
# print(first_question.quesion())


work = True
while work:

    a = 0
    b = 0
    c = 0

    print("\n"*4)
    print("\t\t\t\t\t**************************")
    print("\t\t\t\t\t* Jakim psiakiem jesteś? *")
    print("\t\t\t\t\t**************************\n\n\n")

    name = input("Podaj swoje imię: ")

    maltańczyk = ['radosny', 'żywy', 'spokojny', 'inteligentny', 'wierny', 'szczęśliwy']
    charles_spaniel = ['spokojny', 'cierpliwy', 'łagodny', 'wdzięczny', 'towarzyski', 'przystosowujący się']
    rottwailer = ['nieustraszony', 'odważny', 'czujny', 'pewny siebie', 'nieustępliwy', 'charakterny']
    mix = ['nieznany', 'niewiadomy', 'losowy', 'nieodgadniony']

    print("\n"*5)
    print("a) Masz maksymalnie 160cm.")
    print("b) Masz 161cm - 175cm wzrostu.")
    print("c) Masz minimum 176cm wzrostu.")
    answer = input("\nChose your answer: ")

    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1

    print("\n"*5)
    print("a) Jesteś zrównoważona/y.")
    print("b) Jesteś spokojna/y.")
    print("c) Jesteś drażliwa/y.")
    answer = input("\nChose your answer: ")

    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1

    print("\n" * 5)
    print("a) Prowadzisz umiarkowany tryb życia.")
    print("b) Prowadzisz leniwy tryb życia.")
    print("c) Prowadzisz aktywny tryb życia.")
    answer = input("\nChose your answer: ")

    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1

    print("\n" * 5)
    print("a) Potrafisz postawić na swoim.")
    print("b) Wolisz się podporządkować.")
    print("c) Bywa różnie.")
    answer = input("\nChose your answer: ")

    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1

    print("\n"*5)
    print("a) Jesteś zrównoważona/y.")
    print("b) Jesteś strachliwa/y")
    print("c) Jesteś odważna/y.")
    answer = input("\nChose your answer: ")

    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1

    print("\n"*5)
    print("a) Lubisz się wyróżnić, ale nie dowodzisz grupą.")
    print("b) Raczej się nie wychylasz.")
    print("c) W grupie jesteś liderem.")
    answer = input("\nChose your answer: ")

    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1

    print("\n"*5)
    if a > b and a > c:
        print(f'{name.title()} jesteś rasowym Maltańczykiem! :D')
        print('\n\n\nWpisz "quit" aby zamknąć.')
        print('Wpisz "info", aby uzyskać więcej informacji.')
        information = input("")

        if information == 'info':
            print("\n" * 5)
            print("Maltańczyk jest:")
            for characteristic in maltańczyk:
                print(f"- {characteristic}")
            print("\nDziękujemy Maltańczyku, do zobaczenia!")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

        elif information == 'quit':
            print("\n" * 5)
            print("Dziękujemy Maltańczyku, do zobaczenia!\n\n\n")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

    elif b > a and b > c:
        print(f'{name.title()} drzemie w tobie spokojny Cavalier King Charles Spaniel! ^^')
        print('\n\n\nWpisz "quit" aby zamknąć.')
        print('Wpisz "info", aby uzyskać więcej informacji.')
        information = input("")

        if information == 'info':
            print("\n" * 5)
            print("Cavalier King Charles Spaniel jest:")
            for characteristic in charles_spaniel:
                print(f"- {characteristic}")
            print("\nDziękujemy Spanielku, do zobaczenia!")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

        elif information == 'quit':
            print("\n" * 5)
            print("Dziękujemy Spanielku, do zobaczenia!\n\n\n")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

    elif c > a and c > b:
        print(f'{name.title()} nikomu nie umknęło, to że prawdziwy z Ciebie Rottweiler! :->')
        print('\n\n\nWpisz "quit" aby zamknąć.')
        print('Wpisz "info", aby uzyskać więcej informacji.')
        information = input("")

        if information == 'info':
            print("\n" * 5)
            print("Rottweiler jest:")
            for characteristic in rottwailer:
                print(f"- {characteristic}")
            print("\nDziękujemy Rottweilerze, do zobaczenia!")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

        elif information == 'quit':
            print("\n" * 5)
            print("Dziękujemy Rottweilerze, do zobaczenia!\n\n\n")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

    else:
        print(f'{name.title()} z Ciebie to nie wiadomo co wyrośnie "Rasowy Mieszańcu"! :p')
        print('\n\n\nWpisz "quit" aby zamknąć.')
        print('Wpisz "info", aby uzyskać więcej informacji.')
        information = input("")

        if information == 'info':
            print("\n" * 5)
            print("Mieszaniec jest:")
            for characteristic in mix:
                print(f"- {characteristic}")
            print("\n*Każdy psiak jest kochany i dla Ciebie będzie najlepszy na świecie!!!*")
            print("\nDziękujemy Mieszanko, do zobaczenia!")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False

        elif information == 'quit':
            print("\n" * 5)
            print("Dziękujemy Mieszanko, do zobaczenia!\n\n\n")
            print("Czy chcesz Jeszcze raz wziąć udział w ankiecie? (tak/nie)")
            decision = input("")
            if decision == 'tak':
                work = True
            else:
                work = False
