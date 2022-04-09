import re


def split_orders(choice):

    #To test if an item starts with a number
    number_regex = "^[1-9]"
    #if an item does have number sepreate it with the rest
    if re.match(number_regex, choice):
        amount = int(choice[0])
        snack_name = choice[1:]
    #iF has no number assume it's one
    else:
        amount = 1
        snack_name = choice
    #Removing space
    snack_name = snack_name.strip()
    return snack_name, amount


def snacks_validator(choice, valid_choice):
    error_message = "sorry ,that's not a valid input please try again"
    for list_item in valid_choice:
        if choice in list_item:
            choice = list_item[0].title()
            return choice

    print(error_message)

def collate_orders():
    Valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&m", "mms", "m", "(2"],
                ["pita chips", "chips", "pc", "pita", "c", "(3"], ["water", "w", "(4"],
                ["orange juice", "oj", "(5"], ["x", "exit", "(6"]]
# valid options
    valid_yes_no_answer = [["y", "yes"], ["n", "no"]]
    snack_order = []
    max_number_of_snacks = 4
    # assuming everyone wants snacks
    getting_snacks = True
    while getting_snacks:
        # To find out if they want sancks or not
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            #Response passed to generic string checking function
            # With the list yes_no valid answers as parameters
            checks_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = snacks_validator(checks_snacks, valid_yes_no_answer)

        if snacks_required == "N":
            getting_snacks = False
            break
        else:
            # otherwise for each snakcs, the generic string checker is called with
            # the "ask for snacks' question and the list of valid snacks as parameters
            option = ""
            while option != "X":
                snack = input("what snacks do you want or enter X to stop ordering: ").lower()
                snack = split_orders(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                     snack = None
                     print("Sorry the max anount you can order is 4")
                else:
                    snack = snack[1]
                    option = snacks_validator(snack, Valid_snacks)
                    if option != "X":
                         getting_snacks = False
                    elif option is not None:   #Filters out the invalid choices
                         snack_order.append([quantity, option])
    return snack_order

snack_order = collate_orders()
#After loops is broken chekcing for an empty list
if len(snack_order) > 0:
    print("Here is your order summary: ")
    for item in snack_order:
     print(f"\n{item[0]} {item[1]}")
else:
    print("No snacks have been ordered")




