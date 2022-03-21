def merge(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k)=([],0,0,0)
    while(k<m+n):
        if(i==m):
            C.extend(B[j:])
            k=k+(n-j)
        elif(j==n):
            C.extend(A[i:])
            k=k+(m-i)
        elif(A[i]<B[j]):
            C.append(A[i])
            (i,k)=((i+1),(k+1))
        else:
            C.append(B[j])
            (j,k)=((j+1),(k+1))
    return(C)

def mergesort(P):
    q=len(P)

    if(q<=1):
        return(P)

    L=mergesort(P[:q//2])
    R=mergesort(P[q//2:])

    Q=merge(L,R)
    return(Q)

