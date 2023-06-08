def CalculateAverage(Count):
    DigitCounter = 1
    i = 0
    TheSum = 0
    for i in range(Count):
        print("Please input value #", DigitCounter, ":", end = "")
        SumInput = int(input())
        DigitCounter += 1
        TheSum = TheSum + SumInput
    TheAverage = TheSum / (DigitCounter-1)
    return TheAverage

def main():

    try:    
        NumInput = int(input("Average Finder Machine - Input how many #s you want to find the average of:"))
        FinalAverage = CalculateAverage(NumInput)
        print("The Average of the numbers you have put in:", FinalAverage)
    except ValueError:
        print("Your input must only be numbers")
        UserDecision = str(input("Do you want to try again? \nPlease type 'yes' or 'no' "))
        if(UserDecision.upper() == "YES"):
            main()
        elif(UserDecision.upper() == "NO"):
            print("Thank you for trying out the Average Finder Machine!")
        else:
            print("Invalid input! Your input must be either 'yes' or 'no' \n**Machine restarting** \n**Machine back online**", end = "\n")
            main()

main()