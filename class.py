class Animal:
    def __init__(self,variety,age):
        self.variety=variety
        self.__age=age #封裝/私有屬性
    def hungry(self):
        return "肚子餓的時候，會找喜歡的東西吃。"
    def sleep(self):
        return "想睡覺的時候，會找舒服的地方睡覺。"
ani=Animal("種類","幾歲")
print(f"這個動物是什麼{ani.variety}，年齡{ani._Animal__age}?") #_Animal__age訪問私有屬性
print(f"動物如果{ani.hungry()}如果{ani.sleep()}")
print()

class Dog(Animal): #繼承
    def __init__(self,weight,color):
        self.weight=weight
        self.color=color
    def move(self):
        return "用四隻腳走路"
    def bark(self):
        return "汪汪"
    def play(self):
        return "出去玩!"
dog=Animal("黑狗","")
thisDog=Dog(6,"黑色")
print(f"這個動物是{dog.variety}，這隻{dog.variety}的體重是{thisDog.weight}公斤，毛色是{thisDog.color}。")
print(f"這隻{dog.variety}的移動方式是{thisDog.move()}，叫聲是{thisDog.bark()}，喜歡{thisDog.play()}")
print()

class Corgi(Dog): #多層繼承
    def __init__(self,name):
        self.name=name
    def play(self): #覆蓋 play() method
        return "玩玩具!"
corgi1=Corgi("土豆")
peanuts=Dog(5,"白色&橘黃色")
thePeanuts=Animal("柯基犬",3)
corgi2=Corgi("露露")
lulu=Dog(6,"白色&橘黃色")
theLulu=Animal("柯基犬",3)
print(f"這兩隻狗是{thePeanuts.variety}，{thePeanuts.variety}的移動方式是{lulu.move()}，叫聲是{lulu.bark()}。")
print(f"他們分別叫做{corgi1.name}和{corgi2.name}，他們都是{theLulu._Animal__age}歲，毛色都是{peanuts.color}。")
print(f"{corgi1.name}的體重是{peanuts.weight}公斤，{corgi2.name}的體重是{lulu.weight}公斤。")
print(f"他們都喜歡{corgi1.play()}{theLulu.hungry()}{theLulu.sleep()}")