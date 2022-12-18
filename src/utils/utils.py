def print2d_with_index(dp): 
    print ("#", end="\t") 
    for i in range(len(dp[0])): 
        print(i, end="\t")
    """
    print ("\n", end="\t")
    for i in range(len(dp[0])): 
        print ("-", end="\t")
    """
    print () 
    for i in enumerate(dp):
        print (i[0], "|", end="\t")
        for j in i[1]:
            print (j, end="\t") 
        print ()
    print () 

