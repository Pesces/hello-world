pal = raw_input ("Ingrese palabra: ")
i=len(pal)
l=[]
for x in pal:
	l.append(x)
print l
li=[]
while i>=1:
	i=i-1	
	li.append(l[i])
print li

s=''.join(li)
print s
