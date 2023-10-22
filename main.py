def searchbook(self):
        self.searchbook=input("Enter the Book Name/Author Name/Genre !!! ")
        for i in self.bookdata:
            if self.searchbook in i:
                print(f"Book : {i[0]} ..... Author : {i[1]} ...... Genre : {i[3]}")
        return "Sorry !!! We can not find related Book !"
    def checkin(self):
        self.nameofcbook=input("Which book did you checked out !!!")
        userdata=pd.read_csv("data.csv")
        userlistdata=userdata.values.tolist()
        for i in userlistdata:
            if i[4] == True:
                for j in self.bookuser:
                    if i[0] in j and self.nameofcbook in j:
                        print("Sure !!! Thanks for returning the book ! Hope you enjoyed reading it ! ('-')")
                        self.bookuser.remove(j)
                        return
                else: 
                    print("Sorry !!! That does not match our records !!! ")
    def userRecord(self):
        print("Sure ! Here You Go !!! ")
        userdata=pd.read_csv("data.csv")
        userlistdata=userdata.values.tolist()
        for m in userlistdata:
            if m[4]==True:
                for j in self.bookuser:
                    if m[0] in j:
                        print(f"name : {j[0]} .... book : {j[1]}")
    def Bookall(self):
        print("Here You go !!! ")
        for i in self.bookdata:
            print(f"Book : {i[0]} ..... Author : {i[1]} ...... Genre : {i[3]}")
    def singout(self):
        print("Sure ! Here You Go !!! ")
        print("You Are Signed Out !!!")
        for m in self.datalist:
            if m[4]==True:
                data.loc[data['name'] == m[0], 'login'] = False
                
library = Library()
signed_in = False