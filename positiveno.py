#print positive numbers in range

#input of list
list=[]
n=int(input("Enter size of list1"))
for i in range(0,n):
  e=int(input("Enter element of list1"))
  list.append(e)


n=int(input("Enter size of list2"))
for i in range(0,n):
  e=int(input("Enter element of list2"))
  list.append(e)

print("Positive numbers in",list,"are: ")

#transversing
for i in list:
     #checking condition
     if i>= 0:
       print(i, end = " ")
