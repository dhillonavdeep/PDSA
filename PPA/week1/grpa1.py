def find_Min_Difference(L,P):
    Q=sorted(L)
    start=0
    end=P-1
    min=Q[end]-Q[start]
    while(end<len(Q)):
        if(Q[end]-Q[start]<=min):
            min=Q[end]-Q[start]
        start+=1
        end+=1
    return min
