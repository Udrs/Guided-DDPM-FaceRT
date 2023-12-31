import numpy as np

a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape((2,2))
print(a)
'''
[[1 1]
 [0 1]]
'''
print(b)
'''
[[0 1]
 [2 3]]
'''
# 多维度矩阵乘法
# 第一种乘法方式:
c = a.dot(b)
print(c)
# 第二种乘法:
c = np.dot(a,b)
print(c)
'''
[[2 4]
 [2 3]]
'''
# 多维矩阵乘法不能直接使用'*'号
 
a = np.random.random((2,4)) # 2*4 矩阵，0到1的随机数
 
print(np.sum(a)) # 3.657010765991042
print(np.min(a)) # 0.10936760904735132
print(np.max(a)) # 0.9476048882750654
 
print("a=",a)
'''
a= [[0.16607436 0.94760489 0.59649117 0.22698245]
 [0.66494464 0.23447984 0.10936761 0.71106581]]
'''
 
print("sum=",np.sum(a,axis=1)) # sum= [1.93715287 1.7198579 ]
print("min=",np.min(a,axis=0)) # min= [0.16607436 0.23447984 0.10936761 0.22698245]
print("max=",np.max(a,axis=1)) # max= [0.94760489 0.71106581]
 
'''
如果你需要对行或者列进行查找运算，
就需要在上述代码中为 axis 进行赋值。
当axis的值为0的时候，将会以列作为查找单元，即竖列
当axis的值为1的时候，将会以行作为查找单元。即横行
不写axis时，对所有元素处理
'''