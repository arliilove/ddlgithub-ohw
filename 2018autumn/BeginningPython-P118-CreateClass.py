#创建一个类，P118**********************
__metaclass__ = type #确定使用新式类

class Person:

    def setName(self,name):#注意self参数
        self.name = name
        
    def getName(self):
        return self.name
    
    def greet(self):
        print("Hello, world! I'm %s."%self.name)
#**************************************************
#创建一些类的实例
foo = Person()
bar = Person()
foo.setName("Luke Skywalker") #在调用setName方法时，foo自动将自己作为第一个参数传入方法中
bar.setName("Anak in Skywalker")
foo.greet()
Person.greet(foo)#这种写法也是可以的，事实上，上面一句正式本行的简单写法
bar.greet()
Person.greet(bar)

foo.name = "Yoda"
print(foo.name) #类的特性还可以在外部访问

def func():
    print("This is a common function!")

foo.getName = func #可以将类的特性绑定到一个普通函数上

foo.getName()

func2 = foo.greet #可以将一个普通变量绑定到特性上
func2()
print(type(foo))

print(hasattr(foo,"setName")) #检查对象的某个方法是否存在
print(hasattr(foo.setName,"__call__"))#检查对象某个方法是否可调用
print(getattr(foo,"name",None)) #获取对象的某个特性的值
print(getattr(foo,"setName",None))#获取对象的某个方法的描述
setattr(foo,"name","Mr. Gumby")#设置对象的某个特性
print(foo.name)
