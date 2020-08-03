[Python学习网址](https://www.runoob.com/python3/python3-tutorial.html)
# Python3基本语法
## 编码
*   默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。
## 标识符
*   第一个字符必须是字母表中字母或下划线 _ 。
*   标识符的其他的部分由字母、数字和下划线组成。
*   标识符对大小写敏感。
*   在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的
## 保留字/关键字/keywords
*   保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
```python
import keyword
keyword.kwlist
```
## 注释
*   Python中单行注释以 # 开头，实例如下：
```python
#第一个注释
print("Hello python") #第二个注释
```
*   多行注释可以使用多个#，或者'''或者"""，例如
```python
#第一个注释
#第二注释
'''
第三个注释
第四个注释
'''
"""
第五个注释
第六个注释
"""
print("Hello,python!")
```
## 行与缩进
*   **python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。**
*   缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
```python
if True:
    print ("True")
else:
    print ("False")
```
## 多行语句
*   Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
```python
total = item_one + \
        item_two + \
        item_three
```
*   在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
```python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```
## 空行
* 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
* 类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
* 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
* **记住**：空行也是代码的一部分。
## 等待用户输入
*   执行下面的程序就会等待用户输入，一旦用户按下回车键，程序就会退出
```python
myinput = input("请输入，按下enter键后退出")
print(myinput)
```
## 同一行键入多条语句
*   Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
```python
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```
## 多个语句构成代码组
*   缩进相同的一组语句构成一个代码块，我们称之代码组
*   像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。我们将首行及后面的代码组称为一个子句(clause)。
*   如下实例：
```python
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```
## Print输出
*   print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 **end=""：**
```python
#!/usr/bin/python3
 
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
```
## import与from...import
* 在 python 用 **import** 或者 **from...import** 来导入相应的模块。
* 将整个模块（例如time）导入，格式为：```import time```，调用函数的格式为：```time.sleep(1)```
* 从某个模块（例如time）中导入所有函数，格式为：```from time import *```，调用函数的格式为：```sleep(1)```
* 从某个模块（例如time）中导入某个函数，格式为：```from time import sleep```，调用函数的格式为：```sleep(1)```
* 将模块（例如time）换个别名引入，格式为：```import time as abc```，调用函数的格式为：```abc.sleep(1)```
* 代码举例：
```python
#导入sys模块
import 

print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
#导入sys模块的argv、path成员
from sys import argv,path

print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
```
## help函数
* 调用 python 的 help() 函数可以打印输出一个函数的文档字符串：
```python
# 如下实例，查看内置函数 max 的参数列表和规范的文档
help(max)
```
# Python3基本数据类型
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
```python
#!/usr/bin/python3

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)
```
## 多个变量赋值
Python允许你同时为多个变量赋值。例如：
```python
a = b = c = 1
```
以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
您也可以为多个对象指定多个变量。例如：
```python
a, b, c = 1, 2, "runoob"
```
以上实例，两个整型对象 1 和 2 分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。
*   *   *   
## 标准数据类型
Python3 中有六个标准的数据类型：
* Number(数字)
* String(字符串)
* List(列表)
* Tuple(元组)
* Set(集合)
* Dictionary(字典)
Python3 的六个标准数据类型中：
* **不可变数据(3个)：**Number（数字）、String（字符串）、Tuple（元组）；
* **可变数据(3个)：**List（列表）、Dictionary（字典）、Set（集合）。
*   *   *   
## Number(数字)
Python3 支持 **int、float、bool、complex（复数）**。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
内置的 type() 函数可以用来查询变量所指的对象类型。
```python
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
```
此外还可以用 isinstance 来判断：
```python
a = 111
print(isinstance(a,int))
```
isinstance 和 type 的区别在于：
* type()不会认为子类是一种父类类型。
* isinstance()会认为子类是一种父类类型。
*   *   *   
***注意*** ：*在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。*
*   *   *   
当你指定一个值时，Number 对象就会被创建：
```python
var1 = 1
var2 = 10
```
您可以使用del语句删除一些对象引用，也可以通过使用del语句删除单个或多个对象。例如：
```python
del var1
del var_a,var_b
```
**注意：**
1. Python可以同时为多个变量赋值，如a, b = 1, 2。
2. 一个变量可以通过赋值指向不同类型的对象。
3. 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4. 在混合计算时，Python会把整型转换成为浮点数。
5. Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
*   *   *   
## 字符串
Python中的字符串用单引号 ``` '```  或双引号```  "  ```括起来，同时使用反斜杠 ``` \ ``` 转义特殊字符。
字符串的截取的语法格式如下：
```变量[头下标:尾下标]```
索引值以 0 为开始值，-1 为从末尾的开始位置。
加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。实例如下：
```python
#!/usr/bin/python3  
  
str  =  'Runoob'  
  
print  (str)  # 输出字符串  
print  (str[0:-1])  # 输出第一个到倒数第二个的所有字符  
print  (str[0])  # 输出字符串第一个字符  
print  (str[2:5])  # 输出从第三个开始到第五个的字符  
print  (str[2:])  # 输出从第三个开始的后的所有字符  
print  (str * 2)  # 输出字符串两次，也可以写成 print (2 * str)  
print  (str + "TEST")  # 连接字符串
```
Python 使用反斜杠``` \ ```转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个``` r(raw)```，表示原始字符串：
```python
print('Ru\noob')  
print(r'Ru\noob') 
word = "Python"
print(word[0], word[5])
print(word[-1], word[-6]) 
```
**注意**：*Python 没有单独的字符类型，一个字符就是长度为1的字符串。*
与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
**注意：**
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
- 字符串可以用+运算符连接在一起，用*运算符重复。
- Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
- Python中的字符串不能改变。
## 列表
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
***列表是写在方括号  []  之间、用逗号分隔开的元素列表。***
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。列表截取的语法格式如下：
```
变量[头下标:尾下标]
```
索引值以 0 为开始值，-1 为从末尾的开始位置。
![列表截取示意图](PythonLearningNotes_md_files/list_slicing1.png?v=1&type=image)
加号 ```+ ```是列表连接运算符，星号``` * ```是重复操作。如下实例：
```python
#!/usr/bin/python3  
  
list  =  [  'abcd',  786  ,  2.23,  'runoob',  70.2  ]  
tinylist =  [123,  'runoob']  
  
print  (list)  # 输出完整列表  
print  (list[0])  # 输出列表第一个元素  
print  (list[1:3])  # 从第二个开始输出到第三个元素  
print  (list[2:])  # 输出从第三个元素开始的所有元素  
print  (tinylist * 2)  # 输出两次列表  
print  (list + tinylist)  # 连接列表
```
与Python字符串不一样的是，列表中的元素是可以改变的：
```python
>>> a =  [1,  2,  3,  4,  5,  6]  
>>> a[0]  =  9  
>>> a[2:5]  =  [13,  14,  15]  
>>> a  
[9,  2,  13,  14,  15,  6]  
>>> a[2:5]  =  []  # 将对应的元素值设置为 []  
>>> a  
[9,  2,  6]
```
**注意：**
-   1、List写在方括号之间，元素用逗号隔开。
-   2、和字符串一样，list可以被索引和切片。
-   3、List可以使用+操作符进行拼接。
-   4、List中的元素是可以改变的。
Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
![输入图片描述](PythonLearningNotes_md_files/python_list_slice_2.png?v=1&type=image)
如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
```python
def reverseWords(input):  
  
# 通过空格将字符串分隔符，把各个单词分隔为列表  
inputWords =  input.split(" ")  
  
# 翻转字符串  
# 假设列表 list = [1,2,3,4],  
# list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)  
# inputWords[-1::-1] 有三个参数  
# 第一个参数 -1 表示最后一个元素  
# 第二个参数为空，表示移动到列表末尾  
# 第三个参数为步长，-1 表示逆向  
inputWords=inputWords[-1::-1]  
  
# 重新组合字符串  
output =  ' '.join(inputWords)  
  
return output  
  
if __name__ ==  "__main__":  
input  =  'I like runoob'  
rw = reverseWords(input)  
print(rw)
```
## Tuple(元组)
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在**小括号** ```()```  里，元素之间用逗号隔开。
**元组中的元素类型也可以不相同**：
```python
#!/usr/bin/python3  
  
tuple  =  (  'abcd',  786  ,  2.23,  'runoob',  70.2  )  
tinytuple =  (123,  'runoob')  
  
print  (tuple)  # 输出完整元组  
print  (tuple[0])  # 输出元组的第一个元素  
print  (tuple[1:3])  # 输出从第二个元素开始到第三个元素  
print  (tuple[2:])  # 输出从第三个元素开始的所有元素  
print  (tinytuple * 2)  # 输出两次元组  
print  (tuple + tinytuple)  # 连接元组
```
元组与**字符串**类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
其实，可以把字符串看作一种特殊的元组。
```python
>>> tup =  (1,  2,  3,  4,  5,  6)  
>>>  print(tup[0])  
1  
>>>  print(tup[1:5])  
(2,  3,  4,  5)  
>>> tup[0]  =  11  # 修改元组元素的操作是非法的  
Traceback (most recent call last):  
File "<stdin>", line 1,  in  <module>  
TypeError: 'tuple'  object does not support item assignment  
>>>
```
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
```python
tup1 = ()
tup2 =(20,)
```
string、list和tuple都属于sequence序列
**注意**：
-   1、与字符串一样，元组的元素不能修改。
-   2、元组也可以被索引和切片，方法一样。
-   3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
-   4、元组也可以使用+操作符进行拼接。
## Set(集合)
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。基本功能是进行成员关系测试和删除重复元素。
可以使用大括号  { }  或者  set()  函数创建集合，注意：创建一个空集合必须用 set()  而不是  { }，因为  { }  是用来创建一个空字典。

创建格式：
```python
parame =  {value01,value02,...} 
set(value)
```
**实例**
```python
#!/usr/bin/python3  
  
sites =  {'Google',  'Taobao',  'Runoob',  'Facebook',  'Zhihu',  'Baidu'}  
  
print(sites)  # 输出集合，重复的元素被自动去掉  
  
# 成员测试  
if  'Runoob'  in sites :  
	print('Runoob 在集合中')  
else :  
	print('Runoob 不在集合中')  
# set可以进行集合运算  
a =  set('abracadabra')  
b =  set('alacazam')  
print(a)   
print(a - b)  # a 和 b 的差集  
print(a | b)  # a 和 b 的并集   
print(a & b)  # a 和 b 的交集   
print(a ^ b)  # a 和 b 中不同时存在的元素
```
## Dictionary(字典)
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用  { }  标识，它是一个无序的  **键(key) : 值(value)**  的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
**实例**
```python
#!/usr/bin/python3  
  
dict  =  {}  
dict['one']  =  "1 - 菜鸟教程"  
dict[2]  =  "2 - 菜鸟工具"   
tinydict =  {'name': 'runoob','code':1,  'site': 'www.runoob.com'}  
print  (dict['one'])  # 输出键为 'one' 的值  
print  (dict[2])  # 输出键为 2 的值  
print  (tinydict)  # 输出完整的字典  
print  (tinydict.keys())  # 输出所有键  
print  (tinydict.values())  # 输出所有值
```
构造函数 dict() 可以直接从键值对序列中构建字典如下：
**实例**
```python
>>>  dict([('Runoob',  1),  ('Google',  2),  ('Taobao',  3)])  
{'Runoob': 1,  'Google': 2,  'Taobao': 3}  
>>>  {x: x**2  for x in  (2,  4,  6)}  
{2: 4,  4: 16,  6: 36}  
>>>  dict(Runoob=1, Google=2, Taobao=3)  
{'Runoob': 1,  'Google': 2,  'Taobao': 3}  
>>>
```
**注意：**

-   1、字典是一种映射类型，它的元素是键值对。
-   2、字典的关键字必须为不可变类型，且不能重复。
-   3、创建空字典使用  **{ }**。
## python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
# python注释
以下实例可以输出函数的注释：
```python
def a():
  '''这是文档字符串'''  
  pass  
print(a.__doc__)
```
# python 3运算符
## python算术运算符
|运算符|描述  |
|--|--|
|+|加 - 两个对象相加|
|-|减 - 得到负数或是一个数减去另一个数
|*|乘 - 两个数相乘或是返回一个被重复了若干次的字符串
|/|除 - x除以y
|%|取模 - 返回除法的余数
|**|幂 - 返回x的y次幂
|//|取整除 - 向下取接近商的整数
以下实例演示了Python所有算术运算符的操作：
**实例**
```python
#!/usr/bin/python3  
a = 21  
b = 10  
c = 0  
c = a + b  
print  ("1 - c 的值为：", c)  
c = a - b  
print  ("2 - c 的值为：", c)  
c = a * b  
print  ("3 - c 的值为：", c)  
c = a / b  print  ("4 - c 的值为：", c)  
c = a % b  print  ("5 - c 的值为：", c)  
# 修改变量 a 、b 、c  
a = 2  
b = 3  
c = a**b  
print  ("6 - c 的值为：", c)  
a = 10  
b = 5  
c = a//b  
print  ("7 - c 的值为：", c)
```
## python比较运算符
|==|等于 - 比较对象是否相等|
|--|--|
|!=|不等于 - 比较两个对象是否不相等
|>|大于 - 返回x是否大于y
|<|小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。
|>=|大于等于 - 返回x是否大于等于y
|<=|小于等于 - 返回x是否小于等于y
## python赋值运算符
|运算符|描述|实例|
|--|--|--|
|=|简单的赋值运算符
|+=|加法赋值运算符
|-=|减法赋值运算符
|*=|乘法赋值运算符
|/=|除法赋值运算符
|%=|取模赋值运算符
|**=|幂赋值运算符
|//=|取整除赋值运算符
|:=|海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**。|在这个示例中，赋值表达式可以避免调用 len() 两次:<br><code>if  (n := len(a))  >  10:	print(f"List is too long ({n} elements, expected <= 10)") </code>
## python位运算符
|运算符|描述|
|--|--|
|&|按位与运算符
|&#124;|按位或运算符|
|^|按位异或运算符
|~|按位取反运算符
|<<|左移运算符
|>>|右移运算符
## python逻辑运算符
|运算符|描述|
|--|--|
|and|布尔"与"|
|or|布尔"或"|
|not|布尔"非"|
## python成员运算符
Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
|运算符|描述|
|--|--|
|in|如果在指定的序列中找到值返回 True，否则返回 False。
|not in|如果在指定的序列中没有找到值返回 True，否则返回 False。
**实例**：
```python
#!/usr/bin/python3  
a = 10  
b = 20  
list = [1, 2, 3, 4, 5  ]; 
if  (  a  in  list  ): 
	print  ("1 - 变量 a 在给定的列表中 list 中")  
else: 
	print  ("1 - 变量 a 不在给定的列表中 list 中")  
if  (  b  not  in  list  ):
	print  ("2 - 变量 b 不在给定的列表中 list 中")  
else: 
	print  ("2 - 变量 b 在给定的列表中 list 中")  # 修改变量 a 的值  a = 2  
if  (  a  in  list  ): 
	print  ("3 - 变量 a 在给定的列表中 list 中")  
else: 
	print  ("3 - 变量 a 不在给定的列表中 list 中")
```
## python身份运算符
身份运算符用于比较两个对象的存储单元。
|运算符|描述|
|--|--|
|is|s 是判断两个标识符是不是引用自一个对象|
|is not|is not 是判断两个标识符是不是引用自不同对象
**注：** [id()](https://www.runoob.com/python/python-func-id.html)  函数用于获取对象内存地址。
以下实例演示了Python所有身份运算符的操作：
```python
#!/usr/bin/python3 
a = 20  
b = 20 
if  (  a  is  b  ): 
	print  ("1 - a 和 b 有相同的标识")  
else:
	print  ("1 - a 和 b 没有相同的标识") 
if  (  id(a) == id(b)  ): 
	print  ("2 - a 和 b 有相同的标识")  
else: 
	print  ("2 - a 和 b 没有相同的标识")  
# 修改变量 b 的值  
b = 30  
if  (  a  is  b  ): 
	print  ("3 - a 和 b 有相同的标识")  
else: 
	print  ("3 - a 和 b 没有相同的标识")  
if  (  a  is  not  b  ): 
	print  ("4 - a 和 b 没有相同的标识")  
else:
	print  ("4 - a 和 b 有相同的标识")
```
*is 与 == 区别：*
*is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。*


