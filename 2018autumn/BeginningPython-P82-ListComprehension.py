#列表推导式——轻量级循环
list1 = [x*x for x in range(10)]
print("list1 =",list1)
list2 = [x*x for x in range(10) if x % 3 == 0]
print("list2 =",list2)
list3 = [(x,y) for x in range(3) for y in range(3)]
print("list3 =",list3)

#使用如下代码双重循环也可以创建list3
list3 = []
for x in range(3):
    for y in range(3):
        list3.append((x,y))
print("list3 =",list3)

#与if子句联合使用，像之前list2一样的
girls = ["alice","bernice","clarice"]
boys = ["chris","arnold","bob"]
list4 = [b + "+" + g for b in boys for g in girls if b[0] == g[0]]
print ("list4 =",list4)

#上面这段代码其实效率不高，因为它要搜索所有可能的配对，Python有很多解决这种问题的方法
girls = ["alice","bernice","clarice"]
boys = ["chris","arnold","bob"]
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print("letterGirls =",letterGirls)
list4 = [b + "+" + g for b in boys for g in letterGirls[b[0]]]
print("list4 =",list4)
