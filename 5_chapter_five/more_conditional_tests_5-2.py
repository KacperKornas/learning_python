print("\t 1 \n")
car = 'chevrolet'
print(car == 'chevrolet')
print(car == 'porshe')


print("\n\t 2 \n")
game = 'Chess'
print(game == 'Chess')
print(game.lower() == 'Chess')


print("\n\t 3 \n")
age = 23
print("age = 23")
print(age == 23)
print(age == 26)

print("\nage = 23")
print(age != 28)
print(age != 23)

print("\nage > 23")
print(age > 22)
print(age < 22)

print("\nage < 23")
print(age > 22)
print(age < 22)

print("\nage <= 23")
print(age <= 23)
print(age >= 24)

print("\nage >= 23")
print(age >= 23)
print(age <= 22)


print("\n\t 4 \n")
print("If price > 50 and price < 150")
price = 120

if price > 50 and price < 150:
    print("True")
else:
    print("False")
    
if price > 130 and price < 150:
    print("True")
else:
    print("False")

print("\nIf price > 50 or price == 30:")
if price > 50 or price == 30:
    print("True")
else:
    print("False")
    
if price > 130 or price == 30:
    print("True")
else:
    print("False")
    

print("\n\t 5 \n")
country = ['italy', 'slovenia', 'montenegro', 'austria']

print('slovenia' in country)
print('germany' in country)


print("\n\t 6 \n")
expencive_country = 'usa'

if expencive_country not in country:
    print("True")

if country not in country:
    print("False")

