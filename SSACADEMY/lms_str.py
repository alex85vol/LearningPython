# -*- coding: cp1251 -*-
'''
@author: lhalam
'''
print('�������� ���'), type("type"), type(u"type")

x= "P���� str"
print "x ", x, type(x), "������� �����:", len(x)
print "\tx+x ", x+x, type(x+x)
print "\tx*3 ", x*3, type(x*3)
print "\tx[0] ", x[0], type(x[0])
print "\tx[8] ", x[8], type(x[8])
print "\tx[-1] ", x[-1], type(x[-1])
print "\tx[-0] ", x[-0], type(x[-0]) # -0 == 0
print "\tx[0:3] ", x[0:3], type(x[0:3]), "������� �����:", len(x[0:3])
print "\tx[-3:-1] ", x[-3:-1], type(x[-3:-1]), "������� �����:", len(x[-3:-1])
print "\tx[-1:-3] ", x[-1:-3], type(x[-1:-3]), "������� �����:", len(x[-1:-3])
print "\tx[:-1] ", x[:-1], type(x[:-1]), "������� �����:", len(x[:-1])
print "\tx[-3:] ", x[-3:], type(x[-3:]), "������� �����:", len(x[-3:])
print "\tx[:] ", x[:], type(x[:]), "������� �����:", len(x[:])
print "\tx[:5]+'STR'", x[:5]+'STR', type(x[:5]+'STR'), "������� �����:", len(x[:5]+'STR')
print "\tx.upper()", x.upper(), type(x.upper()), "������� �����:", len(x.upper())
print "\tx.find('s')", x.find('s'), type(x.find('s'))
print "\tx.find('str')", x.find('str'), type(x.find('str'))
print "\tx.decode('unicode-escape')", x.decode('unicode-escape'), type(x.decode('unicode-escape'))

u= u"P���� Unicode"
print "\nx ", u, type(u), "������� �����:", len(u)
print "\tu+u ", u+u, type(u+u)
print "\tu*3 ", u*3, type(u*3)
print "\tu[0] ", u[0], type(u[0])
print "\tu[8] ", u[8], type(u[8])
print "\tu[-1] ", u[-1], type(u[-1])
print "\tu[-0] ", u[-0], type(u[-0]) # -0 == 0
print "\tu[0:3] ", u[0:3], type(u[0:3]), "������� �����:", len(u[0:3])
print "\tu[-3:-1] ", u[-3:-1], type(u[-3:-1]), "������� �����:", len(u[-3:-1])
print "\tu[-1:-3] ", u[-1:-3], type(u[-1:-3]), "������� �����:", len(u[-1:-3])
print "\tu[:-1] ", u[:-1], type(u[:-1]), "������� �����:", len(u[:-1])
print "\tu[-3:] ", u[-3:], type(u[-3:]), "������� �����:", len(u[-3:])
print "\tu[:] ", u[:], type(u[:]), "������� �����:", len(u[:])
print "\tu[:5]+'STR'", u[:5]+'STR', type(u[:5]+'STR'), "������� �����:", len(u[:5]+'STR')
print "\tu.upper()", u.upper(), type(u.upper()), "������� �����:", len(u.upper())
print "\tu.find('s')", u.find('s'), type(u.find('s'))
print "\tu.find('str')", u.find('str'), type(u.find('str'))
print "\tu.encode('ascii','ignore')",u.encode('ascii','ignore'),\
      type(u.encode('ascii','ignore')), "������� �����:", len(u.encode('ascii','ignore'))
print "\tu.encode('ascii','replace')",u.encode('ascii','replace'),\
      type(u.encode('ascii','replace')), "������� �����:", len(u.encode('ascii','replace'))
print "\tu.encode('utf8')",u.encode('utf8'),\
      type(u.encode('utf8')), "������� �����:", len(u.encode("utf8"))

print "Str" + u'Unicode' "Fin"


#error

#x**3
x[9]
#x[5]='error'
x+u