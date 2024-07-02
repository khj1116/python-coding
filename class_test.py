#신호등 클래스

class traffic_light:
    def __init__(self, color):
        self.color = color
    def do(self):
        if self.color == 'red':
            self.next_color = 'yellow'
            print('멈추고 기다리세요')
        elif self.color == 'yellow':
            self.next_color = 'green'
            print('멈출 준비하세요')
        elif self.color == 'green':
            self.next_color = 'red'
            print('출발하세요!')
        else :
            self.next_color = '고장'
            print('수리를 요합니다. ')
            
for c in ['red', 'yellow', 'green', 'error']:
    c = traffic_light(c)
    print(c.color)
    c.do()
    print(c.next_color)
    print('\n')            

'''
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, x, y):
        self.result = x + y
    def subtract(self, x, y):
        self.result = x - y
# 클래스 인스턴스 생성
calc = Calculator()              
 # 메서드 호출
calc.add(8, 4)
print("Additional result:", calc.result)

calc.subtract(10,6)
print("Subtraction result:", calc.result)
'''
'''
class cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def muliply(self, num1 , num2):
        self.result1 = num1 * num2
    def divide(self, num1 , num2):
        self.result2 = num1 / num2
c = cal(0,0)
c.muliply(30, 2)
c.divide(10, 2)
print("곱하기 : " , c.result1)
print("나누기 : ", c.result2)
'''

class bank:
    def __init__(self, balance, number):
        self.balance = balance
        self.number = number
    def bal_withdraw(self, balance, number):
        self.withdraw = balance - number
        return self.withdraw 
    def bal_deposit(self, balance, number):
        self.deposit = balance + number
        return self.deposit
b = bank(10,10)

print(f"출금 후 통장 잔액 : ",b.bal_withdraw(100, 40))
print(f"입금 후 통장 잔액: ",b.bal_deposit(100, 80))
