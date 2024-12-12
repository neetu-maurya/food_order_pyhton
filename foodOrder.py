# Food Ordering System

# Function to display the food menu
def display_menu():
    """Displays the food menu."""
    menus = {
        "Vegetarian": {
            '1': {'name': 'Tawa Chaap', 'price': 100},
            '2': {'name': 'Dal Makhani', 'price': 140},
            '3': {'name': 'Kadai Paneer', 'price': 150},
            '4': {'name': 'Palak Paneer', 'price': 100},
            '5': {'name': 'Mixed Kofta', 'price': 105},
            '6': {'name': 'Dum Aloo', 'price': 85},
            '7': {'name': 'Malai Kofta', 'price': 140},
        },
        "Tandoori Veg": {
            '1': {'name': 'Harabhara Kabab', 'price': 90},
            '2': {'name': 'Tandoori Aloo', 'price': 100},
            '3': {'name': 'Malai Chaap', 'price': 120},
            '4': {'name': 'Mushroom Tikka', 'price': 120},
            '5': {'name': 'Pudhina Tikka', 'price': 150},
        },
        "Tandoori Non-Veg": {
            '1': {'name': 'Shahi Murg (Tandoori)', 'price': 180},
            '2': {'name': 'Shahi Tikka', 'price': 110},
            '3': {'name': 'Chicken Tikka', 'price': 290},
            '4': {'name': 'Afghani Chicken', 'price': 120},
        },
        "Momo": {
            '1': {'name': 'Chicken Momo', 'price': 110},
            '2': {'name': 'Veg Momo', 'price': 90},
            '3': {'name': 'Chicken Fry Momo', 'price': 150},
            '4': {'name': 'Veg Fry Momo', 'price': 140},
        },
    }

    print("\nFood Menu:")
    print("1. Vegetarian\n2. Tandoori Veg\n3. Tandoori Non-Veg\n4. Momo")
    category_choice = input("Enter your choice (1-4) or type 'back' to return to the main menu: ")

    if category_choice == 'back':
        return None
    elif category_choice in ['1', '2', '3', '4']:
        categories = list(menus.keys())
        selected_category = categories[int(category_choice) - 1]
        print(f"\n{selected_category} Menu:")
        for key, item in menus[selected_category].items():
            print(f"{key}. {item['name']} - Rs{item['price']:.2f}")
        return menus[selected_category]
    else:
        print("Invalid choice. Please try again.")
        return None


def take_order(menu):
    """Takes the user's order."""
    order = []
    print("\nEnter the item number to add to your order. Type 'done' when finished.")
    while True:
        choice = input("Choose an item (or type 'done' or 'menu' to return to the menu): ")
        if choice.lower() == 'done':
            break
        elif choice.lower() == 'menu':
            return 'menu'
        elif choice in menu:
            try:
                quantity = int(input(f"Enter the quantity for {menu[choice]['name']}: "))
                if quantity > 0:
                    order.append({
                        'name': menu[choice]['name'],
                        'price': menu[choice]['price'],
                        'quantity': quantity,
                        'total_price': menu[choice]['price'] * quantity
                    })
                    print(f"Added {quantity} x {menu[choice]['name']} to your order.")
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print("Invalid choice. Please try again.")
    return order


def calculate_total(order):
    """Calculates the total cost of the order."""
    total = sum(item['total_price'] for item in order)
    return total


def display_order_summary(order, total):
    """Displays the summary of the order."""
    print("\nOrder Summary:")
    if not order:
        print("No items ordered.")
    else:
        for item in order:
            print(f"- {item['quantity']} x {item['name']} - Rs{item['total_price']:.2f}")
        print(f"\nTotal: Rs{total:.2f}")


# Main program
if __name__ == "__main__":
    print("Welcome to the Food Ordering System!")
    while True:
        menu = display_menu()
        if menu:
            while True:
                order = take_order(menu)
                if order == 'menu':
                    break
                total = calculate_total(order)
                display_order_summary(order, total)
                print("\nThank you for your order!")
                exit()
        else:
            print("Returning to the main menu...")
