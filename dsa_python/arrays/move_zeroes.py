def move_zeroes(a):
    x = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[x] = a[i]
            
            x += 1
            i += 1
    # fill all the remaining element to zero
    for i in range(x,len(a)):
        a[i]=0
        i+=1
    return a


a = [0,1,0,1,0,0,0,0,0, 4, 0, 6, 0, 2, 0]
print(move_zeroes(a))
