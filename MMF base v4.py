#import statement

#Functions
def Get_age(question):
def check_name(question):
    while True:
        answer = input(question).title()
        if not answer.isalpha():
         print("you can't levave this blank")
        else:
         return answer



#Did the user used the proggame before, if no give them the instructions

#Loop to get tickets detail
name = ""
count = 0
Max_tickets = 10
while name != "X" and count != Max_tickets:
     if Max_tickets - count > 1:
         print(f"you have {Max_tickets - count} tickets left")
     else:
      print("you have only ONE ticket left")
    name = check_name("what's your name: ")
    if name == "X":
        break
    else:
        Age_range = range(12, 111)
        age = Get_age("Please enter the ticket holder's age: ")
    while age not in Age_range:
     age = Get_age("please enter an interger that's between 12 and 110: ")
     print(f"Age = {age}")
     count += 1
    if count < Max_tickets:
     print(f"you have sold {count} tickets and have {Max_tickets-count} tickets left")
       else:
     print("you have sold all tickets")
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("please enter an interger (not decimal)")



   #Get name(can't be blank)
question = check_name("what's your name")
   #Get age(between 12-110)

   #Get ticket price

   #Ask for snacks

   #Calculate snack price

   #Payment method(sur charge for credit card)

#calculate total files and profit

#PRint details
