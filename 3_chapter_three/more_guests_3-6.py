guest_list = ['albert einstein', 'leonardo da vinci', 'Pitagoras']

do_not_come = guest_list.pop(2)
guest_list.append('Isaac Newton')


print("\n I am honored to invite You Mr. " + guest_list[0].title() + " to diner.")
print("\n I am honored to invite You Mr. " + guest_list[1].title() + " to diner.")
print("\n I am honored to invite You Mr. " + guest_list[2].title() + " to diner.")

print("\n\n " + do_not_come.title() + " can't come to dinner.")

print("\n My dear guests. I found a bigger dinner table so I can invite more noble personalities.")

guest_list.insert(0, 'maria curie-skłodowska')
guest_list.insert(2, 'nicola tesla')
guest_list.insert(-1, 'niels bohr')

print("\n\n I am honored to invite You Mr. " + guest_list[0].title() + " to diner.")
print("\n I am honored to invite You Mr. " + guest_list[2].title() + " to diner.")
print("\n I am honored to invite You Mr. " + guest_list[-1].title() + " to diner.")





