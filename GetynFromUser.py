
def getContinue():
    x= input("Do you Want to continue? (y/n) ")
    while x != "y" and x != "Y" and x != "n" and x != "N" :
         x= input("Do you Want to continue? (y/n) ")
    return(x)


answer = getContinue()
print("The user answered: ", answer)
