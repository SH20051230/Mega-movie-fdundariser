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

def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"There are {maximum - sold} tickets left")
    else:
        print("You have only one ticket left")

def check_valid_age(minium, maximum):
    #confirm again the age, just to fix the error
    age = interger_checker(f"Please confirm {name}'s age: ")
    if age < minium:
        print(f"sorry {name} is too young for this movie")
    else:
        while not age <= maximum:
            age = interger_checker(f"at {age} {name} is very old, please re-enter {name}'s age")
        return age
#main routine
#set up dictionarys
all_name = []
all_tickets = []

#Data from dictionary
movie_data_dict = {'name': all_name,
                   'tickets': all_tickets
                   }



#Did the user used the proggame before, if no give them the instructions

#Loop to get tickets detail
Max_tickets = 10
ticket_cost = 5
name = ""
ticket_count = 0
profit = 0
#Get name(can't be blank)

while name != "X" and ticket_count != Max_tickets:
     check_max_tickets(Max_tickets, ticket_count)
     #Get details and name
     name = check_name("Enter the name of the ticket holder: ")
     if name == "X":
        break
     else:
        Age_range = range(12, 111)
        age = interger_checker(f"Please enter the {name}'s age: ")
        if age < 12:
             print(f"sorry {name} is too young for this movie")
        else:
            age = check_valid_age(12, 110)
            if not age:
                continue  #restarts the get ticket loop
            else:
             ticket_count += 1
            #Claculate ticket price
            ticket_price = clac_tickets_price(age)
            print(f"for {name} the ticket price is {ticket_price}")
            profit += (ticket_price - ticket_cost)

            #add ticket price and name to list
            all_name.append(name)
            all_tickets.append(ticket_price)

            #GEt snacks

            #Get payment method

        #end of ticket/snack/payment loop



if ticket_count < Max_tickets:
    if ticket_count > 1:
     print(f"you have sold {ticket_count} tickets")
    else:
     print("one ticket had now been sold")
    if Max_tickets - ticket_count > 1:
     print(f"{Max_tickets - ticket_count} tickets are still avalible")
    else:
        print("There is only one ticket left!!!")
else:
    print("YOu have sold all avalible tickets!!!")

#Print details
print(f"The profit is {profit}$")


   #Get name(can't be blank)

   #Get age(between 12-110)

   #Get ticket price

   #Ask for snacks

   #Calculate snack price

   #Payment method(sur charge for credit card)

#calculate total files and profit

#PRint details
