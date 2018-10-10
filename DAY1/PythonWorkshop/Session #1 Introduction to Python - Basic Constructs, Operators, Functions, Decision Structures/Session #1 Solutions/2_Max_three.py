def max2(n1, n2):
   '''
   Objective: To find maximum of two numbers
   Input Parameters: n1, n2 - numeric values
   Return Value: maximum of n1, n2 - numeric value
   '''
   '''
   Approach:
       Compare two numbers and return the maximum of two numbers.
   '''
   if n1 > n2:
       return n1
   else:
       return n2
       
def max3(n1, n2, n3):
   '''
   Objective: To find maximum of three numbers
   Input Parameters: n1, n2, n3 - numeric values
   Return Value: number - numeric value
   '''
   '''
   Approach:
       Find maximum of two numbers and compare the larger with the third number
       Use function max2
   '''
   return max2(max2(n1, n2), n3)

def main():
   '''
   Objective: To find maximum of three numbers provided as input
   by user
   Input Parameter: None
   Return Value: None
   '''
   n1 = int(input('Enter first number: '))
   n2 = int(input('Enter second number: '))
   n3 = int(input('Enter third number: '))
   maximum = max3(n1, n2, n3)
   print('Maximum number is', maximum)

if __name__ == '__main__':
    main()

