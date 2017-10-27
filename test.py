## 使用@staticmethod产生静态函数，静态函数不是绑定在实例上，可以吧实例化直接使用
## 父类
class NEW_Classs():
    def __init__(self):
        self.x = 1
        self.y = 2
    @staticmethod##
    def add(a,b):
        return a+b
## 子类继承
class S(NEW_Classs):
    def __init__(self):
        self.x =2
        self.y =3

P = NEW_Classs()
###常规类的继承要实例化
Q = S()
print(Q.x)
## 静态函数的继承使用
print(S.add(Q.x,Q.y))
l_0 = P.add(P.x,P.y)
l_1 = NEW_Classs.add(2,1)
print(l_0,end=' ')
print(l_1,end=' ')