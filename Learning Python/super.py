class A:
    def method(self):
        print('A.method')


class Mixin(A):
    def method(self):
        print('Mixin.method')
        super().method()
        # A.method(self)


class B(A):
    def method(self):
        print('B.method')


class C(Mixin, B):
    def method(self):
        print('C.method')
        super().method()


class D(B, Mixin):
    def method(self):
        print('D.method')
        super().method()

# Mixin().method()
C().method() # ⽆法使⽤ A.method
# D().method()

