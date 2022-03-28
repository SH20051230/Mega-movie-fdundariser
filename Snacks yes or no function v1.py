error = "Please try again by entering Yes or No"
Possible_answer = ["Yes", "No", "Y", "N"]
answer = input("Do you want order a snack?: ")
while answer not in Possible_answer:
    print(error)
    input("Do you want order a snack?: ")
if answer == "N" or answer == "No":
    print("Declined you don't want order snacks")
elif answer == "Y" or "Yes":
    print("Accepted You do want snacks")

