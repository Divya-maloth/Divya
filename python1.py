#list excercise
#1.basic list operation
li=[]
li=list(map(int,input("enter elements for list sep as,").split(",")))
print(li)
print(li[1])

#2.list manipulation
li=[2,3,1]
sum=0
for i in li:
    sum=sum+i
print(sum)
li.reverse()
print(li)
li.extend([5,6])
print(li)
#3.Sum and average of all numbers in a list
li=[2,3,1]
l=len(li)
sum=0
for i in li:
    sum=sum+i
avg=sum//l
print(sum)
print(avg)

#Exercise 4: Reverse a list
lis=[1,4,5,2,6]
lis.reverse()
print(lis)
#Exercise 5: Turn every item of a list into its square
l2=list(map(lambda x:x*x,lis))
print(l2)
#Exercise 6: Find Maximum and Minimum
lis=[1,4,5,2,6]
print("max=",max(lis))
print("min=",min(lis))
#Exercise 7: Count Occurrences
lis=[2,4,2,3,4,5,6]
for i in set(lis):
     print(i,"repeated",lis.count(i),"times")

#Exercise 8: Sort a list of numbers
lis=[2,4,2,3,4,5,6]
lis.sort()

#Exercise 9: Create a copy of a list
a=[2,4,2,3,4,5,6]
b=a.copy()
print("list a is",a)
print("list b is ",b)
#Exercise 10: Combine two lists
a=[3,4,5]
b=[3,4,5,6,7]
print(a+b)
a.extend(b)
print(a)

#Exercise 11: Remove empty strings from the list of strings
sl=["apple"," ","banana","orange"," "," "]
for i in sl[:]:
    if i==" ":
        sl.remove(i)
print(sl)
#Exercise 12: Remove Duplicates from list
a=[2,4,2,3,4,5,6]
print(set(a))
#another way
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

#Exercise 13: Remove all occurrences of a specific item from a list
a=[2,4,2,3,4,5,6,2]
i=int(input("enter which number occu you want to remove"))
for j in a:
    if j==i:
        a.remove(j)
print(a)

#Exercise 14: List Comprehension for Numbers
a=[1,23,4,5,8,9,10]
even=[x for x in a if x%2==0]
print(even)

#Exercise 15: Access Nested Lists
lb=[2,3,[4,5],3]
print(lb[2])
print(lb[2][0])
#Exercise 16: Flatten Nested List
l=[1,23,4,[2,3,4],5,8,9,10]
b=[]
for i in l:
    if isinstance(i,list):
        for j in i:
            b.append(j)
    else:
        b.append(i)
print(b)

#Exercise 17: Concatenate two lists index-wise
l1=["good","hello","thank"]
l2=["morning","  hi","you"]
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)

#Exercise 18: Concatenate two lists in the following order
a = [1, 2]
b = [3, 4]
result = []
for i in a:
    for j in b:
        result.append(i)
        result.append(j)
print(result)
#Exercise 19: Iterate both lists simultaneously
l1=[2,3,1,4]
l2=[3,2,4,5]
for a,b in zip(l1,l2):
    print(a,b)

#Exercise 21: Add new item to list after a specified item
li=[10,20,30,40]
i=int(input("enter the index val where you want to insert"))
v=int(input("which val you want to insert"))
li.insert(i,v)
print(li)
#Exercise 22: Extend nested list by adding the sublist
l1=[1,2,3]
l1.extend([3,4,5])
print(l1)
#Exercise 23: Replace list’s item with new value if found
l1=[20,30,40,50]
new=300
old=30
for i in range(len(l1)):
    if l1[i]==old:
        l1[i]=new
print(l1)

#Python Dictionary 
# Exercise 1: Perform basic dictionary operations
d={'k':'v','k2':'v2','k3':'v3'}
print(list(d.items()))

