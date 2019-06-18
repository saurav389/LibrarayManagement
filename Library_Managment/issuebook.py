import csv
from colorama import Fore,Back
import os
import datetime
import shutil
from tempfile import NamedTemporaryFile
class search_student():
    def get_student_details(self):
        message = "Student Details Found \n \t Student id = {Studid}\n\t Name = {name}\n\t class = {Clss}"
        id = input("Student id")
        studdata = {}
        # name = input("Student name")
        with open("StudentDetails.csv", "r") as csvfile:
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
        with open("BookDetails.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Bookid'] == Bkid:
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
        Filename = "Bookissued.csv"
        # fieldname = ['SlNo','Studentid', 'StudentName', 'RegNo', 'RollNo', 'Mno', 'email', 'Bookid', 'BookName', 'AuthorName','IssueDate', 'SubmitDate']
        if not os.path.isfile(Filename):
            return 0
        else:
            with open(Filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                reader_list = list(reader)
                return len(reader_list)
    def check_issued_book(self):
        student_data = self.get_student_details()
        with open("Bookissued.csv","r") as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for data in reader:
                if data['Studentid'] is student_data['studid']:
                    count=count+1
            return count
    def issue_book(self):
        today = datetime.date.today()
        text = '{today.day}/{today.month}/{today.year}'.format(today=today)
        fieldname = ['SlNo','Studentid','StudentName','RegNo','RollNo','Mno','email','Bookid','BookName','AuthorName','IssueDate','SubmitDate','status']
        SlNo = self.get_length()
        if SlNo > 0:
            student_data = self.get_student_details()
            with open("Bookissued.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                for data in reader:
                    if data['Studentid'] is student_data['studid']:
                        count = count + 1
            if count < 2:
                if student_data is not None:
                    Book_data = self.get_book_details()
                    with open("Bookissued.csv","a",newline='') as csvfile:
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
                            "IssueDate": text,
                            "SubmitDate": 30,
                            "status":"issued"
                            })
            else:
                print("Not Eligible\nPlease Submit your Previous Issued Book")
        else:
            # Print("File not present")
            Filename = "Bookissued.csv"
            print(Back.RED + "")
            print(Filename, "Not present")
            with open(Filename, "w",newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldname)
                writer.writeheader()
    def submit_book(self):
        filename = "Bookissued.csv"
        fieldname = ['SlNo', 'Studentid', 'StudentName', 'RegNo', 'RollNo', 'Mno', 'email', 'Bookid', 'BookName', 'AuthorName', 'IssueDate', 'SubmitDate', 'status']
        temp_file = NamedTemporaryFile(delete=False)
        status = "submit"
        with open(filename,"r+") as csvfile, temp_file:
            reader = csv.DictReader(csvfile)
            # Fieldname = ['SlNo', 'Studentid', 'StudentName', 'RegNo', 'RollNo', 'Mno', 'email', 'Bookid', 'BookName','AuthorName', 'IssueDate', 'SubmitDate', 'status']
            writer = csv.DictWriter(temp_file, fieldnames=fieldname)
            writer.writeheader()
            student_data = self.get_student_details()
            book_data = self.get_book_details()
            #status = "submit"
            for row in reader:
                print(Fore.BLUE + '')
                if row['Studentid'] is student_data['studid']:
                    if row['Bookid'] is book_data['bookid']:
                        row['status']= True
                print(row)
                writer.writerow(row)
            shutil.move(temp_file.name,filename)

obj = search_student()
#obj.get_student_details()
#obj.get_book_details()
#obj.issue_book()
obj.submit_book()