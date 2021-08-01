"""
@Author: Ranjith G C
@Date: 2021-07-28
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-28 
@Title : Program Aim is to work with matrix multiplication by using mapper.
"""

#!/usr/bin/env python

import sys
m_r=2
m_c=3
n_r=3
n_c=2

i=0
for line in sys.stdin:
	el=map(int,line.split())
	if(i<m_r):
		for j in range(len(el)):
			for k in range(n_c): print("{0}\t{1}\t{2}\t{3}".format(i, k, j, el[j]))
	else:
		for j in range(len(el)):
			for k in range(m_r): print("{0}\t{1}\t{2}\t{3}".format(k, j, i-m_r, el[j]))
	i=i+1
