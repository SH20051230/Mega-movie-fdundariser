name = ""
count = 0
Max_tickets = 10
while name != "X" and count != Max_tickets:
    name = input("what's your name: ").title()
    count += 1
    print(f"you have {Max_tickets - count} tickets left")
if count < Max_tickets:
    print(f"you have sold {count} tickets and have {Max_tickets-count} tickets left")
else:
    print("you have sold all tickets")
