
# Function takes the question and list of valid choice as parameters
def snacks_validator(choice, valid_choice):
    error_message = "sorry ,that's not a valid input please try again"
    for list_item in valid_choice:
        if choice in list_item:
            choice = list_item[0].title()
            return choice

    print(error_message)

# Main routine
surcharge_rate = .05
name = input("what's your name: ").title()
# get subtotal for testing purposes
sub_total = float(input("Sub-total: $"))
ask_payment_method = input("how do you want to pay: ").lower()
valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                        ["eftpos", "eft", "pos", "ep", "e", "2"],
                        ["cash", "ca", "money", "notes", "coins", "c", "3"]]
payment_method = snacks_validator(ask_payment_method, valid_payment_method)
if not payment_method:
    print("Sorry that's not a valid payment method")
elif payment_method == "Credit Card":
    surcharge = (sub_total * surcharge_rate)
else:
    surcharge = 0

total_payable = sub_total + surcharge
print(f"{name} Sub-total: {sub_total}$"
      f"Surcharge: {surcharge}, The total payable is {total_payable}")

