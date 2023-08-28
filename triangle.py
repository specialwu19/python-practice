#直角三角形
def makeRightTriangle(n,m): #n=高度,m=符號
    for i in range(1,n+1):
        for j in range(i):
            print(m,end="")
        print()

makeRightTriangle(3,"+")
makeRightTriangle(6,"#")
makeRightTriangle(9,"*")

#倒三角形
def makeInvertedTriangle(n,m): #n=高度,m=符號
    for i in range(n,0,-1):
        for j in range(i):
            print(m,end="")
        print()

makeInvertedTriangle(3,"+")
makeInvertedTriangle(6,"#")
makeInvertedTriangle(9,"*")

#反向三角形
def makeReversedRightTriangle(n,m): #n=高度,m=符號
    for i in range(1,n+1):
        for j in range(n-i): #第i層需要n-i個空格
            print(" ",end="")
        for j in range(i):
            print(m,end="")
        print()

makeReversedRightTriangle(3,"+")
makeReversedRightTriangle(6,"#")
makeReversedRightTriangle(9,"*")

#反向倒三角形
def makeReverseInvertedTriangle(n,m): #n=高度,m=符號
    for i in range(n,0,-1):
        for j in range(n-i): #第i層需要n-i個空格
            print(" ",end="")
        for j in range(i):
            print(m,end="")
        print()

makeReverseInvertedTriangle(3,"+")
makeReverseInvertedTriangle(6,"#")
makeReverseInvertedTriangle(9,"*")

#等腰三角形
def makeIsoscelesTriangle(n,m): #n=高度,m=符號
    for i in range(1,n+1):
        for j in range(n-i): #第i層需要n-i個空格
            print(" ",end="")
        for j in range(2*i-1): #把直角三角形補成等腰三角形
            print(m,end="")
        print()

makeIsoscelesTriangle(3,"+")
makeIsoscelesTriangle(6,"#")
makeIsoscelesTriangle(9,"*")

#聖誕樹
def makeXmasTree(n,m): #n=高度,m=符號
    for i in range(1,n+1):
        for j in range(n-i): #第i層需要n-i個空格
            print(" ",end="")
        for j in range(2*i-1): #把直角三角形補成等腰三角形
            print(m,end="")
        print()
    for i in range(1,n):
        print(" ",end="") #為了讓樹幹置中，在樹幹位置前補空白
    print("|") #樹幹

makeXmasTree(3,"*")
makeXmasTree(6,"*")
makeXmasTree(9,"*")