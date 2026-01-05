class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} (Pages: {self.pages})"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

    def __gt__(self, other):
        return self.pages > other.pages


b1 = Book("Python", 300)
b2 = Book("C++", 150)

print(b1)
print(len(b1))
print(b1 > b2)
print(repr(b1))
