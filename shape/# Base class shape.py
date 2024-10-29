# Base class shape
class shape(object): # Inherit from base class 
"""
Abstract base class for all ideal shape classes.

    Keyword arguments:
    dimension -- the principle dimension of the shape (default None)
"""
    def __init__(self, dimension:float=None):
        self.shape_type = self.__class__.__name__.capitalize()
        self.dim = dimension
        return
    
    def diameter(self):
        raise Exception("Unimplmented method error.")
    
    def volume(self):
        raise Exception("Unimplmented method error.")
    
    def surface(self):
        raise Exception("Unimplmented method error.")
        
    def type(self):
        return(self.shape_type)

"""
        Returns the formatted name of the shape type. 
        
        This is set automatically, but can be overwritten by setting the attribute shape_type.
        
        :returns: the name of the class, so shapes.cube is a `Cube` shape type
        :rtype: str
"""



# Cube class
class cube(shape): # Inherit from shape 
    def __init__(self, dim:float):
        super().__init__(dim)
        return
    
    def diameter(self):
        return (3 * self.dim**2)**(1/2)
    
    def volume(self):
        return self.dim**3
    
    def surface(self):
        return 6*(self.dim**2)

# If you've done everything correctly then
# you will no longer get an error here...
s = cube(15)

try: 
    print(f"I am a {s.type()}")
    print(f"My volume is {s.volume()}")
except Exception as e:
    print(f"Error: {e}")



# Sphere class
from math import pi
class sphere(shape): # Inherit from shape
    def __init__(self, dim:float):
        super().__init__(dim)
        return

    def diameter(self):
        return self.dim*2

    def volume(self):
        return 4/3*pi*self.dim**3

    def surface(self):
        return 4*pi*self.dim**2

# If you've done everything correctly then
# you will no longer get an error here...
s = sphere(15)

try: 
    print(f"I am a {s.type()}")
    print(f"My volume is {s.volume()}")
except Exception as e:
    print(f"Error: {e}")





# Pyramid class
class pyramid(shape): # Inherit from shape

    has_mummies = True # This is for *all* regular pyramids

    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = 'Regular Pyramid'
        return

    def diameter(self):
        return (self.dim**2 + self.dim**2)**(1/2)

    def height(self):
        return (self.diameter()/2 + self.dim**2)**(1/2)

    def volume(self):
        return self.dim**2 * self.height() / 3

    def surface(self):
        return self.dim**2 + self.dim**2 * 3**(1/2)



# Triangular Pyramid class
class t_pyramid(pyramid): # Inherit from regular pyramid

    has_mummies = False # This is for all triangular pyramids

    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = 'Triangular Pyramid'
        return

    def diameter(self):
        return self.dim

    def height(self):
        # h = sqrt(6)/3 * d
        return 6**(1/2)/3 * self.dim

    def base(self):
        return 3**(1/2)/4 * self.dim**2

    def volume(self):
        return (1/3) * self.base() * self.height()

    def surface(self):
        return 4 * self.base()


for s in ['shape','sphere','cube','pyramid','t_pyramid']:
    if s in locals():
        del(s)
from shapes import *