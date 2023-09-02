# defining information for people
prompt = '\nEnter all pizza toppings.'
prompt += '\nEnter "order" when you finish: '

while True:
    message = input(prompt)
    if message != 'quit':
        print(f"We'll add {message} to your pizza.")
    else:
        break

