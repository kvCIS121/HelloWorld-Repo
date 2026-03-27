def decresing_order(n1, n2, n3):
    if n1 > n2:
        if n1 < n3: 
           return[n3,n1,n2]
        else:
            return [n1,n2,n3]
    else:
        if n1 < n3:
            if n2 < n3:
                return [n3,n2,n1]
            else:
                return [n2,n3,n1]
        else:
            return [n2,n1,n3]
        
#print(decresing_order(9,8,7))
#print(decresing_order(7,8,4))
#print(decresing_order(1,2,3))

#   Note: Big takeaways from today's lecture:
#   Use breakpoints to let compiler know where we want to start inspecting code
#   Can highlight over variables to see their value
#   Use Step arrow to go line by line and inspect code