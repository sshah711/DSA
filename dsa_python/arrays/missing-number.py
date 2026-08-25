def missing_number(a):
    n=len(a)
    sumt=n*(n+1)//2
    suma=0
    for i in range(n):
            
        suma= suma+a[i]

        
    return sumt-suma

a=[1,3,2,5,0]
print(missing_number(a))