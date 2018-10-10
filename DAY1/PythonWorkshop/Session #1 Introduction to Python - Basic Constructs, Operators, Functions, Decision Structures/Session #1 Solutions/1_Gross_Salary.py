def computeGrossSalary(basicSalary, daPercent, hraPercent):
    '''
    Objective: To compute gross salary given a basic salary, hra% and da%.
    Input Parameters: basicSalary, daPercent, hraPercent - numeric
    Return Value: grossSalary - numeric
    '''
    '''
    Approach: grossSalary is calculated as the sum of basicSalary,
    daPercent of basicSalary and hraPercent of basicSalary
    '''

    grossSalary = basicSalary + basicSalary * (daPercent/100) + basicSalary * (hraPercent/100)
    return grossSalary

def main():
    '''
    Objective: To compute gross salary given a basic salary, grade pay, conveyance charges, hra% and da%.
    Input Parameter: None
    Return Value: None
    '''
    basicSalary = float(input('Enter Basic Salary (in rupees): '))
    daPercent = float(input('percent of da: ')) 
    hraPercent = float(input('Percent of hra:'))
    print('Your Gross Salary ', computeGrossSalary(basicSalary, daPercent, hraPercent))

if __name__ == '__main__':
    main()

