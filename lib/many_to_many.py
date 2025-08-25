class Author:
    all_authors = []

    def __init__(self,name):      
        self.name = str(name)
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all_books = []
    def __init__(self,title):
        self.title = str(title)
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

class Contract:
    author = []
    book = []
    date = str
    royalties = int
    all = []

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,value):        
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,value):        
        if not isinstance(value, (int,float)):
            raise Exception("royalties must be a number")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]
