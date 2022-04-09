#Import statement
import re
import pandas


#This function splits snacks into quantity and snack name
#It has to be called before the snack(name) can be exaluated against the valid snacks list
def split_order(choice):
    #regular expression to test and find out if an item strats with a number
    number_regex = "^[1-9]"
    #if an item has a number sepreate the item
