guest_list = ['albert einstein', 'leonardo da vinci', 'Pitagoras']

do_not_come = guest_list.pop(2)
guest_list.append('isaac newton')


print("\n I am honored to invite You Mr. " + guest_list[0].title() + " to dinner.")
print("\n I am honored to invite You Mr. " + guest_list[1].title() + " to dinner.")
print("\n I am honored to invite You Mr. " + guest_list[2].title() + " to dinner.")

print("\n\n " + do_not_come.title() + " can't come to dinner.")

print("\n My dear guests. I found a bigger dinner table so I can invite more noble personalities.")

guest_list.insert(0, 'maria curie-skłodowska')
guest_list.insert(2, 'nicola tesla')
guest_list.insert(4, 'niels bohr')

print("\n\n I am honored to invite You Mrs. " + guest_list[0].title() + " to dinner.")
print("\n I am honored to invite You Mr. " + guest_list[2].title() + " to dinenr.")
print("\n I am honored to invite You Mr. " + guest_list[4].title() + " to dinner.")


print("\n\n I am very sorry but the new table won't arrive in time so I can invite only two people for dinner.")

do_not_invite = guest_list.pop(0)

print("\n\n I am realy sorry but I can't You invite Mr. " + do_not_invite.title() + " to dinner.") 

do_not_invite_2 = guest_list.pop(1)

print("\n I am realy sorry but I can't You invite Mrs. " + do_not_invite_2.title() + " to dinner.")

do_not_invite_3 = guest_list.pop(1)

print("\n I am realy sorry but I can't You invite Mrs. " + do_not_invite_3.title() + " to dinner.")

do_not_invite_4 = guest_list.pop(1)

print("\n I am realy sorry but I can't You invite Mrs. " + do_not_invite_4.title() + " to dinner.")


print("\n\n You are still invited to dinner Mr " + guest_list[0].title() + ".")
print("\n You are still invited to dinner Mr " + guest_list[1].title() + ".")

del guest_list[0]
del guest_list[0]

print("\n " + str(guest_list))
