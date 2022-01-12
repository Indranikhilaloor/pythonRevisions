import array as arr
#defining an array
a=arr.array('d',[1,23,4,5,6,70])
print(a)
#appending an element
a.append(5)
print(a)
#extending an element
a.extend([5,5,5,5,5])
print(a)
#removing
print(a.pop())
print(a.pop(1))
#exercise
expenses=[2200,2350,260,2130,2190]
extra_spent=expenses[1]-expenses[0]
quater_expenses=0
for i in range(0,3):
    quater_expenses=expenses[i]+quater_expenses
print(quater_expenses)
for a in expenses:
    if(a==2000):
        print("Found it")
expenses.append(1980)
print(expenses)
new_april=expenses[3]-200
expenses.insert(3,new_april)
print(expenses)
#another one
heros=['spider man','thor','hulk','iron man','captain america']
length=len(heros)
print(length)
heros.append("black panther")
print(heros)
heros.pop()
heros.insert(3,"black panther")
print(heros)
heros.remove("hulk")
heros.remove("thor")
heros.insert(1,"Doctor Strange")#heros[1:3}=['doctor strange]
print(heros)
heros.sort()
print(heros)
#odd numbers list
list_with_odd=[]
max=int(input("Enter max number"))
for i in range(1,max+1):
    if(i%2!=0):
        list_with_odd.append(i)
print(list_with_odd)
