'''
def ask_ok(prompt, retries=4, reminder='다시 시도해주세요!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n','no','nop','nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
ask_ok('정말 끝내길 원하세요?')
ask_ok('파일을 덮어써도 좋습니까?',2)
ask_ok('파일을 덮어써도 좋습니까?', 2, 'y or n로 답하세요!')
'''
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num2
        
    return total
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))

  
  