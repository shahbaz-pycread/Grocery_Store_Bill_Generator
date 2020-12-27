# -*- coding: utf-8 -*-


import random
shop_name = "Shop Mart"
customer_name = input("Customer Name: ")
sum = 0
count=0
item_list = []
item_cost = []
item_quantity = []
while(True):
    item = input("Enter the item name: ")
    userInput = input("Enter the price or press q to quit: ")
    quantity = float(input("Enter Quantity: "))
    if(userInput != 'q'):
        sum = sum + int(userInput)*quantity
        print(f"Total Bill so far {sum}")
        item_list.append(item)
        item_cost.append(userInput)
        item_quantity.append(quantity)
        count = count + 1
        
    else:
        print('Bill Id: ',random.randrange(1,10000000))
        print('Items: ', item_list) 
        print('Price: ', item_cost)
        print('Quantity: ', item_quantity)
        print(f"Total Price: Rs {sum}")
       
        print("Total Item: ", count)
        print(f"Thank you {customer_name}, for shopping with us. Please visit {shop_name} again.")
        break
