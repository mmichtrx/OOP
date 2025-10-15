import pickle
class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""

    def get_product_details(self):
        self.pid = input("Enter Product ID: ")
        self.pname = input("Enter Product Name: ")
        self.price = int(input("Enter Product Price: "))
        self.description = input("Enter Product Description: ")

    def display_product_info(self):
        print("ProductID: ", self.pid)
        print("ProductName: ", self.pname)
        print("ProductPrice: ", self.price)
        print("ProductDescription: ", self.description)

while 1:
    print("1. Create A Product Object ")
    print("2. Get Product Info ")
    print("3. Display Product ")
    print("4. Write Product Into File ")
    print("5. Read From File, Display Product Info ")
    print("6. Exit ")


    option = int(input("Select A Option: "))

    if option == 1:
        product_obj = Product()

    if option == 2:
        product_obj.get_product_details()

    if option == 3:
        product_obj.display_product_info()

    if option == 4:
        file1 = open("product_inventory.dat", "ab")
        pickle.dump(product_obj, file1)
        f1.close()

    if option == 5:
        file2 = open("product_inventory.dat", "rb")
        while 1:
            try:
                data = pickle.load(file2)
                data.display_product_info()

            except EOFError:
                break

    if option == 6:
        break