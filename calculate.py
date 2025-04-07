### 사칙연산 함수 정의

def plus(a,b):
    return int(a) + int(b)

def minus(a,b):
    return int(a) - int(b)

def mul(a,b):
    return int(a) * int(b)

def divide(a,b):
    return int(a) / int(b)

if __name__ == '__main__':

    ### 사용자 입력
    print('\n첫번째 숫자를 입력하세요.')
    num1 = input('입력: ')

    print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
    operator = input('기호: ')

    print('\n두번째 숫자를 입력하세요.')
    num2 = input('입력: ')


    ### 연산 수행
    if operator == '+':
        result = plus(num1, num2)
    elif operator == '-':
        result = minus(num1, num2)
    elif operator == '*':
        result = mul(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    print('사칙연산 결과는 {result}입니다.')
    ##흠 주석 잘 들어감?
    ### 시진핑 주석.
    ### 시진핑핑이<-write By 권.
    ## 난 그사람 얼굴도 몰라
    ### 진짜에요?
    #### 증거를 다 남겨야돼
    ##흠 이제야 산다 했군
    