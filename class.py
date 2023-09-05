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
    def __init__(self,variety,age,weight,color):
        super().__init__(variety,age) #利用 super() function
        self.weight=weight
        self.color=color
    def move(self):
        return "用四隻腳走路"
    def bark(self):
        return "汪汪"
dog=Dog("黑狗","",6,"黑色")
print(f"這個動物是{dog.variety}，這隻{dog.variety}的體重是{dog.weight}公斤，毛色是{dog.color}。")
print(f"這隻{dog.variety}的移動方式是{dog.move()}，叫聲是{dog.bark()}。")
print()

class Corgi(Dog): #多層繼承
    def __init__(self,variety,age,weight,color,name):
        super().__init__(variety,age,weight,color) #利用 super() function
        self.weight=weight
        self.name=name
    def play(self): #覆蓋 play() method
        return "玩玩具!"
corgi1=Corgi("柯基犬",3,5,"白色&橘黃色","土豆")
corgi2=Corgi("柯基犬",3,6,"白色&橘黃色","露露")

print(f"這兩隻狗是{corgi1.variety}，{corgi1.variety}的移動方式是{corgi1.move()}，叫聲是{corgi1.bark()}。")
print(f"他們分別叫做{corgi1.name}和{corgi2.name}，他們都是{corgi2._Animal__age}歲，毛色都是{corgi2.color}。")
print(f"{corgi1.name}的體重是{corgi1.weight}公斤，{corgi2.name}的體重是{corgi2.weight}公斤。")
print(f"他們都喜歡{corgi1.play()}{corgi1.hungry()}{corgi1.sleep()}")