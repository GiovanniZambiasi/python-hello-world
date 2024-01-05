

class Book():

    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self) -> str:   # Implemnents conversion from this to string
        return f"{self.title} by {self.author}"
    
    def __len__(self):          # Implementation for the len method on objects of this type
        return self.pages
    
    def __del__(self):          # Destructor
        print(f"'{self}' has been deleted")    

book = Book("Navepedia", "Gionave", 450)
print(book)

book_as_string = str(book)
print(book_as_string)

print(f"Length of '{book}' is {len(book)}")

del(book)
