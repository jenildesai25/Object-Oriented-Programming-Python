class MyClass:

    def object_method(self):
        print('object method')

    @classmethod
    def class_method(cls):
        return 'data from class method'

    @staticmethod
    def static_method(d):
        return 'data' + d


if __name__ == '__main__':
    my_class = MyClass()
    my_class.object_method()
    result = MyClass.class_method()
    print(result)
    res = MyClass.static_method(result)
    print(res)
