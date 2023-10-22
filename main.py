import datetime
import csv
import pandas as pd
dtypes = {'name': str, 'email': str, 'password': str, 'signup': bool, 'login': bool}
data=pd.read_csv("data.csv",dtype=dtypes)
class Library:
    def __init__(self):
        print("Welcome to AM Library Management System !!! ")
        self.login=[]
        self.signup=[]
        self.bookdata = [["The Catcher in the Rye", "J.D. Salinger", 10, "Coming-of-Age"],["To Kill a Mockingbird", "Harper Lee", 15, "Legal Drama"],["1984", "George Orwell", 12, "Dystopian"],["Pride and Prejudice", "Jane Austen", 20, "Romance"],["The Great Gatsby", "F. Scott Fitzgerald", 18, "Classic"],["Brave New World", "Aldous Huxley", 10, "Science Fiction"],["The Lord of the Rings", "J.R.R. Tolkien", 25, "Fantasy"],["Moby-Dick", "Herman Melville", 8, "Adventure"],["Jane Eyre", "Charlotte Brontë", 14, "Gothic"],["Crime and Punishment", "Fyodor Dostoevsky", 10, "Psychological Thriller"],["The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 15, "Science Fiction"],["The Chronicles of Narnia", "C.S. Lewis", 22, "Fantasy"],["The Picture of Dorian Gray", "Oscar Wilde", 10, "Gothic"],["Anna Karenina", "Leo Tolstoy", 12, "Romance"],["The Shining", "Stephen King", 16, "Horror"],["The Grapes of Wrath", "John Steinbeck", 11, "Historical Fiction"],["One Hundred Years of Solitude", "Gabriel García Márquez", 10, "Magical Realism"],["The Road", "Cormac McCarthy", 9, "Post-Apocalyptic"],["Frankenstein", "Mary Shelley", 13, "Gothic"],["The Girl with the Dragon Tattoo", "Stieg Larsson", 17, "Mystery"],["The Hobbit", "J.R.R. Tolkien", 20, "Fantasy"],["Wuthering Heights", "Emily Brontë", 10, "Gothic"],["The Martian", "Andy Weir", 14, "Science Fiction"],["The Count of Monte Cristo", "Alexandre Dumas", 18, "Adventure"],["The Handmaid's Tale", "Margaret Atwood", 11, "Dystopian"],["The Alchemist", "Paulo Coelho", 15, "Philosophical"],["Slaughterhouse-Five", "Kurt Vonnegut", 10, "Satire"],["The Odyssey", "Homer", 12, "Epic"],["The Name of the Wind", "Patrick Rothfuss", 16, "Fantasy"],["Gone with the Wind", "Margaret Mitchell", 14, "Historical Romance"],["The Kite Runner", "Khaled Hosseini", 13, "Drama"],["Dracula", "Bram Stoker", 10, "Gothic Horror"],["The Catch-22", "Joseph Heller", 11, "Satire"],["The Hunger Games", "Suzanne Collins", 19, "Dystopian"],["The Book Thief", "Markus Zusak", 15, "Historical Fiction"],["The Giver", "Lois Lowry", 12, "Dystopian"],["The Secret Garden", "Frances Hodgson Burnett", 9, "Children's"],["The Goldfinch", "Donna Tartt", 14, "Mystery"],["The Color Purple", "Alice Walker", 10, "Epistolary"],["The Wind in the Willows", "Kenneth Grahame", 11, "Children's"],["The Adventures of Sherlock Holmes", "Arthur Conan Doyle", 13, "Mystery"],["Little Women", "Louisa May Alcott", 16, "Coming-of-Age"],["The Picture of Dorian Gray", "Oscar Wilde", 12, "Gothic"],["The Night Circus", "Erin Morgenstern", 15, "Fantasy"],["The Road Not Taken", "Robert Frost", 8, "Poetry"],["The Stand", "Stephen King", 17, "Post-Apocalyptic"],["The Bell Jar", "Sylvia Plath", 11, "Autobiographical"],["The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 20, "Science Fiction"],["The Great Expectations", "Charles Dickens", 19, "Classic"],["The Picture of Dorian Gray", "Oscar Wilde", 14, "Gothic"],["The Adventures of Tom Sawyer", "Mark Twain", 18, "Adventure"],["The Stranger", "Albert Camus", 10, "Philosophical"],["The Metamorphosis", "Franz Kafka", 9, "Surreal"],["The Sun Also Rises", "Ernest Hemingway", 15, "Lost Generation"],["The Sound and the Fury", "William Faulkner", 12, "Modernist"],["The Old Man and the Sea", "Ernest Hemingway", 13, "Adventure"],["The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 20, "Science Fiction"],["The Fountainhead", "Ayn Rand", 16, "Philosophical"],["The Little Prince", "Antoine de Saint-Exupéry", 11, "Children's"],["The Stranger", "Albert Camus", 14, "Philosophical"],["The Stand", "Stephen King", 18, "Post-Apocalyptic"],["The Road Less Traveled", "M. Scott Peck", 9, "Self-Help"],["The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 20, "Science Fiction"],["The Hobbit", "J.R.R. Tolkien", 21, "Fantasy"],["The Alchemist", "Paulo Coelho", 22, "Philosophical"],["The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 23, "Science Fiction"],["The Great Gatsby", "F. Scott Fitzgerald", 24, "Classic"],["The Catcher in the Rye", "J.D. Salinger", 25, "Coming-of-Age"],["The Da Vinci Code", "Dan Brown", 26, "Mystery"],["The Lord of the Rings", "J.R.R. Tolkien", 27, "Fantasy"],["The Girl on the Train", "Paula Hawkins", 28, "Mystery"],["The Help", "Kathryn Stockett", 29, "Historical Fiction"],["The Lovely Bones", "Alice Sebold", 30, "Tragedy"],["The Maze Runner", "James Dashner", 31, "Dystopian"],["The Road", "Cormac McCarthy", 32, "Post-Apocalyptic"],["The Catcher in the Rye", "J.D. Salinger", 33, "Coming-of-Age"],["The Hunger Games", "Suzanne Collins", 34, "Dystopian"],["The Da Vinci Code", "Dan Brown", 35, "Mystery"],["The Kite Runner", "Khaled Hosseini", 36, "Drama"],["The Help", "Kathryn Stockett", 37, "Historical Fiction"],["The Lovely Bones", "Alice Sebold", 38, "Tragedy"],["The Maze Runner", "James Dashner", 39, "Dystopian"],["The Girl on the Train", "Paula Hawkins", 40, "Mystery"],["The Secret Garden", "Frances Hodgson Burnett", 41, "Children's"],["The Goldfinch", "Donna Tartt", 42, "Mystery"],["The Color Purple", "Alice Walker", 43, "Epistolary"],["The Wind in the Willows", "Kenneth Grahame", 44, "Children's"],["The Adventures of Sherlock Holmes", "Arthur Conan Doyle", 45, "Mystery"],["Little Women", "Louisa May Alcott", 46, "Coming-of-Age"],["The Night Circus", "Erin Morgenstern", 47, "Fantasy"],["The Road Not Taken", "Robert Frost", 48, "Poetry"],["The Stand", "Stephen King", 49, "Post-Apocalyptic"],["The Bell Jar", "Sylvia Plath", 50, "Autobiographical"]]
        self.signupS=False
        self.loginS=False
        self.issuedata=[]
        self.bookuser=[]
    def Signup(self):
        print("Sign Up here !!! ")
        self.name=input("Enter your Name !!! ")
        self.email=input("Enter your email !!! ")
        self.password=str(input("Enter your password !!! "))
        print("Contratulation !!! You Have Signed Up ! ")
        self.signupS=True
        with open  ("data.csv",mode="a",newline="") as f:
            write=csv.writer(f)
            write.writerow([self.name,self.email,str(self.password),self.signupS,self.loginS])
    def Login(self):
        print("Login Here !!! ")
        self.email=input("Enter your email !!! ")
        self.password=input("Enter your password !!! ")
        dataa=pd.read_csv('data.csv')
        self.datalist=dataa.values.tolist()
        print(self.datalist)
        for row in self.datalist:
            if self.email == row[1] and str(self.password) == str(row[2]):
                self.loginS=True
                print("Login Done")
                dataa.loc[dataa['name'] == row[0], 'login'] = self.loginS
                dataa.to_csv("data.csv",index=False)
                print("Welcome ", row[0], " !!! You Are logged in !!! ")
                return
        print("Incorrect Credential or User does not exist")
        self.Login()
    def book_acquisition(self):
        self.bookName=input("Enter Book Name !!! ")
        self.author=input("Enter Name of Author !!! ")
        self.copies=input("How many Copies !!! ")
        self.genre=input("What is Genre of the book !!! ")
        self.bookdata.append([self.bookName,self.author,self.copies,self.genre])
        print("Great !!! Book has been added to the library !!! ")
    def issuebook(self):
        nameofbook=input("Great !!! Write the name of the book !!! ")
        issuedata=pd.read_csv("data.csv")
        datalist=issuedata.values.tolist()
        for i in self.bookdata:
            if nameofbook in i:
                print("Thats a Great Book !!! ")
                sure = input("Do you want this book ? ")
                if sure == "yes":
                    for m in datalist:
                        if m[4]==True:
                            print(f"{m[0]} !!! The books is Yours now !!!")
                            now=datetime.datetime.now()
                            due=now+datetime.timedelta(days=15)
                            self.bookuser.append([m[0],nameofbook])
                            print("Your due date will be : ",due)
                            return
                        else:
                            print("Error !!!")
                else:
                    print("Ok !!! No problem !!!")
        else:
            print("Sorry !!! But there is no mentioned book !!! ")
            return
library = Library()
while True:
    print("\n=========================")
    print("Welcome to Library System")
    print("=========================")
    if not signed_in:
        print("1. Sign Up")
        print("2. Log In")
    else:
        print(f"Welcome to LMA System !")
        print("3. Issue Book")
        print("4. Search Book")
        print("5. Check In")
        print("6. User Record")
        print("7. View All Books")
        print("8. Sign Out")

    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1' and not signed_in:
        library.Signup()
    elif choice == '2' and not signed_in:
        library.Login()
        signed_in = True
    elif choice == '3' and signed_in:
        library.issuebook()
    elif choice == '4' and signed_in:
        library.searchbook()
    elif choice == '5' and signed_in:
        library.checkin()
    elif choice == '6' and signed_in:
        library.userRecord()
    elif choice == '7' and signed_in:
        library.Bookall()
    elif choice == '8' and signed_in:
        library.singout()
        signed_in = False
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

        