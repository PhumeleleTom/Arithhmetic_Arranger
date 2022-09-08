def arithmetic_arranger(myList, printAnswer=False):
    
    myListLen = len(myList)
    errorCount = 0
    errorFound = False
    bigNumPos = -1
    smallNumPos = -1
    answer = -1
    outputLine_1 = ""
    outputLine_2 = ""
    outputLine_3 = ""
    outputLine_4 = ""
    output = ""
    
    
    for i in range(myListLen):
        
        myOperation = myList[i]
        myString = myOperation.split(" ")
        myStringLen = len(myString)
        myStringLen_0 = len(myString[0])
        myStringLen_2 = len(myString[2])
        
        if((myStringLen_0 > 4) or (myStringLen_0 <= 0)):
                output += "\nError: Numbers cannot be more than four digits."
                errorCount += 1
                errorFound = True
                
        if((myStringLen_2 > 4) or (myStringLen_2 <= 0)):
                output += "\nError: Numbers cannot be more than four digits."
                errorCount += 1
                errorFound = True
                
        try:
            int(myString[0])
        except:
            errorCount += 1
            output += "\nError: Numbers must only contain digits"
            errorFound = True
            
        try:
            int(myString[2])
        except:
            errorCount += 1
            output += "\nError: Numbers must only contain digits"
            errorFound = True
            
        if(myString[1] != '+' and myString[1] != '-'):
                output += "\nError: Operator must be '+' or '-'."
                errorCount += 1
                errorFound = True

        if(errorCount >= 5):
            output = "Error: Too many problems."

        if(errorFound):
            return output
                
        if(myStringLen_0 > myStringLen_2):
            bigNumPos = 0
            smallNumPos = 2
        else:
            bigNumPos = 2
            smallNumPos = 0
            
        bigNumLen = len(myString[bigNumPos])
        
        outputLine_1 += " "+" "+" "*(bigNumLen-myStringLen_0)+myString[0]+" "*4
        outputLine_2 += myString[1]+" "+" "*(bigNumLen-myStringLen_2)+myString[2]+" "*4
        outputLine_3 += "-"+"-"+"-"*(bigNumLen)+" "*4
        if(printAnswer):
            if(myString[1]=='+'):
                answer = int(myString[0])+int(myString[2])
            else:
                answer = int(myString[0])-int(myString[2])
            outputLine_4 += " "+" "*(bigNumLen-len(str(answer)))+str(answer)+" "*4
            
    output = outputLine_1 + "\n" + outputLine_2 + "\n" + outputLine_3 + "\n" + outputLine_4
    return output

if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))


