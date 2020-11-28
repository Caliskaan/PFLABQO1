a = [1,3,5]
b = [2,4,6]
c = a + b
c[3] = 42
c.append(7)
c.append(8)
c.append(9)
print([c[0],c[1]])
print([b[2]])
count = -1                             #function for length
for i in c:
    count = count + 1
average = sum(c)/count   # function for average we divide it by length and add c 
print(average)
        
    



