from phone_book import Book, json

book = Book(r"E:\PythonCode\PhoneBook\book.json")
while True:
    option = int(input("Enter the Number :\n1.Display \n2.Add \n3.Update \n4.Delete "
                       "\n5.Exit to make changes\n"))
    if option == 1:
        book.display()
    if option == 2:
        book.add_entry()
    if option == 3:
        book.update_entry()
    if option == 4:
        book.delete_entry()
    if option == 5:
        break

result_list = []
for data in book.person_list:
    dict1 = {"Name": data.Name, "PhoneNumber": data.PhoneNumber}
    result_list.append(dict1)


with open(r"E:\PythonCode\PhoneBook\book.json", 'w') as out_file:
    json.dump(result_list, out_file)