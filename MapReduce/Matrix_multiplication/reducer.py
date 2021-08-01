"""
@Author: Ranjith G C
@Date: 2021-07-28
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-28 
@Title : Program Aim is to work with matrix multiplication by using reducer.
"""

#!/usr/bin/env python
import sys
m_r=2
m_c=3
n_r=3
n_c=2

matrix=[]
for row in range(m_r):
	r=[]
	for col in range(n_c):
		s=0
		for el in range(m_c):
			mul=1
			for num in range(2):
				line=sys.stdin.readline()
				n=map(int,line.split('\t'))[-1]
				mul*=n
			s+=mul
		r.append(s)
	matrix.append(r)
print('\n'.join([str(x) for x in matrix]))
