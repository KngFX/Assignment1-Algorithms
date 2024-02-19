#Fahad Shafiq
#100831055
import time #Importing library for time

StartT=time.time() #Timer starts

def main(): #Main Function

    def readFILE(my_file):  #Takes file and returns each line in an array
        data=[]
        with open(my_file) as file:
            for line in file:
                data.append([line.strip()])
        return data

    product_data=readFILE("product_data.txt") #Open and read file
    Products=[] #Initialize array

    for i in range(len(product_data)): #Split each line into an array
        Products.append((product_data[i])[0].split(','))

    def insertionBYprice(Products):  #Use Insertion sort algorithm sort by price
        for index in range(1, len(Products)):
            product=Products[index]
            price=float(product[2])  #Convert price to float for comparison
            position=index-1

            while position>=0 and float(Products[position][2]) > price:  # Move higher price product to the right
                Products[position+1]=Products[position]
                position-=1
            Products[position+1]=product

        return Products

    def insert(id, name, price, category): #Insert item Function
        Products.append([id, name, price, category])
        print('Item inserted!')

    def update(id, name, price, category): #Update item Function
        for i in range(len(Products)):
            if int(Products[i][0])==int(id):
                Products[i]=[id, name, price, category]
        print(f"Item {id} successfully updated")

    def delete(id): #Delete item by ID
        prod_id=0
        for i in range(len(Products)):
            if int(Products[i][0])==int(id):
                prod_id=i
        Products.pop(prod_id)
        print(f"Item {id} successfully deleted")

    def searchNAME(name): #Search item by Name
        for i in range(len(Products)):
            if (Products[i][1]).strip().lower()==name.lower():
                print('Item found!')
                print(f"{Products[i][0]}, {Products[i][1]}, {Products[i][2]}, {Products[i][3]}")

    def searchID(id): #Search item by ID
        for i in range(len(Products)):
            if int(Products[i][0])==int(id):
                print('Item found!')
                print(f"{Products[i][0]}, {Products[i][1]}, {Products[i][2]}, {Products[i][3]}")

    insert('89120', "Asus Gaming Laptop AGLXW", '2199', "Electronics") #Test insert function
    print('\n')
    update("97895", "Blender KSJHL", "99.99", "Home & Kitchen") #Test update function
    print('\n')
    delete(90291) #Test delete function
    print('\n')
    searchID(25425) #Test Search by ID function
    print('\n')
    searchNAME("Mixer CKVJQ") #Test Search by Name function
    print('\n')
    insertionBYprice(Products) #Sort items

    print("########################## Current List ################################")
    for i in range(len(Products)): #Print List of items sorted
        print(Products[i])
    print("########################################################################")
    print('\n')
    EndT=time.time() #Timer Ends
    print('time taken=',EndT-StartT) #Print time taken
    return 0


main()
