def func2(lis):
    lis.append(3)
    return lis
   
lis = [1,2]
print(func2(lis)) # [1,2,3]
print(lis) # [1,2,3]