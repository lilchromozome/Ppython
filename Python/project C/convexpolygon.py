from vec2d import Point as P
from vec2d import Vec2D as V

import math


def orient2d(a, b, c):

    '''
    Parameters
    ----------
        a : Point object
        b : Point object
        c : Point object
        
    Returns
    --------
        Integer 1/1/0
        Returns 1 if points are oriented in the 
        counter clockwise direction -1 if clockwise
        and 0 if collinear
        
    '''

    # Signed area of triangle formed by a,b,c
    s_a = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    
    # Orientation
    result = 1 if s_a > 0 else -1 if s_a < 0 else 0
    
    return result



class ConvexPolygon:
    '''
    This class takes a list of points to form a polygon
    
    Contains various methods to transform the polygon
    - to string
    - rotate
    - get centroid
    - scale
    - overlap (__and__)
    '''
    ''' Convex Polygon class definition'''
    #uses a list of vertices to form a polygon
    def __init__(self, verts):
        self.clockwise = False
        self.counterclockwise = False
        self.nverts = len(verts)        #attributes
        self.verts = verts
        self.edges = []
        
        self.c3verts()
        self.checkAngles()
        
        #check if interior angles smaller than 180 and sides don't intersect, using cross product
    def checkAngles(self):
        for i in range (0, len(self.edges)):
            try:
                cross = self.edges[i].x * self.edges[i+1].y - self.edges[i].y * self.edges[i+1].x
                if cross < 0:
                    self.clockwise = True
                elif cross > 0:
                    self.counterclockwise = True
            except IndexError:
                self.edges[i].x * self.edges[0].y - self.edges[i].y * self.edges[0].x
                if cross < 0:
                    self.clockwise = True
                elif cross > 0:
                    self.counterclockwise = True
        if (self.clockwise == self.counterclockwise):
            raise ValueError('Interior angles must be smaller than 180 degrees and edges must not intersect')

    #creates edges based on verts        
    def c3verts(self):
        #check if polygon has more than 2 sides
        if self.nverts < 3:
            raise ValueError('A convex polygon must have at least 3 vertices')
        for i in range (0, len(self.verts)):
            try:
                self.edges.append(V(self.verts[i+1]-self.verts[i]))
            except IndexError:
                self.edges.append(V(self.verts[0])-self.verts[i])



    #formats ConvexPolygon into a string to print
    def __str__(self):
        nv = 'No. of Vertices: '+str(self.nverts)+'\n'
        vs = "Vertices "+" ".join([v.__str__() + ', ' for v in self.verts]) + '\n'
        es = "Edges "+ " ".join([e.__str__() + ', ' for e in self.edges]) 
        return nv + vs + es

    # Translates a polygon in direction of a vector
    def translate(self, other):
        if isinstance(other, V):
            for vert in self.verts:
                vert.x += other.x
                vert.y += other.y
        else: raise ValueError('Value to translate is not a vector')
        return None
    
    #rotates a polygon by angle (radian) around point pivot
    def rotate(self, angle, pivot = P(0.0)):
        nverts = []
        if isinstance(angle, float) and isinstance(pivot, P):
            for vert in self.verts:
                vx = math.cos(angle) * (vert.x - pivot.x) - math.sin(angle) * (vert.y - pivot.y) + pivot.x
                vy = math.sin(angle) * (vert.x - pivot.x) + math.cos(angle) * (vert.y - pivot.y) + pivot.y
                nverts.append(V(vx, vy))
        else: raise ValueError('Invalid angle or pivot point')
        temp = ConvexPolygon(nverts)
        for i in range(len(self.verts)):
            self.verts[i] = temp.verts[i]
            self.edges[i] = temp.edges[i]
        return None
    
    #returns centroid of polygon, the center of mass
    def get_centroid(self):
        x = 0; y = 0
        for vert in self.verts:
            x += vert.x / self.nverts
            y += vert.y / self.nverts
        p = P(x,y)
        return p
    
    #scales polygon from centroid by sx in x direction adn sy in y direction
    def scale(self, sx = 1, sy = 1):
        if sx > 0 and sy > 0:
            nverts =[]
            centroid = self.get_centroid()
            for vert in self.verts:
                nx = sx * (vert.x - centroid.x) + centroid.x
                ny = sy * (vert.y - centroid.y) + centroid.y
                nverts.append(P(nx,ny))
            temp = ConvexPolygon(nverts)
            for i in range(len(self.verts)):
                self.verts[i] = temp.verts[i]
                self.edges[i] = temp.edges[i]
        else: raise ValueError('Invalid scaling factors')
        return None
    
    #overload &, return true if self and other overlap, otherwise False
    def __and__(self, other):
        i = 0
        result = True
        edges = self.edges + other.edges
        projScalarsA = []
        projScalarsB = []
        for i in range(len(edges)):
            o = V(-1* edges[i].y, edges[i].x)
            for vert in self.verts:
                projScalarsA.append(o * vert)
            for vert in other.verts:
                projScalarsB.append(o * vert)
            if max(projScalarsA) < min(projScalarsB) or max(projScalarsB) < min(projScalarsA):
                result = False
            projScalarsA.clear()
            projScalarsB.clear()
        return result
                
   
if __name__=='__main__':
    
    a = ConvexPolygon([P(1,0), P(0,1), P(-1,0), P(0,-1)])
    b = ConvexPolygon([P(3,0), P(-1,2), P(-1,0)])  
    c = ConvexPolygon([P(6,0), P(2,2), P(2,0)])  
    # b = ConvexPolygon([P(1,6), P(3,4)])
    #c = ConvexPolygon([P(0,0), P(1,1), P(0,1), P(1,0)])
    #d = ConvexPolygon([P(0,0), P(1,1), P(2,2), P(3,3)])
    # a.rotate(math.pi/4.0)
    print(a & b)
    print(a & c)
    print(b & c)
    