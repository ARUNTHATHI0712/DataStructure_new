class student:
    clg='xyz'

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):
        print("student name:",self.name)
        print("student rollno:",self.rollno)
        print("college:",student.clg)
student1=student('xyz009',"amul")
student1.display()

student2=student("xyz7","arun")
student2.display()
