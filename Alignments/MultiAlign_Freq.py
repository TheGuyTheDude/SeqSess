seq1 = "actggcttac"

seq2 = "accggccttc"

seq3 = "agtggcttac"

seq4 = "agtggcttac"


letter_assignments = {'a':1.0, 'c':0.1, 't':0.01, 'g':0.001}

s1 = list(seq1)
s2 = list(seq2)
s3 = list(seq3)
s4 = list(seq4)


s1num = []
s2num = []
s3num = []
s4num = []


for i in s1:
  s1num.append(letter_assignments[i])
  
for i in s2:
  s2num.append(letter_assignments[i])
  
for i in s1:
  s3num.append(letter_assignments[i])
  
for i in s1:
  s4num.append(letter_assignments[i])
  
  
  
  
print(s1num)
print(s2num)
print(s3num)
print(s4num)


import numpy as np
import pandas as pd


vect1 = np.array(s1num)
vect2 = np.array(s2num)
vect3 = np.array(s2num)
vect4 = np.array(s4num)

sumVect = vect1 + vect2 + vect3 + vect4

print(sumVect)

a = np.array([1, 0, 0, 0])
t = np.array([0, 1 ,0, 0])
c = np.array([0, 0, 1, 0])
g = np.array([0, 0, 0, 1])


let = {'a':a, 'c':c, 't':t, 'g':g}


one = []
two = []
three = []
four = []


for i in seq1:
  one.append(i)
  
for i in seq2:
  two.append(i)
  
for i in seq3:
  three.append(i)
  
for i in seq4:
  four.append(i)
  
  
  
a = np.array([1, 0, 0, 0])
t = np.array([0, 1 ,0, 0])
c = np.array([0, 0, 1, 0])
g = np.array([0, 0, 0, 1])


dick_2 = {'a': a, 't': t, 'c':c, 'g':g}


arraylist1 = []
arraylist2 = []
arraylist3 = []
arraylist4 = []

for i in one:
  arraylist1.append(dick_2[i])

for i in two:
  arraylist2.append(dick_2[i])
  
for i in three:
  arraylist3.append(dick_2[i])
  
for i in four:
  arraylist4.append(dick_2[i])
  
  
  
_1_ = np.array(arraylist1)
_2_ = np.array(arraylist2)
_3_ = np.array(arraylist3)
_4_ = np.array(arraylist4)

_net_ = _1_ + _2_ + _3_ + _4_

print(_net_)



l_of_l = []
for i in _net_:
  a = i[0]
  t = i[1]
  c = i[2]
  g = i[3]
  w = 100 * a/4
  x = 100 * t/4
  y = 100 * c/4
  z = 100 * g/4
  
  n = str(w) + "%"
  o = str(x) + "%"
  p = str(y) + "%"
  q = str(z) + "%"
  
  l_of_l.append([n, o, p, q])
  
  
#print(l_of_l)
  
  
concensus = np.array(l_of_l)
print(concensus)


_data_ = pd.DataFrame({'Adenosine':concensus[:,0],
                        'Tyrosine':concensus[:,1],
                        'Cytosine':concensus[:,2],
                        'Guanine':concensus[:,3]})


print(_data_)
