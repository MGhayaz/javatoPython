l = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)

def functioning(i):
    if(i % 5 == 0):
        return True
    return False
# filter ka syntax : list(filter(function,input_list))
r = list(filter(functioning,l))
print(r)