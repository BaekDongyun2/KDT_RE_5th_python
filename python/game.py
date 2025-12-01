# 초기상태 설정
player_name = input("당신의 이름은 무엇입니까?: ")
health = 100
inventory = []

print(f"{player_name}님, 7days에 참여하신 것을 환영합니다.")
print(f"초기 체력: {health}\nHello, world!")

# 1일차 (월요일)

print("[1일차 / 월요일] 배고픈 아침입니다.\n 먹다남은 사과를 발견했습니다.")

while True:
    eat_eaten_apple = input("먹다남은 사과를 먹겠습닉까? (예/아니오): ")
    if eat_eaten_apple == "예":
        health += 5
        inventory.append("먹다남은 사과")
        print("먹다남은 사과를 먹고 허기를 채웠습니다! (체력 + 5)")
        break
    elif eat_eaten_apple == "아니오":
        health -= 10
        print("아침을 걸러 기운이 빠집니다... (체력 -10)")
        break
    else:
        print("잘못 입력하셨습니다. (예/아니오) 중에서 선택하여 입력해주세요. ")

# 어떤 활동을 하고 난 뒤 항상 체력 확인 상태창

print(f"현재 체력: {health}")
if health <= 0:
    print("체력이 다 떨어져 쓰러졌습니다. Byebye, worldㅜㅠ")

print("주위에 애옹이와 멍멍이가 있습니다.")

while True:
    petting_animal = input("쓰다듬으시겠습니까? (예/아니오)")
    if petting_animal == "예":
        health += 5
        print("멍멍이와 애옹이가 좋아죽어서 힐링이 돼버렸습니다. (체력 + 5)")
        while True:
            companion = input("멍멍이와 애옹이가 따라가고 싶어합니다. 동행하시겠습니까? (예/아니오)")
            if companion == "예":
                inventory.append("멍멍이", "애옹이")
                break
            elif companion == "아니오":
                print("멍멍이와 애옹이를 두고  떠났습니다.")
                break
            else:
                print("잘못 입력하셨습니다. (예/아니오) 중에서 선택하여 입력해주세요. ")
        break
    elif eat_eaten_apple == "아니오":
        health -= 40
        print("근처에 서식하는 곰을 만나 신체가 찢어질 뻔 했습니다.... (체력 -40)")
        break
    else:
        print("잘못 입력하셨습니다. (예/아니오) 중에서 선택하여 입력해주세요. ")

# 어떤 활동을 하고 난 뒤 항상 체력 확인 상태창

print(f"현재 체력: {health}")
if health <= 0:
    print("체력이 다 떨어져 쓰러졌습니다. Byebye, worldㅜㅠ")

# 선택 처리 함수
def ask_choice(question, yes_action, no_action):
    while True:
        answer = input(question + " (예/아니오): ")
        if answer == "예":
            yes_action()
            break
        elif answer == "아니오":
            no_action()
            break
        else:
            print("잘못 입력하셨습니다. (예/아니오) 중에서 선택해주세요")

# 선택 후 또는 활동 후 체력 확인
def check_health():
    global health
    print(f"현재 체력: {health}")
    if health <= 0:
        print("체력이 다 떨어져 쓰러졌습니다. Byebye, worldㅜㅠ")
        exit() # 게임종료

# 게임 속 이벤트를 함수로 정의하자
def morning_event():
    def eat_yes():
        global health, inventory
        health += 5
        inventory.append("먹다남은 사과")
        print("먹다남은 사과를 먹고 허기를 채웠습니다! (체력 +5)")

    def eat_no():
        global health
        health -= 10
        print("아침을 걸러 기운이 빠집니다... (체력 -10)")

    ask_choice("먹다남은 사과를 먹겠습니까?", eat_yes, eat_no)
    check_health()