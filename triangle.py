#直角三角形
def makedelta(n,m):
    for i in range(1,n):
        for j in range(i):
            print(m,end=" ")
        print()

makedelta(3,"+")
makedelta(6,"#")
makedelta(9,"*")

#倒三角形
def makereverse(n,m):
    for i in range(n,0,-1):
        for j in range(i):
            print(m,end="")
        print()

makereverse(3,"+")
makereverse(6,"#")
makereverse(9,"*")

#反向三角形
def makervdelta(n,m):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(i):
            print(m,end="")
        print()

makervdelta(3,"+")
makervdelta(6,"#")
makervdelta(9,"*")

#反向倒三角形
def makerevrese2(n,m):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(i):
            print(m,end="")
        print()

makerevrese2(3,"+")
makerevrese2(6,"#")
makerevrese2(9,"*")

#正三角形
def maketriangle(n,m):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(2*i-1):
            print(m,end="")
        print()

maketriangle(3,"+")
maketriangle(6,"#")
maketriangle(9,"*")

