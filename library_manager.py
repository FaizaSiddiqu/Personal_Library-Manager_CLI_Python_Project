import json                             # Importing the json module used for data save and load data in json format
import os                              # used to system operations and file handling


data_file = "library.txt"

def load_libaray():
    if os.path.exists(data_file):                          # check if the file exists or not
        with open(data_file, 'r') as file:                  # 'r' open the file in read mode
            return json.load(file)
    else:
        return {}

def save_libaray(library):                         # save the data in json format
    with open(data_file, 'w') as file:                       # 'w' open the file in write mode
        json.dump(library, file)                            # dump the data in json format

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (yes/no): ").lower() == "yes"
    
    new_book = {
    "title": title,
    "author": author,
    "year": year,
    "genre": genre,
    "read": read
}
    
    library.append(new_book)
    save_libaray(library)
    print(f"Book {title} added successfully")
    
def remove_book(library):
    title = input("Enter the titlr of the book you want to remove:")
    initial_length = len(library)
    library = [book for book in library if book["title"].lower() != title]
    if len(library) < initial_length:
        save_libaray(library)
        print(f"Book {title} removed successfully")
    else:
        print(f"Book {title} not found in the libaray")
    
def search_library(library):
    search_by = input("Search by title and auther").lower()
    search_term = input(f"Enter the {search_by}").lower()
    
    results = [book for book in library if search_term in book[search_by].lower()]
    
    if results:
        for book in results:
            status = "read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} -  {status}")
    else:
        print(f"No books found for {search_term} in the {search_by} field")

def display_all_books(library):
    if library:
        for book in library:
            status = "read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} -  {status}")
        else:
            print("The library is empty.")
            
def display_statistics(library):
    total_books = len(library)
    total_read_books = len([book for book in library if book["read"]])
    percentage_read = (total_read_books / total_books) * 100 if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")
    
def main():
    library = load_libaray()
    while True:
        print("\n\n----Library Manager---\n")
        print("Select an option:")
        print("1- Add a Book")
        print("2- Remove a Book")
        print("3- Search the Library")
        print("4- Display all Books")
        print("5- Display Statistics")
        print("6- Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Gooodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()