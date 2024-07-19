import os
import csv
#initializing the csv fie and confirming if it is present in the directory
def initialize_csv():
    if not os.path.exists('product.csv'):
        with open('product.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Price', 'Quantity'])
            print('CSV file created successfully')
    else:
        print("File exists")
#remove the function call to avoid overwriting the existing file
#add function allows the user to add details
def add():
    print("\nProduct Details:")
    id = input('\nEnter product ID: ')#the ID allows the user to edit or remove the the product easily without mentioning the prouct item itself and its details
    name = input('Enter product name: ')
    price = float(input('Enter product price: '))#added float data type
    quantity = int(input('Enter product quantity: '))#added int datatype
    
    with open('product.csv','a') as csvfile:#this opens the product,csv file and allows the user to append it
       writer = csv.writer(csvfile)
       writer.writerow([id,name, price, quantity])
       print("Product added successfully")

       #the function view allows the user to view the product from the csv file
def view():
  with open('product.csv','r') as csvfile:#this allows the easy to read from the file
      reader = csv.reader(csvfile)
      products = list(reader)
        
      if len(products) == 1:
            print("No products available.")#display a message if there are no products.
      else:
            for row in products:
                print(', '.join(row))#empty line

#this function allows the user to make updates on the file
def update():
    id = input('Enter product ID to update: ')#the ID allows the user to select the product and specific detail that they want to change
    found = False
    products = []

    with open('product.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == id:
                found = True
                name = input('Enter new product name: ')
                price = float(input('Enter new product price: '))
                quantity = int(input('Enter new product quantity: '))
                products.append([id, name, price, quantity])
            else:
                products.append(row)#adds product details in a row

            
    if found:
        with open('product.csv','w') as csvfile:#allows the user to make changes of any details of an item
            writer = csv.writer(csvfile)
            writer.writerows(products)
        print('Product updated successfully.')
    else:
        print('Product ID not found.')

#this function allows the user to delete any product from the file by use of the ID
def delete():
    id = input('Enter product ID to delete: ')
    found = False
    products = []

    with open('product.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == id:
                found = True
            else:
                products.append(row)
    
    if found:
        with open('product.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(products)
        print('Product deleted successfully.')
    else:
        print('Product ID not found.')

#this function allows implementation of the code
def main():
    initialize_csv()#calls the function
    
    while True:
        print('\nProduct Management System')
        print('1. Add Product')
        print('2. View Products')
        print('3. Update Product')
        print('4. Delete Product')
        print('5. Exit')
        choice = input('Enter your choice:')
        
        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
          