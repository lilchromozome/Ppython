import math

class Point:
    '''
    Creates a point object with an x and y coordinate
    Contains various methods for point arithmetic
    - get X and Y values
    - add / iadd
    - sub / isub
    '''
    #gives each point x and y
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    #to string method to print a point
    def __str__(self):
        return f'x: {self.x} y: {self.y}'
    
    #adds the x and y of self and other
    def __add__(self, other):
        sumx = self.x + other.x
        sumy = self.y + other.y
        return Point(sumx, sumy)
    
    #subtracts the x and y of other from self
    def __sub__(self, other):
        difx = self.x - other.x
        dify = self.y - other.y
        return Point(difx, dify)
    
    #adds and substitutes other to self
    def __iadd__(self, other):
        temp = self + other
        self = temp
        return self
    #subtracts and substitues other to self
    def __isub__(self, other):
        temp = self - other
        self = temp
        return self
        
class Vec2D(Point):
    '''
    Inherits methods and attributes from point
    Will create the vector between 2 points, or can be manually set with x and y coord
    - new sub/add returns a vector
    - mul returns dot product
    - norm returns length of vector
    ''' 
    def __init__(self, p1 = 0, p2 = 0):
        #vector between 2 points
        if isinstance(p1, Point) and isinstance(p2, Point):
            self.x = p2.x - p1.x
            self.y = p2.y - p1.y
        #if only 1 parameter as a point
        elif isinstance(p1, Point):
            self.x = p1.x
            self.y = p1.y
        #2 integers 
        else:
            Point.__init__(self, p1, p2)
            
    #adds but returns vector obj
    def __add__(self, other):
        return Vec2D(Point.__add__(self, other))
    
    #subtracts but returns vector obj
    def __sub__(self, other):
        return Vec2D(Point.__sub__(self, other))
    
    #multiply vector or dot product   
    def __mul__(self, other):
        #if other is a point or vector, dot prod
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        #else int multiply vector
        else:
            return Vec2D(other * self.x, other * self.y)
        
    #find magnitude
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    

if __name__=='__main__':
    
    a = Point(2,0)
    b = Point(3,4)
    c = Point(4,9)
    v1 = Vec2D(a,b)     #1,4
    v2 = Vec2D(5,6)
    print(v1-v2, type(v1-v2))
    print(v1 * 3.5)
