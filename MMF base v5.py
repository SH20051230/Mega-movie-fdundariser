#import statement

#Functions
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
#The ticket holder's name can't be blank
def check_name(question):
    while True:
        name = input(question).title()
        if not name.isalpha():
         print("you can't levave this blank")
        else:
            return name

#Interger checker(for age)
def interger_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("please enter an interger (not decimal)")
#main routine




#Did the user used the proggame before, if no give them the instructions

#Loop to get tickets detail
Max_tickets = 10
ticket_cost = 5
name = ""
ticket_count = 0
profit = 0
#Get name(can't be blank)

while name != "X" and ticket_count != Max_tickets:
     if Max_tickets - ticket_count > 1:
         print(f"you have {Max_tickets - ticket_count} tickets left")
     else:
        print("you have only ONE ticket left")
    #Get detail
     name = check_name("what's your name")
     if name == "X":
        break
     else:
        Age_range = range(12, 111)
        age = interger_checker("Please enter the ticket holder's age: ")
        if age < 12:
             print(f"sorry {name} is too young for this movie")
        else:
            while not age < 111:
              age = interger_checker(f"{name} is very old, please re-enter the age")
              print(f"Age = {age}")
            ticket_count += 1
     #Get ticket price
            tikcet_price = clac_tickets_price(age)
            print(f"for {name} your ticket price is {tikcet_price}")
            profit += (tikcet_price - ticket_cost)


if ticket_count < Max_tickets:
     print(f"you have sold {ticket_count} tickets and have {Max_tickets-ticket_count} tickets left")
else:
     print("you have sold all tickets")
print(f"The profit for the day is {profit}")



   #Get name(can't be blank)

   #Get age(between 12-110)

   #Get ticket price

   #Ask for snacks

   #Calculate snack price

   #Payment method(sur charge for credit card)

#calculate total files and profit

#PRint details
