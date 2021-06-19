total_nos=[]
for i in range (2000,3201):
    total_nos.append(i)
# print(total_nos)
divby7 = []
for i in total_nos:
  if i%7 ==0 and i%5!= 0:
    divby7.append(i)
print(divby7)
# print(type(divby7))
# setof7not5 = set(divby7)
# type(setof7not5)
  
