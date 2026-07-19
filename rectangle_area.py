class Rectangle:
    def setValues(self, length, width):
        self.length = length
        self.width = width

    def findArea(self):
        area = self.length * self.width
        print("Area =", area)

r = Rectangle()
r.setValues(10, 5)
r.findArea()