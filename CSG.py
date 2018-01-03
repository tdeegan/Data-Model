from abc import ABC, abstractmethod
import tkinter as tk
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

def draw_pixel(canvas, x, y, color='#000000'):
    """Draw a pixel at (x,y) on the given canvas"""
    x1, y1 = x - 1, y - 1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color)
    
def main(shape):

    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    
    shape.draw(canvas)

    tk.mainloop()
    
    
class Drawable(ABC):
    
    @abstractmethod
    def __contains__(self,x):
        raise NotImplementedError("Need to implement __contains__ in subclass of abstract class")
    
    def __and__(self,other):
        return Intersection(self,other)
    
    def __or__(self,other):
        return Union(self,other)
    
    def __sub__(self,other):
        return Difference(self,other)
    
    def draw(self,canvas): #canvas is an instance of tkinter.Canvas, happy_face is self
        
        for i in range(-250,250):
            for j in range(-250, 250):
                if((i,j) in self):
                    x = i + CANVAS_WIDTH / 2
                    y = -j + ((CANVAS_HEIGHT) / 2)
                    draw_pixel(canvas,x,y)

    
class Circle(Drawable):
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        
    def __contains__(self,other): 
        
        d = math.sqrt(((other[0] - self.x)**2) + ((other[1] - self.y)**2))
        
        if d <= self.r:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"a Circle with radius {self.r} and center ({self.x},{self.y})"
    
class Rectangle(Drawable):
    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
            
    def __contains__(self,point): 
        
        if((self.x0 <= point[0] <= self.x1) and (self.y0 <= point[1] <= self.y1)):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"a Rectangle with lower-left corner ({self.x0},{self.y0}) and upper right corner ({self.x1},{self.y1})"
        
    
    
class Intersection(Drawable):
    def __init__(self,shape1,shape2):
        self.shape1 = shape1
        self.shape2 = shape2
            
    def __contains__(self,point):
        
        if(self.shape1.__contains__(point) and self.shape2.__contains__(point)):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"This is the intersection of {self.shape1} and {self.shape2}"

class Union(Drawable):
    def __init__(self,shape1,shape2):
        self.shape1 = shape1
        self.shape2 = shape2
            
    def __contains__(self,point):
            
        if(self.shape1.__contains__(point) or self.shape2.__contains__(point)):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"This is the union of {self.shape1} and {self.shape2}"
            
class Difference(Drawable):
    def __init__(self,shape1,shape2):
        self.shape1 = shape1
        self.shape2 = shape2
            
    def __contains__(self,point):
            
        if(self.shape1.__contains__(point) and (self.shape2.__contains__(point)==False)):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"This is the difference between {self.shape1} and {self.shape2}"
    

if __name__ == '__main__':
    # Create a "happy" face by subtracting two eyes and a mouth from a head
    head = Circle(0, 0, 200)
    left_eye = Circle(-70, 100, 20)
    right_eye = Circle(70, 100, 20)
    mouth = Rectangle(-90, -80, 90, -60)
    happy_face = head - left_eye - right_eye - mouth

    # Draw the happy face
    main(happy_face)
    
    board = Rectangle(-250,-250,250,250)
    r1 = Rectangle(-250,125,-125,250)
    r2 = Rectangle(0,125,125,250)
    r3 = Rectangle(-125,0,0,125)
    r4 = Rectangle(125,0,250,125)
    r5 = Rectangle(-250,-125,-125,0)
    r6 = Rectangle(0,-125,125,0)
    r7 = Rectangle(-125,-250,0,-125)
    r8 = Rectangle(125,-250,250,-125)

    print('Checkers board coming...')
    
    checkers_board = board - r1 - r2 - r3 - r4 - r5 - r6 - r7 - r8
    
    main(checkers_board)
    
    










    
    
    
    
