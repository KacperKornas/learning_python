def make_shirt( size, text ):
    """Summarize the shirt that's going to be made."""
    print(f"Size of your t-shirt is {size}.")
    print(f"Text on the t-shirt is {text.title()}.")

make_shirt('s', '"the metal fans"')
make_shirt(size='s', text="the metal fans")
