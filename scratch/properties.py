class A(object):
    def __init__(self, foo):
        self.foo = foo

    @property
    def bar(self):
        print "returning foo"
        return self.foo

print A('blah').bar
