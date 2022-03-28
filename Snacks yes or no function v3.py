def Snack_checker_Yes_No(question):
   error = "Please try again by entering Yes or No"
   Possible_answers = ["Yes", "No", "Y", "N"]
   answer = input(question).upper()
   while answer not in Possible_answers:
    print(error)
    input(question).upper()

   if answer[0] == "N":
    return False
   else:
    return True

Test = True
while Test:
 snacks = Snack_checker_Yes_No("Do you want to order snacks? ")
 if not snacks:
    print("Declined you don't want order snacks")
 else:
    print("Accepted what do you want to order?")


