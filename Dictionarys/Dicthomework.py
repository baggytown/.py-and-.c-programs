#Create and print
d={'Jack':'Bean','Hi':'bye'}
print(d)
#acsess dict
print(d['Jack'])
#Add key value
d["hello"]='byebye'
print(d)
#Update a Dictionary Value 
d.update({'Jack':'Ex'})
print(d)
#Del a dict value
d.pop('Jack',None)
print(d)
#Delete an Item from Dictionary
d['Jack'] = ''
#Merge two Dictionaries
c={'Hii':'byee'}
d.update(c)
print(d)
#Sort 2 dicts
print(dict(sorted(d.items())))