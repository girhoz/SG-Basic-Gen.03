data1 = "Kurung.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line
	return x

x = readData(data1)

stack = []
z = " "
for i in x:
	#print (i)
	if i == '(':
		stack.append(i)
	elif i == ')':
		if len(stack) != 0:
			for j in stack:
				#print (j)
				if j == '(':
					z = "Valid"
					stack.remove('(')
					break
				elif j != '(':
					z = "Not Valid"
					break
		elif len(stack) == 0:
			z = "Not Valid"
			break
	#print(stack)
print (stack)
if len(stack) != 0:
	z = "Not Valid"

print (z)
