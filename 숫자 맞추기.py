print('0~20까지 숫자중 아무 숫자를 말하세요 :')
a = str(input())
while True:
    print('1번이 말한 숫자를 예측하여 말해보세요 :')
    b = str(input())
    

    if a - b < 0:
        print('더 큽니다 더 작은수를 입력하세요.')
    elif a - b > 0:
        print('더 작습니다 더 큰수를 입력하세요.')

    else:
        print("정답입니다")
        break
        

