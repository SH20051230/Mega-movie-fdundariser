#Use the re method to work out if there is a number attached to the answer or not
#Then sepreate it with the rest of the string
import re



test_strings = [
    "Popcorn",   #string with no number
    "2 pc",   #String with number and space
    "1.50J",  #string with preceeding decimals
    "40J",  #String with preceeding number but no space
     ]
for item in test_strings:
    #To test if an item starts with a number
    number_regex = "^[1-9]"
    #if an item does have number sepreate it with the rest
    if re.match(number_regex, item):
        amount = int(item[0])
        snack = item[1:]
    #iF has no number assume it's one
    else:
        amount = 1
        snack = item
    #Removing space
    snack = snack.strip()
print(f"Amount: {amount}")
print(f"Snack : {snack}")
print(f"length of snack: {len(snack)}")
