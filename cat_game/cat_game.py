colors = ['red', 'green', 'green', 'blue', 'green', 'red', 'blue', 'green', 'blue', 'red', 'red', 'red', 'blue']

red = []
blue =[]
green = []

for color in colors:
    if color == 'red':
        red.append(color)

    elif color == 'green':
        green.append(color)

    else:
        blue.append(color)

colors.clear()

print(red)
print(blue)
print(green)
print(len(colors))
print(len(red))
print(len(blue))
print(len(green))