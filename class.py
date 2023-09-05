class Animal:
    def __init__(self,variety,age):
        self.variety=variety
        self.__age=age #私有屬性
    def hungry(self):
        return "肚子餓的時候，就吃點點心吧!"
    def sleep(self):
        return "想睡覺的時候，會找舒服的地方睡。"
    
dog1=Animal("柯基",3) #多型
print(f"這隻動物是{dog1.variety},今年{dog1._Animal__age}歲。牠{dog1.sleep()}") #_Animal__age訪問私有屬性
print(dog1.hungry())
print()

dog2=Animal("牧羊犬",2) #多型
print(f"這隻動物是{dog2.variety},今年{dog2._Animal__age}歲。牠{dog2.sleep()}")
print(dog2.hungry())
print()

class Cat(Animal): #繼承
    def __init__(self,color):
        self.color=color
    def bark(self):
        return "喵喵~"
    
cat=Cat("黑色")
print(f"這隻動物的毛色是{cat.color},牠的叫聲是{cat.bark()}")

cat=Animal("波斯貓",5)
print(f"牠是一隻{cat.variety},今年{cat._Animal__age}歲。")
print(cat.hungry())
print()

class Bird(Cat): #多層繼承
    def __init__(self,move):
        self.move=move
    def bark(self):
        return "啾啾!啾啾!" #覆蓋bark() method
    
bird=Bird("飛行")
print(f"這隻動物移動的方式是{bird.move}。牠的叫聲是{bird.bark()}")

bird=Cat("咖啡色")
print(f"牠的毛色是{bird.color}。")
bird=Animal("麻雀",1)

print(f"牠是一隻{bird.variety},今年{bird._Animal__age}歲。")
print(bird.sleep())