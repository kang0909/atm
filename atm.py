# 잔액 초기화
balance = 1000

while True:# 조건이 True면 계속 작동합니다.
    num = input('사용하실 번호을 선택해주세요 (1.입금, 2.출금, 3.영수증보기, 4.종료): ')

    if num == '2':
        print('출금')

    if num == '1':
        print('입금')

    if num == '4':
        print('종료')
        break

    if num == '3':
        print('영수증보기')
# 목차 = {"1.입금", "2.출금", "3.영수증 보기", "4.종료"}


