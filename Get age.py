def Get_age(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("please enter an interger (not decimal)")


Age_range = range(12, 111)
age = Get_age("Please enter the ticket holder's age: ")
while age not in Age_range:
    age = Get_age("please enter an interger that's between 12 and 110: ")
print(f"Age = {age}")

