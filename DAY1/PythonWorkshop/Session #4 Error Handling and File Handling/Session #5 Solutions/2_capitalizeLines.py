'''
Program that takes data to be stored in the file file1 as interactive input from the
user until he responds with nothing as input. Each line (or paragraph) taken as input from
the user should be capitalized, and stored in the file file1.
'''

def takeFileInput(file1):
    '''
    Obective: To take data to be stored in the file file1 interactively from the user and capitalize it
    until (s)he responds with empty string
    Input Parameter: file1 : output file name - string value
    Return Value: None
    '''
    '''
    Approach:
    Iteratively, read lines as input from the user until he responds with nothing
    as the input
               1.Capitalize each line
               2.Add a newline at the end before writing it to file file1
    '''
    f=open(file1,'w')
    print("Please enter the data to be stored in file \'", file1, "\' : ")
    line=input()
    while line!='':
        line=line.capitalize()
        f.write(line+'\n') #add a newline after each insertion
        line=input()
    print("The file is successfully created!!")
    f.close()

def main():
   '''
    Objective: To take data to be stored in the file file1 interactively from the user and capitalize it
    until (s)he responds with empty string
    Input Parameter: None
    Return Value: None
   '''
   file=input('Enter the destination file name : ')
   takeFileInput(file)
   

if __name__ == '__main__':
   main()
