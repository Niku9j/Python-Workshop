'''
Define a class Rectangle. The class should contain sides: length and breadth
of the rectangle as the data members. It should support the following methods:
    (a) __init__ for initializing the data members: length and breadth.
    (b) setLength for updating the length of the rectangle.
    (c) setBreadth for updating breadth of the rectangle.
    (d) getLength for retrieving the length of the rectangle.
    (e) getBreadth for retrieving the breadth of the rectangle.
    (f)  area to find the area of the rectangle.
    (g) perimeter for finding perimeter of the rectangle.
'''

class Rectangle:
    
    def __init__(self, length, breadth):
        '''
        Objective: To initialize an object of class Rectangle
        Input Parameters:
            self (implicit parameter) - object of type Rectangle
            length, breadth- numeric value
        Return Value: None
        '''
        self.length=length
        self.breadth=breadth

    def setLength(self, length):
        '''
        Objective: To update the length of the Rectangle object
        Input Parameters:
            self (implicit parameter) - object of type Rectangle
            length- numeric value
        Return Value : None
        '''
        self.length=length
        
    def setBreadth(self, breadth):
        '''
        Objective: To update the breadth of the Rectangle
        Input Parameters:
            self (implicit parameter) - object of type Rectangle
            breadth- numeric value
        Return Value : None
        '''
        self.breadth=breadth

    def getLength(self):
        '''
        Objective: To return the length of the Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value : numeric value
        '''
        return self.length
    
    def getBreadth(self):
        '''
        Objective: To return the breadth of the Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value : numeric value
        '''
        return self.breadth
    
    def area(self):
        '''
        Objective: To return the area of the Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value : numeric value
        '''
        return self.length*self.breadth
    
    def perimeter(self):
        '''
        Objective: To return the perimeter of the Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value : numeric value
        '''
        return 2*(self.length+self.breadth)

    def __str__(self):
        '''
        Objective: To return string representation of object of type
        Rectangle
        Input Parameter:
            self (implicit parameter) - object of type Rectangle
        Return Value: string
        '''
        return 'Length: '+str(self.length)+', Breadth: '+str(self.breadth)

def main():
    '''
    Objective: To create objects of class Rectangle and to perform operations on it
    Input Parameter: None
    Return Value: None
    '''
    length = int(input('Enter length of Rectangle:'))
    breadth = int(input('Enter breadth of Rectangle:'))
    rect = Rectangle(length, breadth)
    print(rect)
    print('Area of Rectangle:  ', rect.area())
    print('Perimeter of Rectangle:  ', rect.perimeter())
    
        
if __name__=='__main__':
    main()

    
    

