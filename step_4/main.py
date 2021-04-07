import book
import author

first_author = author.Author("John", "Doe", "USA")
book = book.Book("All about Phython", 1, author)


book.lend("testUser")