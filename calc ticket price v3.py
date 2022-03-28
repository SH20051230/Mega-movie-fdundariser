def clac_tickets_price(age):
    Children_age = range(12, 16)
    Standard_age = range(16, 65)
    child_price = 7.5
    standard_price = 10.5
    Retired_price = 6.5
    if age in Children_age:
     ticket_price = child_price
    elif age in Standard_age:
     ticket_price = standard_price
    else:
     ticket_price = Retired_price

    return (ticket_price)

Testing = [["steven", 15],["Joseph",16],["jack",64],["Gavin",65]]
for test in Testing:
    test_name = test[0]
    test_age = test[1]
    print(f"for {test_name} the ticket price is {clac_tickets_price(test_age)}")

