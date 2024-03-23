def ProductList(ls, i = 0):
    if len(ls) == i:
        return ls
    if i == 0:
       ls[i] = ls[0] 
    else:
        ls[i] = ls[i] * ls[i-1]
    
    return ProductList(ls, i+1)


print(ProductList([3, 5, 1, 4]))