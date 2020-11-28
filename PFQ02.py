def check(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    return False
    
list1 = [9,10,3,4]   #values given of list1 and list2
list2 = [8,4,6,7]      
check(list1,list2)
