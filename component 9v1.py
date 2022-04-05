#Based on component 8
#add ticket lists for testing purposes
#Add the ticket list to movie_data_dict
#Create a price dictionary
#Remove the print statements under #print the snack list and replace with sub-total





import pandas

names = ["Rangi", "Manaia", "Talia", "Arhri", "Fetu"]
tickets = [7.5, 10.5, 10.5, 10.5, 6.5]
#Create sepreate list for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
#Put the seprete list above the master list
snacks_lists = [popcorn, mms, pita_chips, water, orange_juice]
#Create a snack dictionary with a lable and then the list for content
movie_data_dict = {
    "Name" : names,
    "popcorn": popcorn,
    "water" : water,
    "Pita chips" : pita_chips,
    "Mms" : mms,
    "orange juice" : orange_juice
}
#cost of each snack
price_dict = {
    "popcorn" : 2.5,
    "water" : 2,
    "Pita chips" : 4.5,
    "Mms" : 3,
    "orange juice" : 3.25
}
#Testing datas:
test_data = [
    [[2, 'popcorn'], [1, 'Pita chips'], [1, 'orange juice']],
    [[]],  #This is empty list for Mania
    [[1, 'water']],
    [[1, 'popcorn'], [1, 'orange juice']],
    [[1, 'Mms'], [1, 'Pita chips'], [3, 'orange juice']]
]
count = 0  #need count to get the index of each snack in the list
for client_order in test_data:
    #Assume no snack have been bough
    for item in snacks_lists:
        item.append(0)

    snack_order = test_data[count]   #Sets snack order to the [ count value of index] item in test data
    count += 1
    for item in snack_order:
        if len(item) > 0:
            to_find = item[1]  #The name of the snack
            amount = item[0]   #The amount of the snacks
            add_list = movie_data_dict[to_find]  #Match the name to the snack menu
            add_list[-1] = amount  #appends the number ordered to the end of the dictionary list of quantities ordered

print()
#Print details
movie_frames = pandas.DataFrame(movie_data_dict)
movie_frames = movie_frames.set_index("Name")  #change reference to names rather than an atual number

movie_frames["Sub totals"] = \
    movie_frames["tickets"] + \
    movie_frames["popcorn"] * price_dict["popcorn"] + \
    movie_frames["water"] * price_dict["water"] + \
    movie_frames["Pita chips"] * price_dict["Pita chips"] + \
    movie_frames["Mms"] * price_dict["Mms"] + \
    movie_frames["orange juice"] * price_dict["orange juice"]

movie_frames = movie_frames.rename(columns={"orange juice": "OJ",
                                            "Pita chips": "Chips"})
print(movie_frames)



