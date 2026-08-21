import math
def count_digit(n):
    if n==0:   #corner case
        return 1    
    n=abs(n)     #corner case
    c=0
    while(n>0):
        # n=math.floor(n/10)
        n=n//10
        c+=1
    return (c)    

n=-1837
print(count_digit(n))
# print(math.floor(n))