#Exercise 2: Perform dictionary operations
d1={'k':'v','k2':'v2','k3':'v3'}
print(d1["k2"])
d1.pop('k')
print(d1)
d1.popitem() #removes last item in dict
print(d1)
#Exercise 3: Dictionary from Lists
li1=[1,2,3,4,5]
li2=[10,20,30,40,50]
d={}
for i in range(len(li1)):
    d[li1[i]]=li2[i]
print(d)
#another way
d1={}
d1=dict(zip(li1,li2))
print(d1)
#Exercise 4: Clear Dictionary
d1={'k':'v','k2':'v2','k3':'v3'}
print(d1)
d1.clear()
print(d1)
#Exercise 5: Merge two Python dictionaries into one
d1={"k":1,"k2":2}
d2={"k3":4,"k4":4}
d1.update(d2)
print(d1)
#Exercise 6: Count Character Frequencies
s="banana"#python programming"
d1={}
for i in s:
    d1[i]=d1.get(i,0)+1
print(d1)
#or
for i in s:
    d1[i]=s.count(i)
print(d1)

#Exercise 7: Access Nested Dictionary
d1={"k":1,"k2":2,"d2":{"k3":4,"k4":4}}
result={}
for k,v in d1.items():
    if isinstance(v,dict):
        for key,val in v.items():
            result[f"{k}.{key}"]=val
    else:
        result[k]=v
print(result)

#Exercise 8: Print the value of key ‘history’ from nested dict
d1={"k":1,"k2":2,"d2":{"history":"hval","k4":4}}
for k,v in d1.items():
    #print(v["history"])
    if isinstance(v,dict):
        for key,val in v.items():
            if key=="history":
                print(v["history"])

#another way
print(d1["d2"]["history"])
#Exercise 9: Modify Nested Dictionary
d1={"k":1,"k2":2,"d2":{"history":"hval","k4":4}}
d1["d2"]["history"]=100
print(d1)
#Exercise 10: Initialize dictionary with default values
k={"a","b","c","d"}
defualt_val=0
d=dict.fromkeys(k,defualt_val)
print(d)
#Exercise 11: Create a dictionary by extracting the keys from a given dictionary
di={"k":1,"k2":2,"d2":3}
new_d=dict.fromkeys(di,None)
print(new_d)
#Exercise 12: Delete a list of keys from a dictionary
k={"a":1,"b":2,"c":3,"d":4}
dk={"b","c"}
for key in dk:
    if key in k:
        del(k[key])
print(k)

        
#Exercise 13: Check if a value exists in a dictionary
di={"k":1,"k2":2,"d2":3}
flag=0
v=int(input("enter val to check"))
for k,val in di.items():
    if val==v:
        flag=1

if flag:
    print("val exist")
else:
    print("val not exist")

#other way
di = {"k": 1, "k2": 2, "d2": 3}

v = int(input("enter val to check: "))

if v in di.values():
    print("val exist")
else:
    print("val not exist")

    
#Exercise 14: Rename key of a dictionary
d = {"name": "A","age": 22}
d["full_name"] = d.pop("name")
print(d)
#other way
d = {"name": "A","age": 22}
d["f_name"]=d["name"]
del d["name"]
print(d)
#Exercise 15: Get the key of a minimum value
d1={'a':1,'b':2,'c':9}
min_v=9
min_k=None
for k,v in d1.items():
    if v < min_v:
        min_v=v
        min_k=k
print(min_k)

#Exercise 17: Invert Dictionary
d1={"apple":10,"banana":20,"orange":30}
d2={}
for k,v in d1.items():
    if not isinstance(v,dict):
        d2[v]=k
print(d2)
#Exercise 18: Sort Dictionary by Keys
d1={'b':2,'c':3,'d':4,'a':1}
lst=list(d1.keys())
print(lst)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]>lst[j]):
            lst[i],lst[j]=lst[j],lst[i]
sorted_dict={}
for i in lst:
    sorted_dict[i]=d1[i]
