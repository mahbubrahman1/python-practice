class A:

    def class1(self):
        print("this is class one")

    def class3(self):
        print("this is class three")


class B(A):

    def class5(self):
        print("this is class five")

    def class4(self):
        print("this is class four")


class C(B):

    def class6(self):
        print("this is class six")

    def class10(self):
        print("this is class ten")


both = C()
both.class1()
both.class3()
both.class5()
both.class4()
both.class6()
both.class10()


class A:

    def class1(self):
        print("this is class one")

    def class3(self):
        print("this is class three")


class B(A):

    def class5(self):
        print("this is class five")

    def class4(self):
        print("this is class four")


class C(B):

    def first(self):
        super().class1()
        super().class3()
        super().class5()
        super().class4()
        print("this is one, three, four, five")


both = C()
both.first()
