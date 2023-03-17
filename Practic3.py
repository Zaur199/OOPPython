#Декоратор @staticmethod
class Math:
    ARG = 2

    # def super_sum(self, a, b):
    # return (a+ b) * a * b

    @staticmethod
    def super_sum(a, b):
        print(__class__)
        # return Math.ARG + (a+ b) * a * b
        return __class__.ARG + (a + b) * a * b


class A(Math):
    def super_sum(a, b):
        print(__class__)
        return a + b


#m = Math()
print(Math.super_sum(10, 30))
print(A.super_sum(10, 30))
