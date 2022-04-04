#Trailing method and extracting and testing the first character is a string and to see if it's a number
#All i have down in this proggame is splitting the first character from the rest

string = [
    "Popcorn",  #string with no number
    "2 pc",  #String with a space and a valid number
    "1.50J",  #String with preceding decimal
    "40J",  #string with preceding interger with no space
    "12Chips",
     ]
for item in string:
    if item[0].isdigit():  #test to see if the fir cha is a digit
        if item[1].isdigit():  #if yes Also about the second cha if it's a digit
            quantity = int(item[0]+item[1])  #if both of them are digit join them
            snack = item[2:]  #and split the rest of the string off at item 2
        else:
            quantity = int(item[0])  #if only first cha is a digit
            snack = item[1:]  #split the rest of string off at item 1
    else:  #if no digit is found
        quantity = 1  #assume the number is 1
        snack = item
    print(f"Quantity is {quantity}")
    print(f"Your snack is {snack}")
