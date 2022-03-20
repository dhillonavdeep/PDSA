def Twin_Primes(n,m):
    prime_list=[]
    num=0
    for num in range(n,m+1):
        if(num>1):
            flag=False
            for i in range(2,num):
                if(num%i==0):
                    flag=True
                    break
            if(flag==False):
                prime_list.append(num)                  
    d=len(prime_list)
    touple_list=[]
    c=0
    for c in range(0,d-1):
        if(prime_list[c+1] - prime_list[c] == 2 ):
            touple_list.append((prime_list[c],prime_list[c+1]))
       
    return(touple_list)
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))