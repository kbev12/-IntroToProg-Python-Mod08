# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KBeverly,8.30.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
        to_string(): utilizes __str__() to return product name and price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        kbeverly,8.31.2022,Modified code to complete assignment 8
    """
    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        #Attributes
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    # -- Properties --
    # product name
    @property  # DON'T USE NAME for this directive!
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value: str):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name_str = value
        else:
            raise Exception("Names cannot be numbers")

    # product_price
    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value: float):  # (setter or mutator)
        if str(value).isnumeric() == True:
            self.__product_price = float(value)
        else:
            raise Exception("Prices must be numbers")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        kbeverly,8.31.2022,Modified code to complete assignment 8
    """
    @staticmethod
    def write_data_to_file(file_name: str, list_of_product_objects: list):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was an error")
            print(e, e.__doc__, type(e), sep="\n")
            raise e
        return success_status


    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :return: (list) of product rows
        """
        list_of_product_rows = []  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was an error")
            print(e, e.__doc__, type(e), sep="\n")
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for performing Input and Output
     methods:
     print_menu_items():
     print_current_list_items(list_of_rows):
     input_product_data():
     changelog: (When,Who,What)
     RRoot,1.1.2030,Created Class
    kbeverly, 8.31.2022, added functions"""

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_products_in_list(list_of_rows: list):
        """ Shows the current products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product():
        """  Gets product and product price to be added to the list

        :return: object with input data
        """
        try:
            product = str(input("What is the product? ")).strip()
            price = float(input("What is the product's price? "))
            print()
            p = Product(product_name=product, product_price=price)
        except Exception as e:
            print(e)
        return p
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts

try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data

    # Display a menu of choices to the user
    while (True):
        # Show user a menu of options
        IO.output_menu_tasks()
        # Get user's menu choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.output_current_products_in_list(lstOfProductObjects)
            continue  # to show the menu
        elif strChoice == '2':
            # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_new_product())
            continue  # to show the menu
        elif strChoice == '3':
            # let user save current data to file
            FileProcessor .write_data_to_file(strFileName, lstOfProductObjects)
            print("Data Saved!")
            continue  # to show the menu
        elif strChoice == '4':
            # Exit Program
            print("Goodbye!")
            break  # by exiting loop
except Exception as e:
    print("There was an error")
    print(e, e.__doc__, type(e), sep='\n')
# Main Body of Script  ---------------------------------------------------- #