print(sorted_dict)

#Exercise 19: Sort Dictionary by Values
d1={'a':5,'b':12,'c':3,'d':15,'e':1}
lst=list(d1.items())
print(lst)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if (lst[i][1]>lst[j][1]):
            lst[i],lst[j]=lst[j],lst[i]
sorted_dict={}
for k,v in lst:
    sorted_dict[k]=v
print(sorted_dict)
#Exercise 20: Check if All Values are Unique
d1={'a':1,'b':1,'c':1}
lst=list(d1.values())
print(lst)
value=lst[0]
for i in lst:
    if i!=value:
        print("values are not unique")
        exit()
else:
    print("values are unique")


#python tuple
#Exercise 1: Perform Basic Tuple Operations
t=(1,2,3,4,5)
print(t)
 
 
#Exercise 2:Tuple Repetition
t=(1,2,3,4)
res=t*3
print(res)
 
 
#Exercise 3: Slicing Tuples
t=(1,2,3,4,5)
print(t[1:4])
 
 
#Exercise 4: Reverse the tuple
t=(1,2,3)
print(t[::-1])
 
 
#Exercise 5: Access Nested Tuples
t=(1,2,3,(4,5),6)
print(t[3])
 
 
#Exercise 6: Create a tuple with single item 50
t=(50,) #to represent tuple we need to use comma here because if there is no comma it will consider it as integer
print(t)
 
 
#Exercise 7: .Unpack the tuple into 4 variables
t=(10,20,30,40,50)
a,b,c,d,e=t
print(a,b,c,d,e)
#     (or)
t=(10,20,30,40,50)
a,b,c,*d=t
print(a,b,c,d)
 
 
#Exercise 8: .Swap two tuples in Python
t1=(1,2,3)
t2=(4,5,6)
t1,t2=t2,t1
print("t1:",t1)
print("t2:",t2)
 
 
#Exercise 9: Copy Specific Elements From Tuple
t1=(1,2,3,4,5)
print(t1[3:5])
 
 
#Exercise 10: List to Tuple
t1=[1,2,3]
print(tuple(t1))
 
 
#Exercise 11: Function Returning Tuple
def tup():
    return 10,20,30
result=tup()
print(result)
 
 
#Exercise 12: Comparing Tuples
t1=(1,2,3)
t2=(1,2,3)
if(t1==t2):
    print("tuples are equal")
else:
    print("tuples are not equal")
 
 
#Exercise 13: Removing Duplicates from Tuple
t1=(1,2,3,1,2,3,4)
print(set(t1))
 
 
#Exercise 14: Filter Tuples
t1=(1,2,3,45,67,89,12)
result=tuple(filter(lambda x:x%2==0,t1))
print(res)
 
 
#Exercise 15: Map Tuples
t1=(1,2,3,45,67,89,12)
result=tuple(map(lambda x:x*2,t1))
print(result)
 
 
#Exercise 16: Modify Tuple
t1=(1,2,3,4,5)
t2=[]
modify=2
for i in t1:
    if i==modify:
        t2.append(20)
    else:
        t2.append(i)
print(tuple(t2))
 
 
#Exercise 17: Sort a tuple of tuples by 2nd item
t=((1,5),(2,4),(3,3),(4,2))
li=list(t)
print(l)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i][1]>li[j][1]):
            li[i],li[j]=li[j],li[i]
print(tuple(li))
 
 
#Exercise 18: Count Elements
t1=(1,2,3,4,1,2,3,5)
cnt=0
for i in t1:
    cnt=cnt+1
print(cnt)
#another way
t1=(1,2,3,4,1,2,3,5)
print(t1.count(2))
 
 
#Exercise 19: Check if all items in the tuple are the same
t1=(1,1,1) #if we give one element different then tuples are not same
check=t1[0]
for i in t1:
    if i is not check:
        print("items in tuple are not same")
        exit()
else:
    print("items in tuple are same")
