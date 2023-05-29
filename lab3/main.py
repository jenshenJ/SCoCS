from custom_serializer import SerializerFactory

class A:
    a = 1


    @property
    def get_a(self):
        return self.a

if __name__ == '__main__':
    xml = SerializerFactory.serializer('xml')
    a = A()
    ser = xml.dumps(a)
    des = xml.loads(ser)
    print(des.get_a)    
