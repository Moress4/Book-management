books = {
    
}


def show_books():
   if not books:
       print("there is no books!") 
       return
   for idx, (book,details) in enumerate(books.items(), start=1):
       print(f"{idx}. {book}")
       for key, value in details.items():
           print(f"    {key}. {value}")




def add_book():
    try:
        book_m = int(input("How many book you want to add it : "))
    except ValueError:
        print("invalid value")
        return
    for i in range(book_m):
        print(f"Book {i+1}")
        book_name = input("what's name : ")
        books[book_name] = {
        "author" : input("author : "),
        "year" : input("year : "),
        "type" :    input("type: "),
        }
    show_books()

def delete_book():
    show_books()
    try:
        choice = int(input("what is the book you want to delete it : "))
        if 1 <= choice <= len(books):
            book_keys = list(books.keys())
            book_to_delete = book_keys[choice-1]
            del books[book_to_delete]
            print(f"book {book_to_delete} deleted")
    except ValueError:
        print("invalid value, try again later")


while True:
    feedback = input("add book '1', delete book '2', show books '3', end peogrram '4' : ").strip()
    if feedback == "":
        print("your choice is empty, try again")
    elif not feedback.isdigit():
        print('invalid value,please try again')
        continue
    number = int(feedback)


    if number == 1:
        add_book()
    elif number == 2:
        delete_book()
    elif number == 3:
        show_books()
    elif number == 4:
        print('good bye, see you later')
        break
    else:
        print('invalid value')
        continue