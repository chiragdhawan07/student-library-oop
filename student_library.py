# Define a Library class to manage the collection of books
class Library:
    # Initialize the library with a list of books
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    # Display all available books in the library
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)

    # Allow a student to borrow a book if available
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    # Add a returned book back to the library's list
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

# Define a Student class to request and return books
class Student: 
    # Request a book from the library
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
        
    # Return a previously borrowed book to the library
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         
# Main program logic
if __name__ == "__main__":
    # Create a Library object with a list of available books
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    # Create a Student object
    student = Student()
    
    # Continuous loop to interact with the user
    while(True):
        # Show the main menu to the user
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        
        # Ask the user to choose an option
        a = int(input("Enter a choice: "))
        if a == 1:
            # Show list of all available books
            centraLibrary.displayAvailableBooks()
            
        elif a == 2:
             # Borrow a book from the library
            centraLibrary.borrowBook(student.requestBook())
            
        elif a == 3:
            # Return a previously borrowed book
            centraLibrary.returnBook(student.returnBook())
            
        elif a == 4:
             # Exit the program
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
            
        else:
            # Handle invalid input
            print("Invalid Choice!")

        
