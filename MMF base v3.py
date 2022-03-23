#import statement

#Functions
def check_name(question):
    while True:
        answer = input(question).title()
        if not answer.isalpha():
         print("you can't levave this blank")
        else:
         return answer

#MAin routine

#Did the user used the proggame before, if no give them the instructions

#Loop to get tickets detail
name = ""
count = 0
Max_tickets = 10
while name != "X" and count != Max_tickets:
     question = check_name("what's your name:")
     count += 1
     if Max_tickets-count in range (2,10):
       print(f"you have {Max_tickets - count} tickets left")
     else:
      print("you have only ONE ticket left")
if count < Max_tickets:
    print(f"you have sold {count} tickets and have {Max_tickets-count} tickets left")
else:
    print("you have sold all tickets")


   #Get name(can't be blank)
question = check_name("what's your name")
   #Get age(between 12-110)

   #Get ticket price

   #Ask for snacks

   #Calculate snack price

   #Payment method(sur charge for credit card)

#calculate total files and profit

#PRint details
