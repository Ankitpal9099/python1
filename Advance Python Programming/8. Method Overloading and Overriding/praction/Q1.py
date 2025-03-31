#  Write a Python program to show method overloading. 

class math:
    def add(self,a,b=0,c=0,d=0):
        return a+b+c+d
    def sub(self,a,b=0,c=0,d=0):
        return a-b-c-d
    def mul(self,a,b=1,c=1,d=1):
        return a*b*c*d
maths=math()
print("sum of two numbers:",maths.add(2,3))
print("sum of three numbers:",maths.add(2,3,4))
print("sum of four numbers:",maths.add(2,3,4,5))
print("sum of two numbers:",maths.sub(2,3))
print("sum of three numbers:",maths.sub(2,3,4))
print("sum of four numbers:",maths.sub(2,3,4,5))
print("sum of two numbers:",maths.mul(2,3))
print("sum of three numbers:",maths.mul(2,3,4))
print("sum of four numbers:",maths.mul(2,3,4,5))
