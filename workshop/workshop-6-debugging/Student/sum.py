# -*- coding: utf-8 -*-

"""
  Find summation of v_i, from i:=1 to n (inclusive);
    - if i can be divided by 3, v_i = 2xi
    - if i can be divided by 5, v_i = 3xi
    - if i can be divided by 15, v_i = 10xi
    - otherwise v_i = i
    if i can be divided by more than one numbers (in the choices of 3, 5, 15)
      v_i will be calculated by using the biggest divisor condition
"""

n = int(input())
s = 0

for i in range(n):
	if(i % 3 == 0):
		s += 2 * i
	if(i % 5 == 0):
		s += 3 * i
	if(i % 15 == 0):
		s += 10 * i
	else:
		s += i

print(s)