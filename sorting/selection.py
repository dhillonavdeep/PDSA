def selection_sort(l):
    n=len(l)
    i=0
    if n<1:
        return(l)   
    for i in range(n):
        mpos=i
        for j in range(i,n):
            if l[j]<l[mpos]:
                mpos=j
        (l[i],l[mpos])=(l[mpos],l[i])
    return(l)

x=[3,1,2]
selection_sort(x)
print(x)