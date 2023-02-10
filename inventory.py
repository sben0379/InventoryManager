
#========The beginning of the class==========

# Define Shoe class to contain country, code, product, cost and quantity attributes. Define methods to return the cost
# and quantity of shoes, and to return a string representation of the class.

class Shoe:
    
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========

# Create list to store all Shoe objects

shoe_list = []

#==========Functions outside the class==============

# Define read shoes data function to read data from inventory.txt (skipping first line) and create a Shoe object with
# this data as its attributes. Append the object to shoes_list.

def read_shoes_data():
    
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(", ")
                country, code, product, cost, quantity = data
                cost = float(cost)
                quantity = int(quantity)
                shoe_list.append(Shoe(country, code, product, cost, quantity))
    except:
        print("Error: file not found or corrupted. Please check spelling and try again.")

# Define capture shoes function to input required attributes for Shoe class and create a new Shoe object. Append to
# shoe_list.

def capture_shoes():

    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    with open("Inventory.txt", "a+") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

# Define view all function to iterate over shoe_list and print attributes of each shoe Object.

def view_all():

    print('Country Code Product Cost Quantity\n')
    for shoe in shoe_list:
        print(f'{shoe.country}, {shoe.code}, {shoe.product}, {shoe.cost}, {shoe.quantity}\n')

# Define restock function to find Shoe object with lowest quantity and add to a variable. Ask user if they want to add
# quantity to this variable. Update the quantity in inventory.txt.

def restock():
    
    min_quantity = min(shoe_list, key=lambda x: x.quantity)
    index = shoe_list.index(min_quantity)
    restock = input(f"Do you want to restock {min_quantity.product}? (Enter yes or no)").lower()
    if restock == "yes":
        add_quantity = int(input("Please enter the quantity to be added: "))
        min_quantity.quantity += add_quantity
        shoe_list[index] = min_quantity
        with open("inventory.txt", "w") as file:
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

# Define search shoe function to search for specific shoe code in shoe list and return it.

def search_shoe(code_input):
    
    for shoe in shoe_list:
        if code_input == shoe.code:
            return shoe
        else:
            continue
    return None


# Define value per item function to calculate total value of each Shoe object in list and print.

def value_per_item():
    
    total = 0
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} value: {value}")
        total += value
    print(f"Total value: {total}")

# Define highest qty function to function to find Shoe object with highest quantity and add to a variable. Print that
# this shoe is for sale.

def highest_qty():
    
    max_quantity = max(shoe_list, key=lambda x: x.quantity)
    print(f"{max_quantity} is on sale!")

# #==========Main Menu=============

# Create a menu within a while loop to execute each function according to user input.

read_shoes_data()

while True:

    print("""\n
    V - View all stock
    S - Search stock
    A - Add item
    R - Restock
    T - Total value of stock
    H - Highest stocked item
    \n""")

    menu = input("\nWhat would you like to do?\n").upper()

    if menu == "V":

        view_all()

    elif menu == "S":

        user_input = input("Please enter an item code: ")
        result = search_shoe(user_input)
        if result == None:
            print('\nError: Invalid item code. Please try again.')
        else:
            print('\n' + str(result))
            
    elif menu == "A":
        capture_shoes()

    elif menu == "R":

        restock()

    elif menu == "T":

        value_per_item()

    elif menu == "H":

        highest_qty()

    else:

        print("\nError: invalid input. Please enter an option from the menu provided.")