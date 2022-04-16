# This component provides the opportunity for new users to find out how the program is supposed to work

# Function containing instructions
def show_instructions():
    print("Mega movie fundraiser Instructions"
          "Instructions go here, they are brief but helpful")

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

instructions = ""
while not instructions:
    instructions = not_blank("would you like to read the instructions?: ").lower
    instructions = (get_choice(instructions, valid_yes_no))
if instructions == "Y":
    show_instructions()
print("Program launches...")
