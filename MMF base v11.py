#import statement
import re
import pandas
#Functions



def get_choice(choice, valid_choice):
    choice_error = "sorry ,that's not a valid input please try again"
    for list_item in valid_choice:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)

def split_orders(choice):

    #To test if an item starts with a number
    number_regex = "^[1-9]"
    #if an item does have number sepreate it with the rest
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]
    #iF has no number assume it's one
    else:
        quantity_required = 1
        snack_name = choice
    #Removing space
    snack_name = snack_name.strip()
    return quantity_required, snack_name

def collate_orders():
    Valid_snacks = [["Popcorn", "p", "corn", "(1"], ["M&M", "mms", "m", "(2"],
                ["Pita Chips", "chips", "pc", "pita", "c", "(3"], ["Water", "w", "(4"],
                ["Orange Juice", "oj", "(5"], ["x", "exit", "(6"]]
#valid options
    valid_yes_no_answer = [["y", "yes"], ["n", "no"]]
    snack_order = []
    max_number_of_snacks = 4
    option = ""
    while option != "X":
        snack = input("what snacks do you want - qty then item"
                      "eg: 2 popcorn or enter X to stop ordering: ").lower()
        snack = split_orders(snack)
        quantity = snack[0]
        if quantity > max_number_of_snacks:
            print("Sorry the max anount you can order is 4")
        else:
            snack = snack[1]
            option = get_choice(snack, Valid_snacks)
            if option == "X":
                break
            elif option is not None:   #Filters out the invalid choices
                snack_order.append([quantity, option])
    return snack_order


def clac_tickets_price(ticket_age):
    Children_age = range(12, 16)
    Standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    Retired_price = 6.5

    if ticket_age in Children_age:
     price = child_price
    elif ticket_age in Standard_age:
     price = standard_price
    else:
     price = Retired_price

    return price
#The ticket holder's name can't be blank
def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("Please enter an integer(a whole number not a decimal")


#Interger checker(for age)
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question).title()

        # If the name is blank, show the error message
        if not response.isalpha():
            print("You can't leave this blank")
        else:
            return response



def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"There are {maximum - sold} tickets left")
    else:
        print("You have only one ticket left")

def check_valid_age(max_age, min_age):
    #confirm again the age, just to fix the error
    valid_age = number_checker(f"Please confirm {name}'s age: ")
    if valid_age < min_age:
        print(f"sorry {name} is too young for this movie")
        return None
    else:
        while not valid_age <= max_age:
            valid_age = number_checker(f"at {valid_age} {name} is very old, please re-enter {name}'s age")
        return valid_age

def check_valid_payment_method():
    ask_payment_method = input("how do you want to pay: ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_method)
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
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

#store surcharge mutiplier
surcharge_mult_list = []

# Lists to store summary data
# heading orders match the lists in the snack_lists and master_lists above
summary_headings = ["Popcorn", "M&M", "Pita Chips", "Water", "Orange Juice",
                    "Snack profit", "Ticket profit", "Total profit"]
# Empty list to hold the summary data above
summary_data = []

# Dictionary to hold summary data
summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}

#Data frame dictionary
movie_data_dict = {'name': all_name,
                   'tickets': all_tickets,
                    "Popcorn": popcorn,
                    "Water" : water,
                    "Pita Chips" : pita_chips,
                    "M&M" : mms,
                    "Orange Juice" : orange_juice,
                    "Surcharge Multiplier": surcharge_mult_list
                   }
# Cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&M": 3,
    "Orange Juice": 3.25
}



#Did the user used the proggame before, if no give them the instructions

#Loop to get tickets detail
snack_profit_margin = .2
Surcharge_rate = .05
min_age = 12
max_age = 110
Max_tickets = 5
ticket_cost = 5.00
name = ""
ticket_count = 0
ticket_profit = 0
surcharge = 0


while name != "X" and ticket_count < Max_tickets:
     check_max_tickets(Max_tickets, ticket_count)
     #Get details and name
     name = not_blank("Enter the name of the ticket holder: ").title()
     if name == "X":
        break
     else:
        age = check_valid_age(max_age, min_age)
        if not age:
            continue # restarts the get ticket loop
        else:
            ticket_count += 1
            #Claculate ticket price
            ticket_price = clac_tickets_price(age)
            print(f"for {name} the ticket price is {ticket_price:,.2f}")


            #add ticket price and name to list
            all_name.append(name)
            all_tickets.append(ticket_price)

            # Claculate ticket profit and added it to running total
            ticket_profit += (ticket_price - ticket_cost)

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
            while not payment_method:
                payment_method = check_valid_payment_method()

            if payment_method == "Credit Card":
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
    movie_frames["tickets"] + \
    movie_frames["Popcorn"] * price_dict["Popcorn"] + \
    movie_frames["Water" ] * price_dict["Water" ] + \
    movie_frames["Pita chips" ] * price_dict["Pita chips" ] + \
    movie_frames["m&m" ] * price_dict["m&m" ] + \
    movie_frames["orange juice" ] * price_dict["orange juice" ]

movie_frames["Surcharge"] = \
     movie_frames["Sub Total"] * movie_frames["Surcharge Multiplier"]
movie_frames["Total"] = movie_frames["Sub Total"] + movie_frames["Surcharge"]
# Shroten column names
movie_frames = movie_frames.rename(columns={"orange juice": "OJ",
                                            "Pita chips": "Chips",
                                            "Surcharge Multiplier": "SM"})

# Set up summary data frame
# populate snack items from the master snack_lists
for item in snack_lists:
    # Sum item in each snack lists
    summary_data.append(sum(item))
# get snack profit
#Get snack total from panda
snack_total = movie_frames["Snack Cost"].sum()
snack_profit = snack_total * snack_profit_margin
summary_data.append(snack_profit)

# Get ticket profit and added it to the list
summary_data.append(ticket_profit)

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# create summary frame
summary_frames = pandas.DataFrame(summary_data_dict)
summary_frames = summary_frames.set_index("Item")

# Force all coloumns to be printed
pandas.set_option("display.max_columns", None)

# display numbers to 2 decimal places
pandas.set_option("precision", 2)

print(movie_frames)
print()
# For testing ask the user if they want to see all columns
# if no, Just print ticket, sub-total, surcharge and total columns
print()
print("Ticket/snack Information sheet")
#  Referes to an export file - functionality yet to be developed
print("Note: for full details please see the excel file called zzz")
print()
print(movie_frames[["Ticket", "Snack Cost"], "Sub Total", "Surcharge", "Total"])
print()

# Printing the summary frame
print("Snack/profit summary")
print()
print(summary_frames)
# output data to text files
