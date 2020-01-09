#Let's get recursive

def isPalindrome(P): 
    P = P.lower()
##    P= P.strip(" ")
##    P = P.replace(",","")
##    P = P.replace("!","")
##    P = P.replace(".","")
##    P = P.replace("?","")
##    P = P.replace("-","")
##    P = P.strip(".")
    P = P.strip(" ")
    punctuation=[",","!",".","?","-"," ","","[","]","{","}","'",'"']
    for x in punctuation:
        P=P.strip(x)

    if len(P)==1:
        return True
    elif P[0] ==P[-1]:
        return isPalindrome(P[1:-1])
    return False
        

print(isPalindrome("e"))
print(isPalindrome("racecar"))
print(isPalindrome("A man, a plan, a canal, Panama!"))
print(isPalindrome("No pinot noir on Orion to nip on."))

