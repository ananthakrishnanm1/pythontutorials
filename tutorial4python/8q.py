class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost
    
    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: {self.cost}")

book = Book()
book.get_details("Python Basics", "John Doe", 29.99)
book.print_details()
