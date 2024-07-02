'''
class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def method1(self):
        #메서드 동작 정의
        print(f"{self.param1} * {self.param2}={self.param1 * self.param2}")
        print(f"{self.param1}+{self.param2}={self.param1+self.param2}")
    def method2(self):
        #메서드 동작 정의
        pass
    
cal = MyClass(10,11)
cal.method1()
num = MyClass(7,9)
num.method2()
'''
'''
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def name_method(self):
        return self.name
    def age_method(self):
        return self.age
    
result = People("홍길동", 33)
print("이름은 : ", result.name_method())
print("나이는 : ", result.age_method())
'''
'''
#계산기 클래스 -> 곱하기(muliply) & 나누기(divide) 메소드 추가하기
class cal:
    def __init__(self):
        
    def muliply(self, num1 , num2):
        self.result = num1 * num2
    def divide(self, num1 , num2):
        self.result = num1 / num2
c = cal()
c.muliply(30, 2)
c.divide(10, 2)
print("곱하기 : " , c.muliply)
print("나누기 : ", c.divide)
'''          
#직사각형 클래스를 만들어 보세요.
'''
class square:
    def __init__(self, width, height):
        self.width = width  #self.width = 0
        self.height = height  #self.height = 0
                                #self.result = 0
    def cal_method(self, width, height):
        self.result = width * height
        
a = square(0,0)
a.cal_method(25,6)   #a.width = int(input())
print("넓이 : ", a.result)
'''            
'''       
class square:
    def __init__(self, width, height):
        self.width = width  #self.width = 0
        self.height = height  #self.height = 0
                                #self.result = 0
    def cal_method(self):
        result = self.width * self.height
        return result      
a = square(45, 7)
print(a.cal_method())          
 '''           
class library:
    def __init__(self, 도서명, 저자, 출판사, 출판연도):
        self.도서명 = 도서명
        self.저자 = 저자
        self.출판사 = 출판사
        self.출판연도 = 출판연도
    def info(self):
        print(f"도서명 : {self.도서명}, 저자 : {self.저자}, 출판사 : {self.출판사}, 출판연도 : {self.출판연도}")
        #return self.도서명, self.저자, self.출판사, self.출판연도
x = library('치명적 자만', '프리드리히 하이에크', '민음사', '2010년')
x.info()