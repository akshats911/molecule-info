from math import *

"""
PLS GIVE THE FULL PATH OF THE .xyz FILE YOU WISH TO RUN AS STRING BELOW. DO NOT CHANGE ANYTHING ELSE
"""

with open(r"benzene.xyz","r") as f:
    n=int(f.readline())
    f.readline()
    lines=f.readlines()
#n is number of atoms
AtomNameList=[] 
for i in lines:
    AtomNameList.append(i.split(" ")[0])
#AtomNameList=["O","H","H"]

AtomCordinateList=[]
k=1
while(k<=3):
    for i in lines:
        globals()[f"a{k}"]=i.split(" ")[1:4]
        AtomCordinateList.append(f"a{k}")
        k+=1
#AtomCordinateList=[a1,a2,a3]

coordinate = {"x":0,"y":1,"z":2}


def bond_length_calculator(atom1,atom2):
    atom1=eval(atom1)
    atom2=eval(atom2)
    xdist=float(atom1[coordinate.get("x")])-float(atom2[coordinate.get("x")])
    ydist=float(atom1[coordinate.get("y")])-float(atom2[coordinate.get("y")])
    zdist=float((atom1[coordinate.get("z")]).rstrip("\n")) -float((atom2[coordinate.get("z")]).rstrip("\n"))
    dist = sqrt((xdist**2)+(ydist**2)+(zdist**2))
    return dist 

def no_of_bonds(n):
    bonds=(factorial(n))/(factorial(n-2)*factorial(2))
    return int(bonds)

def bond_length():
    for i in range(n):
        for j in range(i+1,n):
            print(f"Bond length between {AtomNameList[i]} and {AtomNameList[j]} is: {bond_length_calculator(AtomCordinateList[i],AtomCordinateList[j])}")

def anglenum(n):
    angles=factorial(n)/(factorial(n-3)*factorial(3))
    return int(angles)

#n = int(input("Enter number of atoms in the molecule"))

print("Number of Bonds is:",no_of_bonds(n))
print("BOND LENGTHS:")
bond_length()
print("Number of Angles is:",anglenum(n))            



