def Snack_checker_Yes_No(question):
 Possible_answer = ["Yes", "No", "Y", "N"]
answer = input("Do you want order snacks").upper()
while answer not in Possible_answer:
    print("Please try again by entering Yes or No")
    input("Do you want order a snack?: ")
    if answer == "Yes" or "Y":
     print("Accepted what do you want to order?")
    else:
     print("Declined you don't want order snacks")

snacks = Snack_checker_Yes_No("Do you want to order snacks?: ")



