class Book:

def __init__(self, name, author):

self.name = name

self.author = author

class Bookshelf:

def __init__(self, capacity=20):

self.capacity = capacity

self.names = []

self.authors = []

def add_book(self, book):

if len(self.names) <= self.capacity:

self.names.append(book.name)

self.authors.append(book.author)

print("Книга успешно добавлена")

else:

raise Exception("На полке нет места")

def delete_book(self, book):

for x in self.names:

if x == book.name:

self.names.remove(x)

self.authors.remove(x)

else:

raise Exception("Книга с таким названием и автором не была найдена")

def find_book(self, book):

for x in self.names:

if x == book.name:

print("Книга найдена на полке")

else:

raise Exception("Книга с таким названием и автором не была найдена")

#def show_book(self):

# for x in self.names

shelf = Bookshelf()

book1 = Book("МертвыеДуши", "Гоголь")

book2 = Book("Обломов", "Грибоедов")

book3 = Book("Меч предназначения", "Сапковский")

book4 = Book("Пылающая роза", "Сапковский")

shelf.add_book(book1)

shelf.add_book(book2)

shelf.add_book(book3)

shelf.add_book(book4)
