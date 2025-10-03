from book import Book

NB=Book("orula","victor mendivil","2009","libro1")


#print(NB.title)
NB.borrow()

#print(NB.borrowed)

NB.return_book()
print(NB.borrowed)
