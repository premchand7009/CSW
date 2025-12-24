class Book:
    def __init__(self, title, author, ISBN, status="available", no_of_copies=1):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status
        self.no_of_copies = no_of_copies
    def issue_book(self, num_copies):
        if self.status == "available" and num_copies <= self.no_of_copies:
            self.no_of_copies -= num_copies
            if self.no_of_copies == 0:
                self.status = "unavailable"
            print(f"Issued {num_copies} copies of '{self.title}'.")
        else:
            print(f"Cannot issue {num_copies} copies of '{self.title}'. Not enough copies available.")
    def return_book(self, num_copies):
        self.no_of_copies += num_copies
        self.status = "available"
        print(f"Returned {num_copies} copies of '{self.title}'.")

book1 = Book("1984", "George Orwell", "1234567890", no_of_copies=3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", no_of_copies=2)
book1.issue_book(2)
book2.issue_book(3)
book1.return_book(1)
book2.issue_book(1)
print(f"Book: {book1.title}, Copies Available: {book1.no_of_copies}, Status: {book1.status}")
print(f"Book: {book2.title}, Copies Available: {book2.no_of_copies}, Status: {book2.status}")
