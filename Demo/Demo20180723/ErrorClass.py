class FooError(ValueError):
    pass

def Foo(s):
    n = int(s)
    if n==0:
        raise FooError('incalid value:%s' % s)
    return 10 / n

Foo('0')