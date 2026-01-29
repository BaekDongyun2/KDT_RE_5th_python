// 원시자료형

// 1. 문자열 (string)
const str1 = "굿모닝"
console.log(str);

// 문자열 연산
const str2 = "오늘도 화이팅╰(*°▽°*)╯"
console.log(str1 + str2);


const name = "Dongyun2";
const age = 27;
console.log('안녕하세요~ 저는 ' + name + '이고, 나이는 ' + age + '살 입니다😊')
// 안녕하세요~ 저는 Dongyun2이고, 나이는 27살 입니다😊

// 템플릿 리터럴
// 변수와 문자열을 함께 쓸 수 있도록 하는 문법
console.long(`안녕하세요~ 저는 ${name}이고, 나이는 ${age}살 입니다😊`);

console.log(`변수말고 코드 실행도 가능하다 ${4+6}`)

//=======================================================================

// 2. 숫자형 (number)

// 정수와 실수를 구분하지 않음
const num1 = 100;
const num2 = 3.14; // num2 = 1;이건 안됨 <= 이미 const로 변수 선언 했으니까
console.log('숫자형', num1, num2);

//=======================================================================

// 3. 불리언/논리형(boolean)

// 참/거짓을 표현하는 true, false
const isTrue = true;
const isFalse = false;
console.log("불리언", isTrue, isFalse);

// 4. null (빈 값)

// 의도적으로 값을 비운 상태
// "값이 없음"을 명시
let isVar = null;
console.log(isVar);
isVar = '이렇게 이후 값이 할당될 수 있음';
console.log(isVar);

//=======================================================================

// 5. undefined
// 값이 정의(할당)되지 않은 상태
let x;
console.log(x1); // undefined 출력
//console.log(x2); // 할당되지 않은 변수로 에러 발생

//=======================================================================

// [객체 자료형]

// 1. 배열 (array)
const fruits = ["청포도", "오렌지", "체리", "말랑복숭아", "망고스틴"]
console.log("배열", fruits);

// 인덱싱s
console.log(fruits[3]);
console.log(fruits[-1]); // undefined

// at 활용 시 음수 인덱싱 사용 가능
console.log(fruits.at(2)); // 체리
console.log(fruits.at(-1)); // 망고스틴

fruits[3] = '딱딱복숭아';
console.log(fruits); // 말랑복숭아 -> 딱딱복숭아

// 배열 안에 요소로 배열 넣을 수 있음
const korean = [
    ["가", "나", "다"],
    ["라", "마", "바"],
    ["사", "아", "자"]
];

console.log(korean[0][1]); // 나
korean[2][2] = '하';
console.log(korean[2][2]);   

// 키-값 쌍을 값으로 가짐
let cat = {
    name: "장화",
    age: 18,
    isCute: true,
    meow: function() {
        return '야옹';
    },
};

console.log("객체", cat);

// 객체의 값 조회
// 1) 점 표기법
// 키가 문자열인 경우만 가능
console.log(cat.name);
console.log(cat.age);
// console.log(cat.12); // 키가 숫자인 경우 접근 못함

// 2) 대괄호 표기법
console.log(cat["name"]);
console.log(cat["age"]);
console.log(cat[12]); // 키가 숫자여도 접근 간으

cat.meow(); // '야옹'이라는 문자열이 리턴됨
console.log(cat.meow());

let catMeow = cat.meow();
console.log(catMeow);

let cat2 = {
    name: "장화",
    age: 18,
    isCute: true,
    12: "12",
    meow: function() {
        alert (야옹22);
    },
};

cat2.meow(); // cat2라는 객체의 meow키 값을 실행시키는 코드

let cat3 = {
    name: "장화",
    age: 18,
    isCute: true,
    12: '12',
    meow: function(str) {
        return str;
    },
};

cat3.meow('야옹야옹') // 매개변수로 전달한 "야옹야옹"을 리턴
// alert(cat3.meow('야옹야옹));
// alert(cat.meow('멍멍'));

//=======================================================================

