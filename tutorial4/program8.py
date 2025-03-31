class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0

    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: ${self.cost}")

book = Book()
book.get_details("1984", "George Orwell", 15)
book.print_details()