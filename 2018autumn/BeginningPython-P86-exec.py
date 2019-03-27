#执行结果与课本描述不同
from math import sqrt
scope = {}
exec('"sqrt = 1" in scope')
print("sqrt(4) =",sqrt(4))
print("length of scope = ",len(scope))
print("scope.keys():",scope.keys())
