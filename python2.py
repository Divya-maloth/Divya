
# python Sets
#Exercise 1: Perform Basic Set Operations
s1={1,6,2,5,4}
print(s1)
 
 
#Exercise 2: Union of Sets
s1={1,3,2}
s2={3,4,5}
s3=s1.union(s2)
print(s3)
 
 
#Exercise 3: Intersection of Sets
s1={1,3,2}
s2={2,3,5,4}
result=s1.intersection(s2)
print(result)
 
 
#Exercise 4: Difference of Sets
s1={1,2,3,6}
s2={2,3,4,5}
s3=s1.difference(s2)
print(s3)
 
 
#Exercise 5: Symmetric Difference
s1={1,2,3,6}
s2={2,3,4,5}
s3=s1.symmetric_difference(s2)
print(s3)
 
 
#Exercise 6: Add a list of Elements to a Set
s1={1,2,3,6}
s2=[2,3,4,5]
s1.update(s2)
print(s1)
 
 
#Exercise 7: Set Difference Update
s1={1,2,3,6}
s2={2,3,4,5}
s3=s1.difference(s2)
print(s3)
 
 
#Exercise 8: Remove Items From Set Simultaneously
s1={1,2,3,4,5}
s2={2,3}
for i in s2:
    s1.discard(i)
print(s1)
 
 
#Exercise 9: Check Subset
def check(s1,s2):
    for i in s1:
        if i not in s2:
            return False
    else:
        return True
s1={1,2}
s2={1,2,3}
s3=check(s1,s2)
print(s3)
 
 
#Exercise 10: Check Superset
def check_superset(s1,s2):
    for i in s2:
        if i not in s1:
            return False
    else:
        return True
s1={1,2}
s2={1,2,3}
result=check_superset(s1,s2)
print(result)
 
 
#Exercise 11: Set Intersection Check
def check_intersection(s1,s2):
    for i in s1:
        if i in s2:
            return True
    else:
        return True
s1={1,2,3}
s2={3,5,6}
result=check_intersection(s1,s2)
print(result)
 
 
#Exercise 12: Set Symmetric Difference Update
s1={1,2,3}
s2={3,5,6}
s1^=s2
print(s1)
 
 
#Exercise 13: Set Intersection Update
s1={1,2,3,4}
s2={3,4,5}
s1&=s2
print(s1)
 
 
#Exercise 14: Find Common Elements in Two Lists
lst1=[1,2,3,4]
lst2=[3,4,5]
common=[]
for i in lst1:
    if i in lst2:
        common.append(i)
print(common)
 
 
#Exercise 15: Frozen Set
se={1,2,2,3,3,4}
s=frozenset(se)
print(s)
 
 
#Exercise 16: Count Unique Words
str1="vector of hyd or vector of blr and UST"
seen=[]
cnt=0
res=str1.split(" ")
for i in res:
    if i not in seen:
        seen.append(i)
print(seen)
print(len(seen))

