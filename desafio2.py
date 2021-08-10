N = [] 
x = int(input())
N.append(x)
print("N[{}]={}".format(0,N[0]))
for i in range (1,10):
   N.append(N[i-1]*2)
   print("N[{}]={}".format(i,N[i]))
   
