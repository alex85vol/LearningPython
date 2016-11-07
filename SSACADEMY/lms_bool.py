# -*- coding: cp1251 -*-
'''
@author: lhalam
'''
print('�������� ���'), type(bool)
x=bool(True)
print "x ", x, type(x)
y= False
print "y ", y, type(y)

print "\tx+y ", x+y, type(x+y)
print "\tx+x ", x+x, type(x+x)
print "\ty+y ", y+y, type(y+y)
print "\tx*y ", x*y, type(x**y)
print "\tx*x ", x*x, type(x**x)
print "\ty*y ", y*y, type(y**y)
print "\tx**y ", x**y, type(x**y)
print "\tx**x ", x**x, type(x**x)
print "\ty**y ", y**y, type(y**y)
print "\tx>y ", x>y, type(x>y)
print "\tx>x ", x>x, type(x>x)
print "\ty>y ", y>y, type(y<y)
print "\tx<=y ", x<=y, type(x<=y)
print "\tx<=x ", x<=x, type(x<=x)
print "\ty<=y ", y<=y, type(y<=y)
print "\tx==y ", x==y, type(x==y)
print "\tx==x ", x==x, type(x==x)
z = x+1
print "z",z,type(z)
print "\tx==(x+1) ", x==(x+1), type(x==(x+1))
print "\tx==z ", x==z, type(x==z)
print "\tx==bool(z) ", x==bool(z), type(x==bool(z))


#error
x/y
x//y
x%y