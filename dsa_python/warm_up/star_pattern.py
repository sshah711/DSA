for i in range(4):
    row=" "
    for j in range(4):
        row+="*"
    print(row)

for i in range(4):
    row=" "

    for j in range(i+1):
        row+="*"
    print(row)

    
print(" ")

for i in range(4,0,-1):
    row=" "
    for j in range(i):
        row+="*"
    print(row)

for i in range(4,0,-1):
    row=" "
    for j in range(i):
        row+=" "
    for k in range(i-1):
        row+="*"
    print(row)