#Casey Wenner

#Inorder
def inOrder(n1,n2,n3):
    
    if n1 < n2 & n2 < n3:
        return(True)
    else:
        return(False)

print(inOrder(1, 9, 17))
print(inOrder(-8, 4, 100))
print(inOrder(9, 1, 17))
print(inOrder(1, 17, 9))
