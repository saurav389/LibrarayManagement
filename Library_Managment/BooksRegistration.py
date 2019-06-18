import os
import csv
from colorama import Fore,Back,Style
# Creating a class of Book Registration
class BookRegistration():
    Fieldname = ['Bookid','BookName','AuthorName','Cost','Date'] #initializing Fieldnames of Books details
    Filename = "BookDetails.csv" # Creating a Filename data of books details beeb stored
    def get_length(self):
        if not os.path.isfile(self.Filename):
            print(Back.RED + "")
            print(self.Filename, "Not present")
            with open(self.Filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.Fieldname)
                writer.writeheader()
            return 0
        else:
            with open(self.Filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                reader_list = list(reader)
                return len(reader_list)
    def GetDetails(self):
        message = "Registration Page"
        print(Back.BLUE + message.center(24))
        bookid = self.get_length()
        print(Fore.GREEN + "")
        bookname = input("Book Name ")
        authorname = input("Author Name ")
        cost = input("Cost ")
        date = input("Date ")
        bookdata = {
            "bookid":bookid,
            "bookname":bookname,
            "authorname":authorname,
            "cost":cost,
            "date":date
        }
        return bookdata
    def InsertData(self):
        bookdata = self.GetDetails()
        print(Fore.LIGHTMAGENTA_EX + "")
        if not os.path.isfile(self.Filename):
            message= "Error {Filename} not present".format(Filename = self.Filename)
            print(Fore.RED + message.center(30,'_'))
        if bookdata['bookid']>0:
            with open(self.Filename,"a") as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=self.Fieldname)
                writer.writerow({
                    "Bookid": bookdata['bookid'],
                    "BookName": bookdata['bookname'],
                    "AuthorName": bookdata['authorname'],
                    "Cost": bookdata['cost'],
                    "Date": bookdata['date']
                })
        else:
            with open(self.Filename,"w") as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames = self.Fieldname)
                writer.writeheader()
                writer.writerow({
                    "Bookid": bookdata['bookid'],
                    "BookName": bookdata['bookname'],
                    "AuthorName": bookdata['authorname'],
                    "Cost": bookdata['cost'],
                    "Date": bookdata['date']
                })
            print("\n\t Data Inserted")
obj = BookRegistration()
obj.InsertData()


