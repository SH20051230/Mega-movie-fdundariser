def snacks_validator(question, valid_choice):
    error_message = "sorry ,that's not a valid input please try again"


    snack_choice = input("snack: ").lower()
    for item in Valid_snacks:
        if snack_choice in item:
            snack_choice = item[0].title()
            return snack_choice
    print(error_message)
    return snacks_validator(question, valid_choice)



ask_for_snacks = "what do you want for snacks, press X to stop ordering"
Valid_snacks = [["popcorn", "p", "corn", "1"], ["m&m", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"], ["water", "w", "4"]]
check_snacks = "do you want snacks"
valid_yes_no_answer = [["yes", "y"], ["n", "no"]]

Getting_snacks = True
snacks_required = snacks_validator(check_snacks, valid_yes_no_answer)
while Getting_snacks:
    if snacks_required == "n":
        print("you don't want snacks")
        Getting_snacks = False
    else:
        option = snacks_validator((ask_for_snacks, valid_yes_no_answer))
        if option != "X":
            print(f"you have chosen {option}")
        else:
            Getting_snacks = False
            print("thank you for ordering")
for test in range(6):
    print(f"you want {snacks_validator(ask_for_snacks, Valid_snacks)}")

