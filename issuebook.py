import csv
from colorama import Fore,Back
import os
import datetime
import shutil
from tempfile import NamedTemporaryFile
class search_student():
    today = datetime.date.today()
    text = '{today.day}/{today.month}/{today.year}'.format(today=today)
    get_student_filepath = os.path.join(os.path.dirname(__file__),"StudentDetails.csv")
    student_filename = get_student_filepath
    get_book_filepath = os.path.join(os.path.dirname(__file__),"BookDetails.csv")
    book_filename = get_book_filepath
    get_issuedbook_filepath = os.path.join(os.path.dirname(__file__),"Bookissued.csv")
    issuedbook_filename = get_issuedbook_filepath
    def get_student_details(self):
        message = "Student Details Found \n \t Student id = {Studid}\n\t Name = {name}\n\t class = {Clss}"
        id = input("Student id")
        studdata = {}
        # name = input("Student name")
        with open(self.student_filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Studid'] == id:
                    # print("Student id ", row['Studid'])
                    print(message.format(Studid = row['Studid'], name = row['Name'], Clss = row['Class']))
                    studdata = {
                        "studid": row['Studid'],
                        "regno": row['Regno'],
                        "rollno": row['Rollno'],
                        "class": row['Class'],
                        "name": row['Name'],
                        "fname": row['FName'],
                        "gender": row['Gender'],
                        "dob": row['DOB'],
                        "doa": row['DOA'],
                        "mno": row['MNo'],
                        "email": row['Email']
                    }
                    return studdata
                else:
                    studdata = None
            if studdata is None:
                print(Fore.RED + "Student Data Not Found")
                return studdata

    def get_book_details(self):
        message = "Book Details Found \n \t Book id = {Bookid}\n\t Book Name = {BookName}\n\t Author Name = {AuthorName}"
        Bkid = input("Book id")
        # name = input("Student name")
        bookdata = {}
        with open(self.book_filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Bookid'] is Bkid:
                    # print("Student id ", row['Studid'])
                    print(message.format(Bookid = row['Bookid'], BookName = row['BookName'], AuthorName = row['AuthorName']))
                    bookdata = {
                        "bookid": row['Bookid'],
                        "bookname": row['BookName'],
                        "authorname": row['AuthorName'],
                    }
                    return bookdata
                else:
                    bookdata = None
            if bookdata is None:
                print(Fore.RED + "Books Data Not Found")
                return bookdata
    def get_length(self):
        fieldname = ['SlNo','Studentid','StudentName','RegNo','RollNo','Mno','email','Bookid','BookName','AuthorName','IssueDate','SubmitDate','status']
        if not os.path.isfile(self.issuedbook_filename):
            with open(self.issuedbook_filename,"w",newline='') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=fieldname)
                writer.writeheader()
                #print(0)
            return 0
        else:
            with open(self.issuedbook_filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                reader_list = list(reader)
                #print(1)
                return len(reader_list)
    def check_issued_book(self):
        student_data = self.get_student_details()
        with open(self.issuedbook_filename,"r") as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for data in reader:
                if data['Studentid'] is student_data['studid']:
                    if data['status'] is "True":
                        count=count+1
            return count
    def issue_book(self):
        fieldname = ['SlNo','Studentid','StudentName','RegNo','RollNo','Mno','email','Bookid','BookName','AuthorName','IssueDate','SubmitDate','status']
        SlNo = self.get_length()
        if SlNo > 0:
            student_data = self.get_student_details()
            with open(self.issuedbook_filename, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                stat = 'True'
                for data in reader:
                    if data['Studentid'] is student_data['studid']:
                        if data['status'] == stat:
                            count = count + 1
            if count < 2:
                if student_data is not None:
                    Book_data = self.get_book_details()
                    with open(self.issuedbook_filename,"a",newline='') as csvfile:
                        writer = csv.DictWriter(csvfile,fieldnames=fieldname)
                        #writer.writeheader()
                        writer.writerow({
                            "SlNo":SlNo,
                            "Studentid": student_data['studid'],
                            "StudentName": student_data['name'],
                            "RegNo": student_data['regno'],
                            "RollNo": student_data['rollno'],
                            "Mno": student_data['mno'],
                            "email": student_data['email'],
                            "Bookid": Book_data['bookid'],
                            "BookName": Book_data['bookname'],
                            "AuthorName": Book_data['authorname'],
                            "IssueDate": self.text,
                            "SubmitDate": None,
                            "status": True
                            })
            else:
                print("Not Eligible\nPlease Submit your Previous Issued Book")
                with open(self.issuedbook_filename,"r")as csvfile:
                    reader = csv.DictReader(csvfile)
                    print("Your Issued Books Are\n")
                    for row in reader:
                        print(row['BookName'])
        else:
            # Print("File not present")
            Filename = "Bookissued.csv"
            print(Back.RED + "")
            print(Filename, "Not present")
            with open(Filename, "w",newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldname)
                writer.writeheader()
    def submit_book(self):
        #filename = "Bookissued.csv"
        fieldname = ['SlNo', 'Studentid', 'StudentName', 'RegNo', 'RollNo', 'Mno', 'email', 'Bookid', 'BookName', 'AuthorName', 'IssueDate', 'SubmitDate', 'status']
        temp_file = NamedTemporaryFile(mode ='r+',newline='', delete=False)
        with open(self.issuedbook_filename,"r+") as csvfile, temp_file:
            reader = csv.DictReader(csvfile)
            # Fieldname = ['SlNo', 'Studentid', 'StudentName', 'RegNo', 'RollNo', 'Mno', 'email', 'Bookid', 'BookName','AuthorName', 'IssueDate', 'SubmitDate', 'status']
            writer = csv.DictWriter(temp_file, fieldnames=fieldname)
            writer.writeheader()
            student_data = self.get_student_details()
            book_data = self.get_book_details()
            for row in reader:
                print(Fore.BLUE + '')
                if row['Studentid'] is student_data['studid']:
                    if row['Bookid'] is book_data['bookid']:
                        row['SubmitDate'] = self.text
                        row['status']= False
                        print("BOOK ID ",row['Bookid'],"\nBook Name ",row['BookName'],"\n\n\n\t STATUS ",row['status'])
                writer.writerow(row)
        shutil.move(temp_file.name,self.issuedbook_filename)

#obj = search_student()
#obj.get_student_details()
#obj.get_book_details()
#obj.issue_book()
#obj.submit_book()
#obj.get_length()
