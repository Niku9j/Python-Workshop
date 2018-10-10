class Shape:

    
    def __init__(self, shapeType):
        '''
        Objective: To initialize object of class Shape
        Input Parameters:
        self (implicit parameter) - object of type Shape
        shapeType - string
        Return Value: None
        '''
        self.shapeType = shapeType

class Rectangle(Shape):

    def __init__(self, length, breadth):
        '''
        Objective: To initialize object of class Rectangle
        Input Parameters:
            self (implicit parameter) - object of type Rectangle
            length, breadth - numeric value
        Return Value: None
        '''
        Shape.__init__(self, 'Rectangle')
        self.length = length
        self.breadth = breadth

    def area(self):
        '''
        Objective: To compute area of the Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value: numeric value
        '''
        #+++ Your Code Here +++


    def perimeter(self):
        '''
        Objective: To compute perimeter of the Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value: numeric value
        '''
        #+++ Your Code Here +++


class Circle(Shape):

    pi = 3.14
    def __init__(self, radius):
        '''
        Objective: To initialize object of class Circle
        Input Parameters:
            self (implicit parameter) - object of type Circle
            radius - numeric value
        Return Value: None
        '''
        #+++ Your Code Here +++

    def area(self):
        '''
        Objective: To compute the area of the Circle
        Input Parameter:
            self (implicit parameter) - object of type Circle
        Return Value: area - numeric value
        '''
        #+++ Your Code Here +++


    def perimeter(self):
        '''
        Objective: To compute the perimeter of the Circle
        Input Parameter:
            self (implicit parameter) - object of type Circle
        Return Value: perimeter - numeric value
        '''
        #+++ Your Code Here +++

def main():
    '''
    Objective: To create objects of class Rectangle and Circle
    and to perform operations on it
    Input Parameter: None
    Return Value: None
    '''
    length = int(input('Enter length of Rectangle:'))
    breadth = int(input('Enter breadth of Rectangle:'))
    rect = Rectangle(length, breadth)
    print('Area of Rectangle:  ', rect.area())
    print('Perimeter of Rectangle:  ', rect.perimeter())

    radius = int(input('\n\nEnter length of Circle:'))
    circ = Circle(radius)
    print('Area of Circle:  ', circ.area())
    print('Perimeter of Circle:  ', circ.perimeter())
    
        
if __name__=='__main__':
    main()
