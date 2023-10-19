#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

class Book {
public:
    Book(std::string title, std::vector<std::string> pages)
        : title(title), pages(pages) {}
    
    string getTitle() const { 
        return title; 
    }
    
    string getPage(int pageNumber) const {
        if(pageNumber < pages.size()) return pages[pageNumber];
        return "Invalid page number";
    }
    
    int totalPages() const {
        return pages.size();
    }

private:
    string title;
    vector<string> pages;
};

class Library {
public:
    void addBook(Book book) {
        books.push_back(book);
    }

    Book* getBook(string title) {
        for(Book &book : books) {
            if(book.getTitle() == title) return &book;
        }
        return nullptr;
    }

    bool removeBook(string title) {
        for(int i=0; i<books.size(); i++) {
            if(books[i].getTitle() == title) {
                books.erase(books.begin() + i);
                return true;
            }
        }
        return false;
    }

    void detecPlagiarism(int windowSize) {
        const int base = 256;
        const int mod = 1000000007;
        unordered_map<int, pair<int, int>> hashMap;
    }

private:
    vector<Book> books;
};

class User {
public:
    User(string name) : name(name), currentPage(0), activeBook(nullptr) {};

    string getName() const {
        return name;
    }

    void setActiveBook(Book* book) {
        activeBook = book;
        currentPage = readingProgress[book->getTitle()];
    }

    string readCurrentPage() {
        if(!activeBook) {
            return "No active book";
        }
        return activeBook->getPage(currentPage);
    }

    void turnPage() {
        if (activeBook && currentPage < activeBook->totalPages() - 1) {
            currentPage++;
            readingProgress[activeBook->getTitle()] = currentPage;
        }
    }

private:
    string name;
    int currentPage;
    Book *activeBook;
    unordered_map<string, int> readingProgress;
};

class ReadingApp {
public:
    void registerUser(User user) {
        users.push_back(user);
    }

    User* getUser(string name) {
        for(User &user : users) {
            if(user.getName() == name) return &user;
        }
        return nullptr;
    }

    Library* getLibrary() {
        return &library;
    }

private:
    vector<User> users;
    Library library;
};

int main()
{
    ReadingApp app;

    // Add books to library
    app.getLibrary()->addBook(Book("Short Story 1", {"Page 1 text", "Page 2 text"}));
    app.getLibrary()->addBook(Book("Short Story 2", {"Page 1 of story 2", "Page 2 of story 2", "Page 3 of story 2"}));

    // Register a user
    app.registerUser(User("John"));

    User *user = app.getUser("John");
    Book *book = app.getLibrary()->getBook("Short Story 1");

    user->setActiveBook(book);

    std::cout << user->readCurrentPage() << std::endl; // Outputs: Page 1 text
    user->turnPage();
    std::cout << user->readCurrentPage() << std::endl; // Outputs: Page 2 text

    return 0;
}
