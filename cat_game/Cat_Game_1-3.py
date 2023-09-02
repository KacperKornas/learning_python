def red_add_other_out():
    for color in colors:
        if color == 'red':
            accept.append(color)



        else:
            colors.remove(color)

    colors.clear()

colors = ['red', 'green', 'green', 'blue', 'green', 'red', 'blue', 'green', 'blue', 'red', 'red', 'red', 'blue']
print(colors)

accept = []


red_add_other_out()

print(accept)
print(colors)
