data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

x = readData(data1)
y = readData(data2)

txt = []
for i in x:
	if i in y:
		if i not in txt:
			txt.append(i)

print (txt)
