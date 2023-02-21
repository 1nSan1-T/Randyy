import random

def randyy(c,r):
	sim=[[random.randint(0, 50) for _ in range(c)]for _ in range(r)]
	for i in sim:
		print(i)

def main():
	rw=input("enter number of rows: ")
	cl=input("enter number of colums: ")
	if not (rw.isdigit or cl.isdigit):
		print("Enter valid number!")
		main()
	else:
		hr=int(rw)
		vt=int(cl)
		randyy(hr,vt)
		
main()