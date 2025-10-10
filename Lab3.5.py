
class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = 0.0

    def add_book(self):
        self.book_id = input("Enter Book ID: ")
        self.book_title = input("Enter Book Title: ")
        self.author_id = input("Enter Author ID: ")
        self.publisher = input("Enter Publisher: ")
        self.year_of_publication = float(input("Enter Year of Publication: "))
        self.books_borrowed = input("Enter Books Borrowed: ")

    def display_book(self):
        print("BookID:", self.book_id)
        print("Book Title:", self.book_title)
        print("Books Borrowed: ", self.books_borrowed)


class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email_id = ""

class User:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email_id = ""
        self.books_borrowed = ""



    def add_user(self):
        self.user_id = input("Enter User ID: ")
        self.user_name = input("Enter User Name: ")

    def display_user(self):
        print("UserID:", self.user_id)
        print("UserName:", self.user_name)
        print("Said Book has been borrowed.")


s1 = User()
s2 = Book()


s2.add_book()
s2.display_book()

s1.add_user()
s1.display_user()


s1.register_book(b1)
s1.display_user()