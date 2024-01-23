import random
names= input("Write the names by using ,")
names_list= names.split(",")
#print("The list of names are:", names_list)
length=len(names_list)
Choice=random.randint(0,length-1)
print(f"{names_list[Choice]} will pay the bill")