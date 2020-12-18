# -*- coding: utf-8 -*-


import random
shop_name = "Shop Mart"
customer_name = input("Customer Name: ")
sum = 0
count=0
item_list = []
item_cost = []
while(True):
    item = input("Enter the item name: ")
    userInput = input("Enter the price or press q to quit: ")
    if(userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Total Bill so far {sum}")
        item_list.append(item)
        item_cost.append(userInput)
        count = count + 1
        
    else:
        print('Bill Id: ',random.randrange(1,10000000))
        print(item_list) 
        print(item_cost)
        print(f"Total Price: Rs {sum}")
       
        print("Total Item: ", count)
        print(f"Thank you {customer_name}, for shopping with us. Please visit {shop_name} again.")
        break
