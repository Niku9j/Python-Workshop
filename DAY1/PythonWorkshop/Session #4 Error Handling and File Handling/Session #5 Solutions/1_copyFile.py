'''
Write a function that takes two file names, file1 and file2 as input. The function should
read the contents of the file file1 line by line and should write them to another file file2
after adding a newline at the end of each line.
'''

def fileCopy(file1,file2):
    '''
    Objective: To copy the content of file1 to file2 line by line while adding
    a newline at the end of each line
    Input Parameters: file1,file2 : file names - string value
    Return Value: None
    '''
    '''
    Approach:
    Read input from file1, line by line and copy to file2 after adding newline
    at the end of each line until null string is returned on reading
    '''
    f1 = open(file1, 'r')
    f2 = open(file2, 'w')
    line = f1.readline()
    while line != '':
        f2.write(line+'\n') #write the line from f1 with additional newline
        line = f1.readline()
    f1.close()
    f2.close()

def main():
   '''
    Objective: To call function fileCopy to copy contents in a file to another file.
    Input Parameter: None
    Return Value: None
   '''
   fileName1=input('Enter the source file name: ')
   fileName2=input('Enter the destination file name : ')
   fileCopy(fileName1, fileName2)
   

if __name__ == '__main__':
   main()
    
