while True: # 무한루프
    ID = "ASDF"
    PW = "1234"

    print("======로그인 화면======")
    print("1. 로그인")
    print("2. 종료")

    num = input("선택 : ")

    if num == "2":
        print("종료합니다.")
        break
    
    elif num == "1":
        ID = input("ID : ")
        PW = input("PW : ")

        while ((ID != "ASDF") or (PW != "1234")):

            print("로그인 실패. 돌아가.")
            ID = input("ID : ")
            PW = input("PW : ")
        
        while ((ID == "ASDF") or (PW == "1234")):

            print("로그인 성공!")
            print("======메뉴======")
            print("1. 정보 보기")
            print("2. 설정")
            print("3. 로그아웃")

            n = input("메뉴 선택 : ")

            if n == "1":
                print("회원님의 정보입니다.")
            
            elif n == "2":
                print("설정 메뉴입니다.")

            elif n == "3":
                print("로그아웃합니다.")
                break
            else:
                print("다시 입력하세요.")
            continue
    else:
        print("다시 입력하세요.")