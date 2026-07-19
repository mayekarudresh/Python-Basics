class room:
    length = 0.0
    breath = 0.0

    def calculate_area(self):
    print("Area of room =", self.length * self.breath)

    study_room = room()

    study_room.length = 42.5
    study_room.breath = 30.8

    study_room.calculate_area()