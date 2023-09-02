colors = ['red', 'green', 'green', 'blue', 'green', 'red', 'blue', 'green', 'blue', 'red', 'red', 'red', 'blue']
print(colors)

accept = []

for color in colors:
    if color == 'blue':
        colors.remove(color)



    else:
        accept.append(color)

colors.clear()


print(accept)
print(colors)
