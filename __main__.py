from argparse import ArgumentParser
import csv
from StudRegistration import StudentRegistration
from BooksRegistration import BookRegistration
from issuebook import search_student
import os
student = StudentRegistration()
book = BookRegistration()
issue = search_student
file_item_path = os.path.join(os.path.dirname(__file__),"Bookissued.csv")
filename= file_item_path
choise = input(" y = Yes / N = No for MAIN MENU")
while choise is "y":
    message = "MAIN MENU"
    print(message.center(30,'*'))
    m1 = "1. STUDENT REGISTRATION"
    m2 = "2. BOOK REGISTRATION"
    m3 = "3. ISSUE BOOK"
    m4 = "4. SUBMIT BOOK"
    m5 = "5. CHECK ISSUED BOOK"
    m6 = "6. PRINT REGISTERED STUDENT DETAILS"
    m7 = "7. PRINT REGISTERED BOOK DETAILS"
    print("\n",m1,"\n",m2,"\n",m3,"\n",m4,"\n",m5,"\n",m6,"\n",m7)
    option = int(input("Please choose the option"))
    if(option<8):
        if option is 1:
            student.InsertData()
        elif option is 2:
            book.InsertData()
        elif option is 3:
            #SlNo = issue.get_length("self")
            issue.issue_book("self")
        elif option is 4:
            issue.submit_book("self")
        elif option is 5:
            mes="Book id = {Bookid}\nBook Name = {BookName}"
            with open(filename,"r")as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(mes.format(Bookid=row['Bookid'],BookName=row['BookName']))
                    #print(row['Bookid'])
                    #print(row['BookName'])
        elif option is 6:
            issue.get_student_details("self")
        elif option is 7:
            issue.get_book_details("self")
    else:
        print("invalid input\nPlease input less than 7")
    choise = input("Do you want to continue y = Yes / N = No")
