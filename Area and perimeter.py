class shape:
    def __init__(self,radius=None,length=None,breadth=None,side=None):
         self.radius=radius
         self.length=length
         self.breadth=breadth
         self.side=side

    def Circle(self):
             print("Area of the circle:",3.14*self.radius*self.radius)
             print("Perimeter of circle:",2*3.14*self.radius)
    def Rectangle(self):
            print("Area of the rectangle:",self.length*self.breadth)
            print("Perimeter of rectangle:",2*self.length+self.breadth)
    def Square(self):
            print("Area of square:",self.side*self.side)
            print("Perimeter of square:",self.side*4)

obj=shape(10,20,30,40)
obj.Circle()
obj.Rectangle()
obj.Square()
