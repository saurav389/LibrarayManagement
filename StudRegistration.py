import os
import csv
from colorama import Fore,Back,Style
# Stud_details = {'Reg_no','Stud_id','Roll_no','Class','name','FName','Gender','DOB','DOA'}
class StudentRegistration():
    get_file_path = os.path.join(os.path.dirname(__file__),"StudentDetails.csv")
    Filename = get_file_path
    def get_length(self):
        if not os.path.isfile(self.Filename):
            print(Back.RED + "")
            print(self.Filename, "Not present")
            with open(self.Filename, "w",newline='') as csvfile:
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
        studid = self.get_length()
        print(Fore.GREEN + "")
        regno = input("Student Registration no ")
        rollno = input("Student Roll no ")
        clss = input("Class ")
        name = input("Student Name ")
        fName = input("Student Father Name ")
        gender = input("Student Gender ")
        dob = input("Student Date Of Birth ")
        doa = input("Student Date Of Admission ")
        mno = input("Student Mobile nO ")
        email = input("Student Email ")
        studdata = {
            "studid":studid,
            "regno":regno,
            "rollno":rollno,
            "class":clss,
            "name":name,
            "fname":fName,
            "gender":gender,
            "dob":dob,
            "doa":doa,
            "mno":mno,
            "email":email
        }
        return studdata
    def InsertData(self):
        studata = self.GetDetails()
        print(Fore.LIGHTMAGENTA_EX + "")
        if not os.path.isfile(self.Filename):
            message= "Error {Filename} not present".format(Filename = self.Filename)
            print(Fore.RED + message.center(30,'_'))
        if studata['studid']>0:
            with open(self.Filename,"a",newline='') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=self.Fieldname)
                writer.writerow({
                    "Studid": studata['studid'],
                    "Regno": studata['regno'],
                    "Rollno": studata['rollno'],
                    "Class": studata['class'],
                    "Name": studata['name'],
                    "FName": studata['fname'],
                    "Gender": studata['gender'],
                    "DOB": studata['dob'],
                    "DOA": studata['doa'],
                    "MNo": studata['mno'],
                    "Email": studata['email']
                })
        else:
            with open(self.Filename,"w",newline='') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames = self.Fieldname)
                writer.writeheader()
                writer.writerow({
                    "Studid": studata['studid'],
                    "Regno":studata['regno'],
                    "Rollno":studata['rollno'],
                    "Class":studata['class'],
                    "Name":studata['name'],
                    "FName":studata['fname'],
                    "Gender":studata['gender'],
                    "DOB":studata['dob'],
                    "DOA":studata['doa'],
                    "MNo":studata['mno'],
                    "Email":studata['email']
                })
            print("\n\t Data Inserted")


#student = StudentRegistration()
#obj.InsertData()


