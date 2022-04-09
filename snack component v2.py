import pandas

names = ["Rangi", "Manaia", "Talia", "Arhri", "Fetu"]
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
#Snack lists
print(f"popcorn: {snacks_lists[0]}")
print(f"Mms: {snacks_lists[1]}")
print(f"Pita chips: {snacks_lists[2]}")
print(f"Water:{snacks_lists[3]} ")
print(f"orange juice: {snacks_lists[4]}")
print()
#Print details
movie_frames = pandas.DataFrame(movie_data_dict)
movie_frames = movie_frames.set_index("Name")  #change reference to names rather than an atual number




