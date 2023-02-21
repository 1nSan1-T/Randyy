import random
import numpy as np
#method to generate random input
def randyy(c,r,lim):
#start and end of array as defined by user
	a=int(lim[0])
	b=int(lim[1])
#sim variable tied to random array to be generated
	sim=[[random.randint(a, b) for _ in range(c)]for _ in range(r)]
	for i in sim:
		print(i)

def main():
	print("Enter start and end of range of numbers: ")
	st=input("start: ")
	en=input("end: ")
#array variable for easy sharing values with other functions
#numpy array for conditionals check
	r_ng=[st, en]
	rng=np.array(r_ng)
	rw=input("enter number of rows: ")
	cl=input("enter number of colums: ")
#input validity check
	if not (all(np.char.isdigit(rng)) and rw.isdigit() and cl.isdigit()):
		print("Enter valid number!")
		main()
	else:
#input strings to int variables and randyy func call
		hr=int(rw)
		vt=int(cl)
		randyy(hr,vt,rng)
		
main()
