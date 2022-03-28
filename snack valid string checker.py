def snacks_validator():
    error_message = "sorry ,that's not a valid input please try again"
    Valid_snacks = [["popcorn", "p", "corn", "1"], ["m&m", "mms", "m", "2"],
                    ["pita chips", "chips", "pc", "pita", "c", "3"], ["water", "w", "4"]]\
    snack_choice = input("snack: ").lower()
    for snack in Valid_snacks:
        if snack_choice in snack:
            snack_choice = snack[0].title()
            return snack_choice
    print(error_message)
    return snacks_validator()

for test in range(6):
    print(f"you want {snacks_validator()}")

