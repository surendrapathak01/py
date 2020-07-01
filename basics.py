# mylist = [1,2,3]
# print("Zeroth value: %d " % mylist[0])

# Dictonary
mydict = {'a':1, 'b':2, 'c':3}
print("A value: %d " % mydict['a'])
mydict['a']=11
print("A value: %d " % mydict['a'])
print("Keys: %s " % mydict.keys())
print("Values: %s " % mydict.values())
for keys in mydict.keys():
    print(mydict[keys])