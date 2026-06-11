
#Swap 2 tuples
t=("People","Hello","Bello","Hello")
p=("Your","jello","Justin","Justin")
t,p=p,t
print(t)
print(p)

#Create a nested loop and acses inner elements
nested_tuple = (("Apple", "Banana"), ("Cherry", "Date"), ("Elderberry", "Fig"))
for inner_tuple in nested_tuple:
  for fruit in inner_tuple:
      print(fruit)

#Find repeated elements in a tuple.
seen=set()
r=set()
for i in p:
  if i in seen:
    r.add(i)
  seen.add(i)
print(r)

#Convert tuple of strings into a single string.
print("".join(t))

#Create a tuple without using parentheses.
y='hello','pello'

#Add elements using add()
d={"Hello","Bello","Cello","Dello","aollo"}
d.add("Eollo")
print(d)

#Remove elements using remove()
d.remove("Hello")
print(d)

#Find the union of 2 sets
s={1,2,3,4,5,6}
st={5,3,2,1,7,8,5}
sst=s.union(st)
print(sst)

#Find intersection of 2 sets
ssti=s.intersection(st)
print(ssti)

#Find difference between sets.
sstd=s.difference(st)
print(sstd)

#Check subset and superset
sstst=s.issubset(st)
sstsp=s.issuperset(st)
print(sstst,sstsp)

#Remove duplicates from a list using sets.

r=[1,2,3,3,4,2,1,3,2,5]
l=(set(r))
print(l)

#Find common elements in two lists.

y=['1','3','4','2']
common = list(set(r) & set(y))  
print(common)

#count unique vowels

def count_unique_vowels(s):
    vowels = set("aeiou")
    unique_found = set(s.lower()) & vowels
    return len(unique_found)

#Find symmetric difference.

s = {1, 2, 3, 4}
se = {3, 4, 5, 6}

result = s.symmetric_difference(se)
print(result)  

# is it disjoint
print(s.isdisjoint(se))
#Create a frozen set.
# Create an empty frozenset
fs = frozenset()
fss = frozenset(s)
print(fss)



