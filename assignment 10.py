#Question 1
N=3;
from itertools import islice
with open("file1.txt") as f:
    a=list(islice(f,N))
print(a)

#Question 2
from collections import Counter
def word_frequency(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("Number of words in file: ",word_frequency("gup.txt"))

#Question 3
with open("a.txt") as f:
    with open("b.txt","w") as f1:
        for l in f:
            f1.write(l)

#Question 4
with open("file1.txt") as f:
    with open("gup.txt") as f1:
        for l,l1 in zip(f,f1):
            print(l+l1)

#Question 5
n=[23,46,78,89,55,10,34,77,18,66]
with open("tan.txt","w") as f:
    for l in n:
        f.write('%d\n' % l)

f1=open("tan.txt")
n=[]
for l1 in f1:
    n.append(int(l1))
n.sort()
f1.close()
with open("bas.txt","w") as f:
    for l in n:
        f.write('%d\n' % l)

