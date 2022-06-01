class Library:

    def __init__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price

    def get_book_info(self):
        print(f"Book Name: {self.book_name}, Author Name: {self.author_name}, Price: {self.price}")

book1 = Library("Make Your Bed", "William H. McRaven", "$5")
book1.get_book_info()