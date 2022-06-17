#list = used to stoe multiple items ina single variable

food = ["pizza" , "hamburguer" , "hotdog" , "spaghetti"]

#changing one of the elements
food[0] = "sushi"

#adding an elemento to the list
food.append("ice cream")
#removing an element\
food.remove("hotdog")
#removes the item at the given index from the list and returns the remoed item
removed_element = food.pop(3)

print(removed_element)

print(food[0])