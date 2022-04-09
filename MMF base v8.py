#import statement
import pandas
#Functions



def snacks_validator(choice, valid_choice):
    error_message = "sorry ,that's not a valid input please try again"

    for list_item in valid_choice:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    return snacks_validator(choice, valid_choice)
    print(error_message)

def split_orders(choice):

    #To test if an item starts with a number
    number_regex = "^[1-9]"
    #if an item does have number sepreate it with the rest
    if re.match(number_regex, choice):
        amount = int(choice[0])
        snack_name = choice[1:]
    #iF has no number assume it's one
    else:
        amount = 1
        snack_name = choice
    #Removing space
    snack_name = snack_name.strip()
    return snack_name, amount

def collate_orders():
    Valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&m", "mms", "m", "(2"],
                ["pita chips", "chips", "pc", "pita", "c", "(3"], ["water", "w", "(4"],
                ["orange juice", "oj", "(5"], ["x", "exit", "(6"]]
#valid options
    valid_yes_no_answer = [["yes", "y"], ["n", "no"]]
    snack_order = []
    max_number_of_snacks = 4
#assuming everyone wants snacks
    getting_snacks = True
    while getting_snacks:
    #To find out if they want sancks or not
     snacks_required = ""
     while snacks_required != "N" and snacks_required != "Y":
        #Response passed to generic string checking function
        #With the list yes_no valid answers as parameters
        checks_snacks = input("Do you want snacks? (Y/N): ").lower()
        snacks_required = snacks_validator(checks_snacks, valid_yes_no_answer)

     if snacks_required == "N":
          getting_snacks = False
          break
     else:
        #otherwise for each snakcs, the generic string checker is called with
    #the "ask for snacks' question and the list of valid snacks as parameters
        option = ""
        while option != "X":
            snack = input("what snacks do you want or enter X to stop ordering: ").lower()
            snack = split_orders(snack)
            quantity = snack[0]
            if quantity > max_number_of_snacks:
                 snack = None
                 print("Sorry the max anount you can order is 4")
            else:
                snack = snack[1]
                option = snacks_validator(snack, Valid_snacks)
                if option == "X":
                     getting_snacks = False
                elif option is not None:   #Filters out the invalid choices
                     snack_order.append([quantity, option])
     return snack_order


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

def check_valid_payment_method():
    ask_payment_method = input("how do you want to pay: ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = snacks_validator(ask_payment_method, valid_payment_method)
    return payment_method
# main routine

# set up dictionarys
all_name = []
all_tickets = []

#Create sepreate list for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# Put the sepearate list above in to master list
snack_lists = [popcorn, mms, pita_chips, orange_juice, water]

#store surcharge mutiplier
surcharge_mult_list = []

#Data frame dictionary
movie_data_dict = {'name': all_name,
                   'tickets': all_tickets,
                    "popcorn": popcorn,
                    "water" : water,
                    "Pita chips" : pita_chips,
                    "Mms" : mms,
                    "orange juice" : orange_juice,
                    "Surcharge Multiplier": surcharge_mult_list
                   }
# Cost of each snack
price_dict = {
    "popcorn": 2.5,
    "water": 2,
    "Pita chips": 4.5,
    "Mms": 3,
    "orange juice": 3.25
}



#Did the user used the proggame before, if no give them the instructions

#Loop to get tickets detail
Surcharge_rate = .05
min_age = 12
max_age = 110
Max_tickets = 10
ticket_cost = 5
name = ""
ticket_count = 0
profit = 0
surcharge = 0
#Get name(can't be blank)

while name != "X" and ticket_count != Max_tickets:
     check_max_tickets(Max_tickets, ticket_count)
     #Get details and name
     name = check_name("Enter the name of the ticket holder: ").title()
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
            snack_order = collate_orders()

            # Assume no snacks have been bought
            for item in snack_lists:
                item.append(0) #  Add 0 as the amount for each item


            # Print snack orders
            for item in snack_order:
                if len(item) > 0:
                    to_find = item[1]  #The name of the snack
                    amount = item[0]   #The amount of the snacks
                    add_list = movie_data_dict[to_find]  #Match the name to the snack menu
                    add_list[-1] = amount  #appends the number ordered to the end of the dictionary list of quantities ordered

#Snack lists

#After loops is broken chekcing for an empty list
            if len(snack_order) > 0:
                print("Here is your order summary: ")
                for item in snack_order:
                    print(f"\n{item[0]} {item[1]}")
            else:
                print("No snacks have been ordered")
                # Get payment method(and workout surcharge if necceary)
            payment_method = check_valid_payment_method()
            if not payment_method:
                continue
            elif payment_method == "Credit Card":
                surcharge_mutiplier = Surcharge_rate
            else:
                surcharge_mutiplier = 0

            surcharge_mult_list.append(surcharge_mutiplier)



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
print()
movie_frames = pandas.DataFrame(movie_data_dict)
movie_frames = movie_frames.set_index("Name")  #change reference to names rather than an atual number
# Create column called sub total
# contains price for tickets and snacks
movie_frames["Sub Total"] = \
    movie_frames = ["tickets"] + \
    movie_frames   ["popcorn"] * price_dict["popcorn"] + \
    movie_frames   ["water" ] * price_dict["water" ] + \
    movie_frames   ["Pita chips" ] * price_dict["Pita chips" ] + \
    movie_frames   ["Mms" ] * price_dict["Mms" ] + \
    movie_frames   ["orange juice" ] * price_dict["orange juice" ]

movie_frames["Surcharge"] = \
     movie_frames["Sub Total"] * movie_frames["Surcharge Multiplier"]
movie_frames["Total"] = movie_frames["Sub Total"] + movie_frames["Surcharge"]
# Shroten column names
movie_frames = movie_frames.rename(columns={"orange juice": "OJ",
                                            "Pita chips": "Chips",
                                            "Surcharge Multiplier": "SM"})
print(movie_frames)
   #Get name(can't be blank)

   #Get age(between 12-110)

   #Get ticket price

   #Ask for snacks

   #Calculate snack price

   #Payment method(sur charge for credit card)

#calculate total files and profit

#PRint details
