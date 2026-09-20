from abc import ABC, abstractmethod
class Book:
    total_books =0; #initialize class variable to keep track of total books

    def __init__(self,title,author,isbn,price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__price = price #private variable

        self.available = True
        Book.total_books +=1

    def get_price(self):
        return self.__price

    def set_price(self,price):

        if price>0:
            self.__price = price
        else:
            print("Price must be greater than 0")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"you have borrowed {self.title}")

            return True
        else:
            print("book is already borrowed")

            return False
    def return_book(self):

        if not self.available:
            self.available = True
            print(f"you have returned {self.title}")
        else:
            print("book was not borrowed")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Price:${self.__price}")

        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed ")

    def __str__(self):

        return f"{self.title} by {self.author}"

    @classmethod
    def get_total_books(cls):

        return cls.total_books

class Member(ABC):
    def __init__(self,name,member_id,email):
        self.name = name
        self.member_id = member_id

        self.email = email
        self.borrowed_books = []

    def borrow_book(self,book):
        if len(self.borrowed_books)>=self.get_borrow_limit():

            print(f"{self.name} has reached the borrow limit of {self.get_borrow_limit()} books.")
            return 

        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title}")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Email: {self.email}")

        print("Borrowed Books:")

        if len(self.borrowed_books)==0:
            print("No borrowed books")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


    @abstractmethod
    def get_borrow_limit(self):
        pass

    @abstractmethod
    def calculate_fine(self,days_late):
        pass

    
        
class Student(Member):
    def __init__(self,name,member_id,email,course):
        super().__init__(name,member_id,email)
        self.course = course

    def get_borrow_limit(self):
        return 3

    def calculate_fine(self,days_late):
        return days_late * 5
    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")
class Faculty(Member):
    def __init__(self,name,member_id,email,department):
        super().__init__(name,member_id,email)
        self.department = department

    def get_borrow_limit(self):
        return 5

    def calculate_fine(self,days_late):
        return days_late * 2
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    def add_member(self,member):

        self.members.append(member)
        print(f"{member.name} has been added as a member.")

    def search_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_all_books(self):
        print("ALL books in the library:")

        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            book.display_info()

    def display_all_members(self):
        print("All members of the library:")
        if not self.members:
            print("No members found.")
            return
        for member in self.members:
            member.display_info()

    @staticmethod
    def validate_isbn(isbn):
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        return True


library = Library("My Library")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 799)

book2 = Book("OpenAI Guide", "OpenAI", "9781234567890", 499)

library.add_book(book1)
library.add_book(book2)

student1 = Student("rahul", "S001", "rahul@example.com", "Computer Science")

faculty1 = Faculty("Dr. Smith", "F001", "dr.smith@example.com", "Computer Science")

library.add_member(student1)
library.add_member(faculty1)

student1.borrow_book(book1)
student1.borrow_book(book2)

student1.return_book(book1)
faculty1.borrow_book(book1)
faculty1.borrow_book(book2)

library.display_all_books()
library.display_all_members()   
