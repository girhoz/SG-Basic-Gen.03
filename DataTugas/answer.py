data1 = "DataSet.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
	
teks = readData(data1)
arr = []
idx = []
word = (teks[0])[0].upper() + (teks[0])[1:]
teks[0] = word
for i, x in enumerate(teks):
	if(x[len(x)-1] == ".") and (i != len(teks)-1):
		word = (teks[i+1])[0].upper() + (teks[i+1])[1:]
		teks[i+1] = word
	if(x.isdigit()):
		arr.append(x)
		idx.append(i)

j = len(arr)-1
for x in idx:
	teks[x] = arr[j]
	j-= 1

print (" ".join(teks))
