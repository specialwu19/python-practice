class Animal:
    def __init__(self,variety,age):
        self.variety=variety
        self.__age=age #封裝/私有屬性
    def hungry(self):
        return "肚子餓的時候，會找喜歡的東西吃。"
    def sleep(self):
        return "想睡覺的時候，會找舒服的地方睡覺。"
animal=Animal("種類","幾歲")
print(f"這個動物是什麼{animal.variety}，年齡{animal._Animal__age}?") #_Animal__age訪問私有屬性
print(f"動物如果{animal.hungry()}如果{animal.sleep()}")
print()

class Dog(Animal): #繼承
    def __init__(self,variety,age,weight,color,name):
        super().__init__(variety,age) #利用 super() function
        self.weight=weight
        self.color=color
        self.name=name
    def move(self):
        return "用四隻腳走路"
    def bark(self):
        return "汪汪"
    def play(self):
        return "出去玩!"
dog=Dog("黑狗","",6,"黑色","Kuro")
print(f"這個動物是{dog.variety}，這隻{dog.variety}的體重是{dog.weight}公斤，毛色是{dog.color}。")
print(f"這隻{dog.variety}的移動方式是{dog.move()}，叫聲是{dog.bark()}。喜歡{dog.play()}")
print()

class Corgi(Dog): #多層繼承
    def __init__(self,age,weight,name):
        super().__init__("柯基犬",age,weight,"白色&橘黃色",name) #利用 super() function
    def play(self): #覆蓋 play() method
        return "玩玩具!"
corgi1=Corgi(3,5,"土豆") #多型
corgi2=Corgi(3,6,"露露") #多型

print(f"這兩隻狗是{corgi1.variety}，{corgi1.variety}的移動方式是{corgi1.move()}，叫聲是{corgi1.bark()}。")
print(f"他們分別叫做{corgi1.name}和{corgi2.name}，他們都是{corgi2._Animal__age}歲，毛色都是{corgi2.color}。")
print(f"{corgi1.name}的體重是{corgi1.weight}公斤，{corgi2.name}的體重是{corgi2.weight}公斤。")
print(f"他們都喜歡{corgi1.play()}{corgi1.hungry()}{corgi1.sleep()}")
print()

class Bulldog(Dog): #多層繼承
    def __init__(self,age,weight,color,name):
        super().__init__("鬥牛犬",age,weight,color,name) #利用 super() function
    def sleep(self): #覆蓋 sleep() method
        return "睡覺的時候，會打呼。"
bulldog=Bulldog(5,8,"米白色","憨吉")
print(f"這隻狗是{bulldog.variety}，名字叫{bulldog.name}，今年{bulldog._Animal__age}歲，體重{bulldog.weight}公斤，毛色是{bulldog.color}。")
print(f"{bulldog.name}{bulldog.hungry()}{bulldog.sleep()}喜歡{bulldog.play()}")