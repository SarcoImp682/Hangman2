pizza = "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
choice = input()
if choice == 'pizza':
    print(pizza)
elif choice == 'salad':
    print(salad)
elif choice == 'soup':
    print(soup)
else:
    print("Sorry, we don't have it in the menu")
