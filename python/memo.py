class Book:
    def __init__(self, title, author,total_pages, current_page):
        self.x1 = title
        self.x2 = author
        self.x3 = total_pages
        self.x4 = current_page

    def read_page(self):
        if self.x4 > self.x3:
            print("책의 범위를 벗어났습니다.")
        else:
            print(f"현재 {self.x4}페이지를 읽으시고 있는 중입니다.")
        pass

    # def read_page(self, page):
    #     self.x4 += page

    #     if page > self.x3:
    #         self.x4 = self.x3      
    #         print("책의 범위를 벗어났습니다.")
    #     else:
    #         print(f"현재 {page}페이지를 읽으시고 있는 중입니다.")
    #     pass

    def progress(self):
        ratio = self.x4 / self.x3 * 100
        result = round(ratio, 1) # 소수점 첫 째 자리까지 반올림
        print(f"전체 중 {result}(%) 읽으셨습니다.")

Dongyuns_Story = Book("Dongyuns_story", "Dongyun2", 500, 245)
Dongyuns_Story.read_page() 
Dongyuns_Story.progress()

class Person2:
    def __init__(self, name, age):
        # public
        self.name = name
        # private: 언더바(__) 두 개를 변수 앞에 붙여서 정의
        self.__age = age
        
        # getter
        def get_age(self):
            return self.__age

        # setter
        def set_age(self, value):
            if value > 120 or value < 0:
                print("유효하지 않은 나이입니다.")
            else:
                self.__age = value

p1 = Person2("lee", 15)
print(p1.name)
#print(p1.__age)
print(p1.get_age())
p1.set_age(-10)

with open("with_example.txt", "a", encoding="utf-8") as f1:
    while True:
        text = input("저장할 내용을 입력해주세요(종료: z)")
        if text == "Z" or text == "z":
            break
        f1.write(text + "\n")