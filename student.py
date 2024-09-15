class student:
    def _init_ (self,Name,Age,DOB,Dep,Blood):
        self.Name=Name
        self.Age=Age
        self.DOB=DOB
        self.Dep=Dep
        self.CGPA=None
        self.Blood =Blood 

    def setCGPA(self,CGPA):
        self.CGPA=CGPA

    def changeDOB(self,C):
        self.DOB=C

    def changeBlood (self,D):
        self.Blood =D

    def displayDetails(self):
        print("Name",self.Name)
        print("Age",self.Age)
        print("DOB",self.DOB)
        print("Dep",self.Dep)
        print("CGPA",self.CGPA)
        print("Blood",self.Blood)
for i in range (3):
    a=input("Enter your Name:")
    b=input("Enter your Age:")
    c=input("Enter your DOB:")
    d=input("Enter your Dep :")
    e=input("Enter your CGPA :")
    f=input("Enter your Blood:")

    obj1=student(a,b,c,d,f)
    obj1.setCGPA(e)
    obj1.displayDetails()
