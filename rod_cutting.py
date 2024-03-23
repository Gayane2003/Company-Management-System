def base_converter(num, x):
    binary = list()
    if num < (x+1):
        binary.append(num)  
    while num >= x+1:
        rem = num % (x+1)
        num = num // (x+1)
        
        binary.append(rem)
        if num < (x+1):
            binary.append(num)  
            
    binary.reverse()
    binary = [0] * (x-len(binary)) + binary
    return binary



def brute_force(l, profit):
    max_profit = 0
    for i in range(0, (l + 1)**l):
        x = base_converter(i, l)
        sum = 0 
        for i in range(0, len(x)):
            sum = x[i] * (i+1) + sum
        if sum == l:
            prf = 0
            for z in range(0, len(x)):
                prf = prf + (profit[z] * x[z])
            max_profit = max(prf, max_profit)
        
    return "Max profit is " + str(max_profit)
   
     
print('Brute force iterative approach')
profit = [1, 3, 5, 5, 7, 8]             
print(brute_force(len(profit), profit) + "\n")


print("Brute force recurisiveapproach recurisive")



def rec_rod_cutting(l, profit):
  if(l == 0):
      return l

  max_prof = -100

  for i in range(1, l+1):
      max_prof = max(max_prof, profit[i] + rec_rod_cutting(l-i, profit))

  return max_prof


print(rec_rod_cutting(6, [0, 1, 3, 5, 5, 7, 8]))


print("\n")
print("Buttom up approach")

def buttom_up_rod_cutting(profit, l):
    length = [i for i in range(0, l+1)]
    for j in range(1, l+1):
        q = -1000
        for i in range(1, j+1):
            q = max(q, profit[i]+length[j-i])
        length[j] = q
    return length[l]
        

print(buttom_up_rod_cutting([0, 1, 3, 5, 5, 7, 8], 6))































