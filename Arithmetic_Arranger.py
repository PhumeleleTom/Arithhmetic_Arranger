def arithmetic_arranger(myList, printAnswer=False): #return output
    
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
                print("Error: Numbers cannot be more than four digits.")#return error
                errorCount += 1
                errorFound = True
                
        if((myStringLen_2 > 4) or (myStringLen_2 <= 0)):
                print("Error: Numbers cannot be more than four digits.")#return error
                errorCount += 1
                errorFound = True
                
        try:
            int(myString[0])
        except:
            errorCount += 1
            print("Error: Numbers must only contain digits")#return error
            errorFound = True
            
        try:
            int(myString[2])
        except:
            errorCount += 1
            print("Error: Numbers must only contain digits")#return error
            errorFound = True
            
        if(myString[1] != '+' and myString[1] != '-'):
                print("Error: Operator must be '+' or '-'.")#return error
                errorCount += 1
                errorFound = True

        if(errorCount >= 5):
            print("Error: Too many problems.")#return error

        if(errorFound):
            return
                
        if(myStringLen_0 > myStringLen_2):
            bigNumPos = 0
            smallNumPos = 2
        else:
            bigNumPos = 2
            smallNumPos = 0
        numDiffLen = len(myString[bigNumPos]) - len(myString[smallNumPos])
        totalLen = len(myString[bigNumPos]) + len(myString[smallNumPos])
        outputLine_1 += " "*(totalLen-myStringLen_0)+myString[0]+" "*4
        outputLine_2 += myString[1]+" "*(totalLen-myStringLen_2-1)+myString[2]+" "*4
        outputLine_3 += "-"*(totalLen)+" "*4
        if(printAnswer):
            if(myString[1]=='+'):
                answer = int(myString[0])+int(myString[2])
            else:
                answer = int(myString[0])-int(myString[2])
            outputLine_4 += " "*((totalLen)-len(str(answer)))+str(answer)+" "*4
    output = outputLine_1 + "\n" + outputLine_2 + "\n" + outputLine_3 + "\n" + outputLine_4
    print(output)

if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)


