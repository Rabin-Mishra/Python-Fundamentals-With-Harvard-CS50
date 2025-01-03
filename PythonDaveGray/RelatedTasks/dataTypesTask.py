# Grocery list manager (Real Life Task)
'''
Create a program that helps users manage and analyze their shopping list. Utilize various data types to store information about the items in the list.
'''
# Create a shopping list with items and their quantities
shopping_list = {'apple': 5, 'banana': 6, 'orange': 7, 'milk': 1, 'bread': 2}
# Display the original shopping list
print('\n Original Shoping list:')
print(shopping_list)

# update the quantity of the banana
shopping_list['banana'] = 8

# Display the updated shopping list
print('\nUpdated shopping list')
print(shopping_list)

# add an item to the shopping list
shopping_list['chocolate'] = 3
# display the shopping list after adding new item
print('\nShopping List After Adding New Item : ')
print(shopping_list)

# calculate the total number of items on the list
total_items = sum(shopping_list.values())
print(f"Total number of items is {total_items}")

# check if the milk is in the shopping list

has_milk = 'milk' in shopping_list
print('\n Has Milk:', has_milk)

# Remove 'bread' from the list
del shopping_list['bread']

print('\nUpdated shopping list is :')
print(shopping_list)
