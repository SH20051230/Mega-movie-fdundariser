# This component provides the opportunity for new users to find out how the program is supposed to work

# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("would you like to read the instructions?: ").lower
        instructions = (get_choice(instructions, valid_responses))
    if instructions == "Y":
        print("\n*************************************************************\n"
              "\n\t\t**** Mega movie Fundraiser Instructions ***\n"
              "\n you will be shown how many tickets are still avalible\n"
              "for sale and asked for the first ticket-purchaser's name.\n"
              "you will then be asked to input the ticket-purchaser's age.\n"
              "'nThis is because:\n"
              "\t-the minimum age for entry is 12; and\n"
              "\t-there is a standard price for adults; but\n"
              "\t-different prices for students and retired people.\n"
              "and once these are entered you will then need to provide a\n"
              "valid method of payment.\n"
              "\nThis process keeps repearting until either all tickets are\n"
              "sold or you choose to exit the program.\n"
              "\n0n exit, a summary of sales and profits will be printed to\n"
              "the screen. Full details of all sales and profits are also \n"
              "output to .csv files. These can be found in the same\n"
              "directory in which the program is stored.\n"
              "\n*************************************************************\n")
    print("program launches...")


# Function takes the question and list of valid choices as parameters


def get_choice(choice, valid_choices):
    choice_error = "sorry ,that's not a valid input please try again"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice

    print(choice_error)


def not_blank(question):
    valid = ""
    while not valid:
        response = input(question).title()

        # If the name is blank, show the error message
        if not response.isalpha():
            print("You can't leave this blank")
        else:
            return response

# Main routine
# Valid options for any yes/no question


valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)
