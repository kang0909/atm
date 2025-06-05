# 잔액 초기화, 통장 잔고
balance = 1000

while True:# 조건이 True면 계속 작동합니다.
    num = input('사용하실 번호을 선택해주세요 (1.입금, 2.출금, 3.영수증보기, 4.종료): ')
    #2번 출금 기능 코드
    if num == '2':
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : "))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        print(f'출금하신 금액은 {withdraw_amount}원 이고, 현재 잔액은 {balance}원 입니다')

    #1번 입금 기능 코드
    if num == '1':
        #얼마를 입금할거야?
        deposit_amount = int(input("입금할 금액을 입력해주세요 : "))
        #balance
        balance += deposit_amount
        print(f'입금하신 금액은 {deposit_amount}원 이고, 현재 잔액은 {balance}원 입니다')

    #4번 종료 기능 코드
    if num == '4':
        print('종료')
        break
    #3번 영수증 보기 코드
    if num == '3':
        print('영수증보기')
# 목차 = {"1.입금", "2.출금", "3.영수증 보기", "4.종료"}


