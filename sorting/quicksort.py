def quicksort(L,l,r):
    if(r-l<=1):
        return
    (pivot,ub,lb)=(L[l],l+1,l+1)
    for i in range(l+1,r):
        if (L[i]>pivot):
            up= up+1
        else:
            (L[i], L[lb]) = (L[lb], L[i])
            (up,lb) = (up+1,lb+1)
    (L[l],L[lb-1])=(L[lb-1],L[l])
    lower=lower-1
    quicksort(L,l,lb)
    quicksort(l,lb+1,up)
    return(L)
L=(1,2,8,4,5,6)
result=quicksort(L,0,5)
print(result)