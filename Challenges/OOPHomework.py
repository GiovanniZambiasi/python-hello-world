import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        distance_vector = (self.coor1[0] - self.coor2[0], self.coor1[1] - self.coor2[1])
        return math.sqrt(distance_vector[0]**2 + distance_vector[1]**2)
    
    def slope(self):
        distance_vector = (self.coor1[0] - self.coor2[0], self.coor1[1] - self.coor2[1])
        return distance_vector[1]/distance_vector[0]
# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())