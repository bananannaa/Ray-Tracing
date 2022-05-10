import math

class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def length_squared(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def normalise(self):
        length = self.length()
        if length == 0:
            raise Exception("length cannot be equal to 0")
        x2 = self.x / length
        y2 = self.y / length
        z2 = self.z / length
        return Vector3(x2, y2, z2)

    def is_normalised(self):
        print(self.length())
        return 0.999999999999 <= self.length() <= 1.000000000001

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __str__(self):
        x = str(self.x)[:5 + str(self.x).find(".")]
        y = str(self.y)[:5 + str(self.y).find(".")]
        z = str(self.z)[:5 + str(self.z).find(".")]
        return f"{x=}, {y=}, {z=}"
