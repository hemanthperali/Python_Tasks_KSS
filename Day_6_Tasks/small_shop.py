'''Develop a Python program for a small shop to process customer purchases. Store product
names and prices in a dictionary, items added to the cart in a list, product categories in a set,
and product details using tuples. Create functions to display products, add items to the cart, and
calculate the total bill. Use a recursive function to compute the total price of all items in the cart.
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist).'''


# Small Shop Purchase Processing System

# Dictionary: Store product names and prices
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5,
    "Eraser": 8,
    "Scale": 15
}

# List: Store items added to the cart
cart = []

# Set: Store product categories
categories = {"Stationery", "Writing", "School Supplies"}

# Tuple: Store product details (name, price, category)
product_details = (
    ("Pen", 10, "Writing"),
    ("Notebook", 50, "Stationery"),
    ("Pencil", 5, "Writing"),
    ("Eraser", 8, "Stationery"),
    ("Scale", 15, "School Supplies")
)


# Function to display available products
def display_products():
    print("\n----- Available Products -----")
    for name, price in products.items():
        print(f"{name}: Rs.{price}")

    print("\nProduct Categories:", categories)


# Function to add products to the cart
def add_to_cart():
    try:
        product_name = input("\nEnter product name: ").title()

        # Check whether the product exists
        if product_name not in products:
            raise NameError("Product does not exist!")

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")

        # Store product and quantity in cart
        cart.append((product_name, quantity))

        print(f"{quantity} {product_name}(s) added to cart.")

    except ValueError as e:
        print("ValueError:", e)

    except NameError as e:
        print("NameError:", e)


# Recursive function to calculate total price
def calculate_total(cart, index=0):
    if index == len(cart):
        return 0

    item = cart[index]

    # Check whether cart item has correct data type
    if not isinstance(item, tuple):
        raise TypeError("Cart item must be a tuple!")

    name, quantity = item

    if not isinstance(name, str) or not isinstance(quantity, int):
        raise TypeError("Invalid data type in cart!")

    # Recursive calculation
    return (products[name] * quantity) + calculate_total(
        cart, index + 1
    )


# Function to display the final bill
def display_bill():
    try:
        print("\n========== CUSTOMER BILL ==========")

        if not cart:
            print("Cart is empty!")
            return

        for name, quantity in cart:
            price = products[name]
            print(
                f"{name} x {quantity} = Rs.{price * quantity}"
            )

        total = calculate_total(cart)

        # Demonstrating ZeroDivisionError handling
        average = total / len(cart)

        print("-----------------------------------")
        print("Total Amount: Rs.", total)
        print("Average item cost: Rs.", average)
        print("===================================")

    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero!")

    except TypeError as e:
        print("TypeError:", e)

    except NameError:
        print("NameError: Product name not found!")

    except KeyError:
        print("Error: Product details are missing!")


# Main program
def main():
    while True:
        print("\n===== SMALL SHOP MANAGEMENT =====")
        print("1. Display Products")
        print("2. Add Item to Cart")
        print("3. Calculate Total Bill")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_products()

            elif choice == 2:
                add_to_cart()

            elif choice == 3:
                display_bill()

            elif choice == 4:
                print("Thank you for shopping!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("ValueError: Please enter a valid number.")


# Execute the program
main()
