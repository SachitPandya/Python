a=[10,30,7.8]
#print(type(a[0]))

b=(1,4,6,a)
print(b)
print(type(b))

s=list(b)
print(type(s))

s.append(10)
print(s)

s.pop(s)
print(s)


a.__contains__(30)