from custom_serializer import SerializerFactory
import math



def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = SerializerFactory.serializer('json')
#
# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)
#
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def f(a):
    for i in a:
        yield i


g = f([1, 2, 3])
print(next(g))
g_s = ser.dumps(g)
g_d = ser.loads(g_s)
print(next(g_d))

d = lambda x: x * x
d_s = ser.dumps(d)
d_d = ser.loads(d_s)
print(d_d(2))

def rec(deep):
    if deep == 5:
        return
    else:
        print(deep)
        rec(deep + 1)
    
rec(0)
rec_s = ser.dumps(rec)
rec_d = ser.loads(rec_s)
rec_d(0)