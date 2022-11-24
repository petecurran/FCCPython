class Rectangle:
  """Creates a visual representation of a polygon."""
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __repr__(self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)
  
  def set_width(self,width):
    self.width = width
    return

  def set_height(self,height):
    self.height = height
    return

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2* self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2) **.5)

  def get_picture(self):
    #Reject larger pictures
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    #Create a single line.
    line = ("*"*self.width)+"\n"
    #Multiply by height and return
    shape = line*self.height
    return shape

  def get_amount_inside(self, shape):
    #Find how many full shapes fit top to bottom
    numFitsVertically = self.height // shape.height
    #Find how many full shapes fit side to side.
    numFitsHorizontally = self.width // shape.width
    #Multiply and return
    numFits = numFitsVertically * numFitsHorizontally
    return numFits

class Square(Rectangle):
  """Creates a visual representation of a square."""
  def __init__(self,side):
    super().__init__(side,side)

  def __repr__(self):
    return "Square(side={})".format(self.width)
  
  def set_side(self,side):
    self.width = side
    self.height = side

  def set_width(self,width):
    self.width = width
    self.height = width

  def set_height(self,height):
    self.width = height
    self.height = height
