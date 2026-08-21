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

for i in range(4):
    row=" "
    for j in range(i+1):
        row+= str(j+1)

    print(row)


for i in range(5):
    row=" "
    for j in range(i+1):
        row+= str(i+1)


    print(row)
print("")

for i in range(5):
    row=" "
    for j in range(5-i):
        row+=str(j+1)
    print(row)

for i in range(5):
    row=" "
    for j in range(5-i):
        row+="*"
    print(row)


for i in range(5):
    row=""
    for k in range(5-(i+1)):
        row+=" "   
    for j in range(i+1):
        row+="*"

    print(row)


for i in range(5):
    row=""
    for k in range(5-(i+1)):
        row+=" "   
    for j in range(i+1):
        row+=str(i+1)

    print(row)

for i in range(5):
    row=" "
    for k in range(5-(i+1)):
        row+=" "   
    for j in range(i+1):
        row+=str(j+1)

    print(row)


for i in range(5):
    row=" "
    switch=1
    for j in range(i+1):
        row+=str(switch)
        if(switch==1):
            switch=0
        else:
            switch=1
    print(row)

switch=1
for i in range(5):
    row=" "
   
    for j in range(i+1):
        row+=str(switch)
        if(switch==1):
            switch=0
        else:
            switch=1
    print(row)

for i in range(5):
    row=" "
    for l in range(i+1):
        row+=str(j)

    for k in range(5-(i+1)):
        row+=" "   
    for j in range(i+1):
        row+=str(j+1)


    print(row)


for i in range(5):
    row=""
    for k in range(5-(i+1)):
        row+=" "   
    for j in range(i):
        row+="*"
    for j in range(i+1):
        row+="*"
    print(row)


for i in range(5):
    row=" "
    for k in range(5-(i+1)):
        row+=" " + " "  
    for j in range(i+1):
        row+=str(j+1)+" " 

    for j in range(i):
        row+=str(j+1)+" " 
    print(row)