// 자료형 확인 (typeof)
console.log(typeof '문자'); // string
console.log(typeof 100); // number
console.log(typeof 3.14); // number
console.log(typeof true); // boolean
console.log(typeof false); // boolean
console.log(typeof null); // object
console.log(typeof undefined); // undefined
console.log(typeof fruits); // object --> 배열은 object 하위의 array이고,
                            // array에는 매서드들이 자동으로 포함되어 typeof로 자료형 확인 시 object로 출력됨
console.log(typeof cat); // object


// 실습1.
let mongryong = {
    name : "이몽룡",
    age : 18,
    like: ['강아지', '고양이'],
    isMarried: true,
    girlfriend: {name: '성춘향', age: 16}
};

console.log("춘향전", mongryong);

//=======================================================================

// 형변환

// 1. 암시적 형변환
console.log('암시적 형변환 1', '2' + 3);
// 기대: 암시적 형변환 (1), 2(문자열)3(숫자)
// 결과: 암시적 형변환 (1), 2(문자열)3(문자열)

console.log('암시적 형변환 (2)', typeof (100 +  '1'));
// 기대: 에러
    // 숫자 더하기 문자는 타입(자료형)을 알 수 없기 때문
// 결과: 암시적 형변환 (2) string
// JS가 자기 마음대로 숫자를 문자로 변환해버림

// 2. 명시적 형변환

// 2-1. 문자열로 변환: String(), .toString()

let string1 = 123;
let string2 = true;
let string3 = undefined;

// String() 사용
console.log(String(string1), typeof String(string1)); // 숫자 123은 문자열 "123"으로 변환
console.log(String(string2), typeof String(string2)); // true
console.log(String(string3), typeof String(string3)); // undefined

// .toString() 사용
console.log(string1.toString(), typeof string1.toString());
console.log(string2.toString(), typeof string2.toString());
// console.log(string3.toString(), typeof string3.toString()); // 변수 값이 없기 때문에 변환 불가해서 에러\

// 2-2. 숫자로 변환: Number(), parseInt()

let Number1 = '123';
let Number2 = false;
let Number3 = '진짜 문자열' ;
let Number4 = 3.14;
let Number5 = '3.14';

// Number() 사용
console.log(Number(Number1), typeof Number(number1)); // 123
console.log(Number(Number2), typeof Number(number2)); // 0 -> false는 다르게 표현하면 0이기 때문에 숫자 변환 시
console.log(Number(Number3), typeof Number(number3)); // NaN(Not a Number)
console.log(Number(Number4), typeof Number(number4)); // 3.14
console.log(Number(Number5), typeof Number(number5)); // 3.14

// "정의되지 않음" => 값이 아예 없는 것 => NaN
console.log(Number(undefined), typeof Number(undefined)); // NaN

// 값이 없음을 정의 => 값이 없다는 것을 표현하는 값인 0으로 변환
console.log(Number(null), typeof Number(null)); // 0

// parseInt() 사용 => 소수점 버리고 정수로 출력
console.log(parseInt(number1), typeof parseInt(number1)); // 123
console.log(parseInt(number4), typeof parseInt(number4)); // 3
console.log(parseInt(number5), typeof parseInt(number5)); // 3
console.log(parseInt(3.8), typeof parseInt(3.8)); // 3 -> 소수점 버림

// parseFloat() 사용 => 소수점까지 모두 변환, 자료형은 number로 출력됨
console.log('=== parseFloat 출력 결과 ===');
console.log(parseFloat(number4), typeof parsefloat(number4)); // 3.14
console.log(parseFloat(number5), typeof parsefloat(number5)); // 3.14
console.log(parseFloat(3.8), typeof parsefloat(3.8)); // 3.8

// 실습2.
let mathScore1 = prompt('수학점수 입력');
let engScore1 = prompt('영어점수 입력');
let avgScore1 = (Number(mathScore1) + Number(engScore1)) / 2;
alert(`평균 점수 ${avgScore1}점 입니다.`);